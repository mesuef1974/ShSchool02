------------------------------------------------------------
-- Shahania School – Domain Schema (NOAUTH v2, PostgreSQL 13+ / 17)
-- Clean, idempotent-ish (safe on re-run where possible)
-- Author: Sufian & Copilot | Date: 2026-03-15
------------------------------------------------------------

-- 0) Extensions (safe if already created)
CREATE EXTENSION IF NOT EXISTS pgcrypto;
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

------------------------------------------------------------
-- 0.1) Common trigger function: auto-update updated_at & row_version
------------------------------------------------------------
CREATE OR REPLACE FUNCTION set_updated_at()
RETURNS trigger LANGUAGE plpgsql AS $$
BEGIN
  NEW.updated_at = NOW();
  NEW.row_version = COALESCE(OLD.row_version, 0) + 1;
  RETURN NEW;
END;
$$;

------------------------------------------------------------
-- 1) Identity & RBAC (Scoped)
------------------------------------------------------------
CREATE TABLE IF NOT EXISTS identity_role (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name VARCHAR(100) NOT NULL UNIQUE,
  description TEXT NOT NULL DEFAULT '',
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  deleted_at TIMESTAMPTZ,
  row_version INT NOT NULL DEFAULT 1
);

CREATE TABLE IF NOT EXISTS identity_permission (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  code VARCHAR(150) NOT NULL UNIQUE,
  description TEXT NOT NULL DEFAULT '',
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  deleted_at TIMESTAMPTZ,
  row_version INT NOT NULL DEFAULT 1
);

CREATE TABLE IF NOT EXISTS identity_rolepermission (
  id BIGSERIAL PRIMARY KEY,
  role_id UUID NOT NULL REFERENCES identity_role(id) DEFERRABLE INITIALLY DEFERRED,
  permission_id UUID NOT NULL REFERENCES identity_permission(id) DEFERRABLE INITIALLY DEFERRED,
  UNIQUE(role_id, permission_id)
);

-- ملاحظة: الربط بالمستخدمين يكون عبر جدول Django (auth_user) عادةً؛
-- لذلك نستخدم جسرًا عامًا دون FK مباشر هنا لتفادي التعارض:
CREATE TABLE IF NOT EXISTS identity_userrole (
  id BIGSERIAL PRIMARY KEY,
  user_id INT NOT NULL, -- يشير إلى auth_user.id (دون FK صريح)
  role_id UUID NOT NULL REFERENCES identity_role(id) DEFERRABLE INITIALLY DEFERRED,
  UNIQUE (user_id, role_id)
);

-- نطاق الدور (اختياري): ربط الدور بسياق مدرسة/سنة/صف
CREATE TABLE IF NOT EXISTS identity_role_scope (
  id BIGSERIAL PRIMARY KEY,
  user_id INT NOT NULL,
  role_id UUID NOT NULL REFERENCES identity_role(id) DEFERRABLE INITIALLY DEFERRED,
  school_id UUID,
  year_id   UUID,
  class_room_id UUID,
  created_at   TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at   TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  deleted_at   TIMESTAMPTZ,
  row_version  INT NOT NULL DEFAULT 1,
  UNIQUE (user_id, role_id, school_id, year_id, class_room_id)
);

CREATE TRIGGER tr_identity_role_u        BEFORE UPDATE ON identity_role        FOR EACH ROW EXECUTE FUNCTION set_updated_at();
CREATE TRIGGER tr_identity_perm_u        BEFORE UPDATE ON identity_permission  FOR EACH ROW EXECUTE FUNCTION set_updated_at();
CREATE TRIGGER tr_identity_role_scope_u  BEFORE UPDATE ON identity_role_scope  FOR EACH ROW EXECUTE FUNCTION set_updated_at();

------------------------------------------------------------
-- 2) Core: School / Year / Term / Grade / Subject / Room / Classroom
------------------------------------------------------------
CREATE TABLE IF NOT EXISTS core_school (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name_ar VARCHAR(200) NOT NULL,
  name_en VARCHAR(200) NOT NULL,
  moehe_code VARCHAR(50) NOT NULL UNIQUE,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  deleted_at TIMESTAMPTZ,
  row_version INT NOT NULL DEFAULT 1
);

CREATE TABLE IF NOT EXISTS core_year (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  label VARCHAR(20) NOT NULL,      -- 2025-2026
  start_date DATE NOT NULL,
  end_date   DATE NOT NULL,
  school_id UUID NOT NULL REFERENCES core_school(id) DEFERRABLE INITIALLY DEFERRED,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  deleted_at TIMESTAMPTZ,
  row_version INT NOT NULL DEFAULT 1
);
CREATE INDEX IF NOT EXISTS ix_year_school ON core_year(school_id);

CREATE TABLE IF NOT EXISTS core_term (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  code VARCHAR(10) NOT NULL,       -- T1/T2/T3
  start_date DATE NOT NULL,
  end_date   DATE NOT NULL,
  year_id UUID NOT NULL REFERENCES core_year(id) DEFERRABLE INITIALLY DEFERRED,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  deleted_at TIMESTAMPTZ,
  row_version INT NOT NULL DEFAULT 1,
  CONSTRAINT uq_core_term_year_code UNIQUE(year_id, code)
);
CREATE INDEX IF NOT EXISTS ix_term_year ON core_term(year_id);

CREATE TABLE IF NOT EXISTS core_grade (
  code SMALLINT PRIMARY KEY,  -- 7..12
  label_ar VARCHAR(50) NOT NULL,
  label_en VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS core_subject (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name_ar VARCHAR(200) NOT NULL,
  name_en VARCHAR(200) NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  deleted_at TIMESTAMPTZ,
  row_version INT NOT NULL DEFAULT 1
);

CREATE TABLE IF NOT EXISTS core_room (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  code VARCHAR(50) NOT NULL UNIQUE,
  room_type VARCHAR(50) NOT NULL,   -- class/lab/hall...
  capacity INT NOT NULL CHECK (capacity >= 0),
  school_id UUID NOT NULL REFERENCES core_school(id) DEFERRABLE INITIALLY DEFERRED,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  deleted_at TIMESTAMPTZ,
  row_version INT NOT NULL DEFAULT 1
);
CREATE INDEX IF NOT EXISTS ix_room_school ON core_room(school_id);

CREATE TABLE IF NOT EXISTS core_classroom (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  grade SMALLINT NOT NULL REFERENCES core_grade(code) DEFERRABLE INITIALLY DEFERRED,
  section VARCHAR(10) NOT NULL,
  school_id UUID NOT NULL REFERENCES core_school(id) DEFERRABLE INITIALLY DEFERRED,
  year_id   UUID NOT NULL REFERENCES core_year(id) DEFERRABLE INITIALLY DEFERRED,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  deleted_at TIMESTAMPTZ,
  row_version INT NOT NULL DEFAULT 1,
  CONSTRAINT uq_core_classroom_school_year_grade_section UNIQUE(school_id, year_id, grade, section)
);
CREATE INDEX IF NOT EXISTS ix_classroom_school ON core_classroom(school_id);
CREATE INDEX IF NOT EXISTS ix_classroom_year   ON core_classroom(year_id);

CREATE TRIGGER tr_core_school_u     BEFORE UPDATE ON core_school     FOR EACH ROW EXECUTE FUNCTION set_updated_at();
CREATE TRIGGER tr_core_year_u       BEFORE UPDATE ON core_year       FOR EACH ROW EXECUTE FUNCTION set_updated_at();
CREATE TRIGGER tr_core_term_u       BEFORE UPDATE ON core_term       FOR EACH ROW EXECUTE FUNCTION set_updated_at();
CREATE TRIGGER tr_core_subject_u    BEFORE UPDATE ON core_subject    FOR EACH ROW EXECUTE FUNCTION set_updated_at();
CREATE TRIGGER tr_core_room_u       BEFORE UPDATE ON core_room       FOR EACH ROW EXECUTE FUNCTION set_updated_at();
CREATE TRIGGER tr_core_classroom_u  BEFORE UPDATE ON core_classroom  FOR EACH ROW EXECUTE FUNCTION set_updated_at();

------------------------------------------------------------
-- 3) People: Student / Guardian / Staff / Enrollment / Teaching Assignment
------------------------------------------------------------
CREATE TABLE IF NOT EXISTS people_student (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  first_name_ar VARCHAR(100) NOT NULL,
  last_name_ar  VARCHAR(100) NOT NULL,
  first_name_en VARCHAR(100) NOT NULL,
  last_name_en  VARCHAR(100) NOT NULL,
  national_id   VARCHAR(32),        -- [SENSITIVE: PDPPL-ID]
  birth_date    DATE NOT NULL,      -- [SENSITIVE: DOB]
  gender        VARCHAR(1) NOT NULL CHECK (gender IN ('M','F')),
  phone         VARCHAR(32) NOT NULL,   -- [SENSITIVE: CONTACT]
  email         VARCHAR(254) NOT NULL,  -- [SENSITIVE: CONTACT]
  nationality_code VARCHAR(5),      -- FK -> refdata_lookup_nationality (اختياري لاحقًا)
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  deleted_at TIMESTAMPTZ,
  row_version INT NOT NULL DEFAULT 1,
  retention_until DATE
);
COMMENT ON COLUMN people_student.national_id IS 'SENSITIVE:PDPPL-ID';
COMMENT ON COLUMN people_student.birth_date  IS 'SENSITIVE:PDPPL-DOB';
COMMENT ON COLUMN people_student.phone       IS 'SENSITIVE:PDPPL-CONTACT';
COMMENT ON COLUMN people_student.email       IS 'SENSITIVE:PDPPL-CONTACT';

CREATE TABLE IF NOT EXISTS people_guardian (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  first_name_ar VARCHAR(100) NOT NULL,
  last_name_ar  VARCHAR(100) NOT NULL,
  phone         VARCHAR(32) NOT NULL, -- [SENSITIVE: CONTACT]
  email         VARCHAR(254) NOT NULL, -- [SENSITIVE: CONTACT]
  relation_to_student VARCHAR(30),
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  deleted_at TIMESTAMPTZ,
  row_version INT NOT NULL DEFAULT 1
);
COMMENT ON COLUMN people_guardian.phone IS 'SENSITIVE:PDPPL-CONTACT';
COMMENT ON COLUMN people_guardian.email IS 'SENSITIVE:PDPPL-CONTACT';

CREATE TABLE IF NOT EXISTS people_studentguardian (
  id BIGSERIAL PRIMARY KEY,
  student_id  UUID NOT NULL REFERENCES people_student(id) DEFERRABLE INITIALLY DEFERRED,
  guardian_id UUID NOT NULL REFERENCES people_guardian(id) DEFERRABLE INITIALLY DEFERRED,
  relation    VARCHAR(30) NOT NULL,  -- father/mother/...
  is_primary  BOOLEAN NOT NULL DEFAULT false,
  UNIQUE(student_id, guardian_id)
);

CREATE TABLE IF NOT EXISTS people_staff (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  first_name_ar VARCHAR(100) NOT NULL,
  last_name_ar  VARCHAR(100) NOT NULL,
  job_title     VARCHAR(120) NOT NULL,
  email         VARCHAR(254) NOT NULL,
  phone         VARCHAR(32),
  department    VARCHAR(120),
  status        VARCHAR(30) NOT NULL DEFAULT 'active',
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  deleted_at TIMESTAMPTZ,
  row_version INT NOT NULL DEFAULT 1
);

CREATE TABLE IF NOT EXISTS people_enrollment (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  grade SMALLINT NOT NULL REFERENCES core_grade(code) DEFERRABLE INITIALLY DEFERRED,
  status VARCHAR(20) NOT NULL CHECK (status IN ('active','transferred','graduated','withdrawn')),
  class_room_id UUID NOT NULL REFERENCES core_classroom(id) DEFERRABLE INITIALLY DEFERRED,
  school_id     UUID NOT NULL REFERENCES core_school(id) DEFERRABLE INITIALLY DEFERRED,
  year_id       UUID NOT NULL REFERENCES core_year(id) DEFERRABLE INITIALLY DEFERRED,
  student_id    UUID NOT NULL REFERENCES people_student(id) DEFERRABLE INITIALLY DEFERRED,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  deleted_at TIMESTAMPTZ,
  row_version INT NOT NULL DEFAULT 1,
  CONSTRAINT uq_enrollment_student_school_year_grade_class UNIQUE(student_id, school_id, year_id, grade, class_room_id)
);
CREATE INDEX IF NOT EXISTS ix_enrollment_student ON people_enrollment(student_id);
CREATE INDEX IF NOT EXISTS ix_enrollment_school  ON people_enrollment(school_id);
CREATE INDEX IF NOT EXISTS ix_enrollment_year    ON people_enrollment(year_id);
CREATE INDEX IF NOT EXISTS ix_enrollment_class   ON people_enrollment(class_room_id);

CREATE TABLE IF NOT EXISTS people_teachingassignment (
  id BIGSERIAL PRIMARY KEY,
  class_room_id UUID NOT NULL REFERENCES core_classroom(id) DEFERRABLE INITIALLY DEFERRED,
  subject_id    UUID NOT NULL REFERENCES core_subject(id)   DEFERRABLE INITIALLY DEFERRED,
  teacher_id    UUID NOT NULL REFERENCES people_staff(id)   DEFERRABLE INITIALLY DEFERRED,
  UNIQUE(teacher_id, class_room_id, subject_id)
);

CREATE TRIGGER tr_people_student_u     BEFORE UPDATE ON people_student     FOR EACH ROW EXECUTE FUNCTION set_updated_at();
CREATE TRIGGER tr_people_guardian_u    BEFORE UPDATE ON people_guardian    FOR EACH ROW EXECUTE FUNCTION set_updated_at();
CREATE TRIGGER tr_people_staff_u       BEFORE UPDATE ON people_staff       FOR EACH ROW EXECUTE FUNCTION set_updated_at();
CREATE TRIGGER tr_people_enrollment_u  BEFORE UPDATE ON people_enrollment  FOR EACH ROW EXECUTE FUNCTION set_updated_at();

------------------------------------------------------------
-- 4) Timetable & Attendance
------------------------------------------------------------
CREATE TABLE IF NOT EXISTS timetable_timetablerule (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name VARCHAR(120) NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  deleted_at TIMESTAMPTZ,
  row_version INT NOT NULL DEFAULT 1
);

CREATE TABLE IF NOT EXISTS timetable_timetableslot (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  day_of_week SMALLINT NOT NULL CHECK (day_of_week BETWEEN 1 AND 7),
  period SMALLINT NOT NULL CHECK (period BETWEEN 1 AND 10),
  class_room_id UUID NOT NULL REFERENCES core_classroom(id) DEFERRABLE INITIALLY DEFERRED,
  room_id   UUID REFERENCES core_room(id) DEFERRABLE INITIALLY DEFERRED,
  subject_id UUID NOT NULL REFERENCES core_subject(id) DEFERRABLE INITIALLY DEFERRED,
  teacher_id UUID NOT NULL REFERENCES people_staff(id) DEFERRABLE INITIALLY DEFERRED,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  deleted_at TIMESTAMPTZ,
  row_version INT NOT NULL DEFAULT 1,
  CONSTRAINT uq_tslot_class_day_period UNIQUE(class_room_id, day_of_week, period)
);

CREATE TABLE IF NOT EXISTS attendance_attendancerecord (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  enrollment_id UUID NOT NULL REFERENCES people_enrollment(id) DEFERRABLE INITIALLY DEFERRED,
  date DATE NOT NULL,
  period SMALLINT NOT NULL CHECK (period BETWEEN 1 AND 10),
  status VARCHAR(10) NOT NULL CHECK (status IN ('present','absent','late','excused')),
  note TEXT,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  deleted_at TIMESTAMPTZ,
  row_version INT NOT NULL DEFAULT 1,
  CONSTRAINT uq_attendance_enrollment_date_period UNIQUE(enrollment_id, date, period)
);
CREATE INDEX IF NOT EXISTS ix_attendance_by_date ON attendance_attendancerecord(date);

CREATE TRIGGER tr_timetable_rule_u  BEFORE UPDATE ON timetable_timetablerule  FOR EACH ROW EXECUTE FUNCTION set_updated_at();
CREATE TRIGGER tr_timetable_slot_u  BEFORE UPDATE ON timetable_timetableslot  FOR EACH ROW EXECUTE FUNCTION set_updated_at();
CREATE TRIGGER tr_attendance_u      BEFORE UPDATE ON attendance_attendancerecord FOR EACH ROW EXECUTE FUNCTION set_updated_at();

------------------------------------------------------------
-- 5) Assessment
------------------------------------------------------------
CREATE TABLE IF NOT EXISTS assessment_exam (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name VARCHAR(150) NOT NULL,
  term_code VARCHAR(10) NOT NULL,
  subject_id UUID NOT NULL REFERENCES core_subject(id) DEFERRABLE INITIALLY DEFERRED,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  deleted_at TIMESTAMPTZ,
  row_version INT NOT NULL DEFAULT 1
);

CREATE TABLE IF NOT EXISTS assessment_examsession (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  exam_id UUID NOT NULL REFERENCES assessment_exam(id) DEFERRABLE INITIALLY DEFERRED,
  room_id UUID NOT NULL REFERENCES core_room(id) DEFERRABLE INITIALLY DEFERRED,
  date DATE NOT NULL,
  start_time TIME NOT NULL,
  end_time   TIME NOT NULL,
  invigilator_staff_id UUID REFERENCES people_staff(id) DEFERRABLE INITIALLY DEFERRED,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  deleted_at TIMESTAMPTZ,
  row_version INT NOT NULL DEFAULT 1,
  CONSTRAINT uq_examsession_exam_room_datetime UNIQUE (exam_id, room_id, date, start_time)
);

CREATE TABLE IF NOT EXISTS assessment_examresult (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  score NUMERIC(6,2) NOT NULL,
  enrollment_id UUID NOT NULL REFERENCES people_enrollment(id) DEFERRABLE INITIALLY DEFERRED,
  exam_id UUID NOT NULL REFERENCES assessment_exam(id) DEFERRABLE INITIALLY DEFERRED,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  deleted_at TIMESTAMPTZ,
  row_version INT NOT NULL DEFAULT 1,
  CONSTRAINT uq_examresult_enrollment_exam UNIQUE (enrollment_id, exam_id)
);

CREATE TABLE IF NOT EXISTS assessment_appeal (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  reason TEXT NOT NULL,
  decision TEXT NOT NULL,
  enrollment_id UUID NOT NULL REFERENCES people_enrollment(id) DEFERRABLE INITIALLY DEFERRED,
  exam_id UUID NOT NULL REFERENCES assessment_exam(id) DEFERRABLE INITIALLY DEFERRED,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  deleted_at TIMESTAMPTZ,
  row_version INT NOT NULL DEFAULT 1,
  CONSTRAINT uq_appeal_enrollment_exam UNIQUE(enrollment_id, exam_id)
);

CREATE TRIGGER tr_exam_u        BEFORE UPDATE ON assessment_exam        FOR EACH ROW EXECUTE FUNCTION set_updated_at();
CREATE TRIGGER tr_examsession_u BEFORE UPDATE ON assessment_examsession FOR EACH ROW EXECUTE FUNCTION set_updated_at();
CREATE TRIGGER tr_examresult_u  BEFORE UPDATE ON assessment_examresult  FOR EACH ROW EXECUTE FUNCTION set_updated_at();
CREATE TRIGGER tr_appeal_u      BEFORE UPDATE ON assessment_appeal      FOR EACH ROW EXECUTE FUNCTION set_updated_at();

------------------------------------------------------------
-- 6) Behavior & Discipline
------------------------------------------------------------
CREATE TABLE IF NOT EXISTS behavior_behaviorincident (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  date DATE NOT NULL,
  period SMALLINT,
  place VARCHAR(120) NOT NULL,
  category VARCHAR(80) NOT NULL,
  description TEXT NOT NULL,         -- [SENSITIVE]
  student_id UUID NOT NULL REFERENCES people_student(id) DEFERRABLE INITIALLY DEFERRED,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  deleted_at TIMESTAMPTZ,
  row_version INT NOT NULL DEFAULT 1,
  retention_until DATE
);
COMMENT ON COLUMN behavior_behaviorincident.description IS 'SENSITIVE:Behavior';

CREATE TABLE IF NOT EXISTS behavior_committee (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  incident_id UUID NOT NULL REFERENCES behavior_behaviorincident(id) DEFERRABLE INITIALLY DEFERRED,
  meeting_date DATE NOT NULL,
  notes TEXT,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  deleted_at TIMESTAMPTZ,
  row_version INT NOT NULL DEFAULT 1,
  CONSTRAINT uq_behavior_committee_incident UNIQUE(incident_id)
);

CREATE TABLE IF NOT EXISTS behavior_sanction (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  incident_id UUID NOT NULL REFERENCES behavior_behaviorincident(id) DEFERRABLE INITIALLY DEFERRED,
  sanction_type VARCHAR(80) NOT NULL,
  level SMALLINT NOT NULL,
  decided_on DATE NOT NULL,
  executed BOOLEAN NOT NULL DEFAULT false,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  deleted_at TIMESTAMPTZ,
  row_version INT NOT NULL DEFAULT 1
);

CREATE TRIGGER tr_behavior_incident_u BEFORE UPDATE ON behavior_behaviorincident FOR EACH ROW EXECUTE FUNCTION set_updated_at();
CREATE TRIGGER tr_behavior_committee_u BEFORE UPDATE ON behavior_committee FOR EACH ROW EXECUTE FUNCTION set_updated_at();
CREATE TRIGGER tr_behavior_sanction_u  BEFORE UPDATE ON behavior_sanction  FOR EACH ROW EXECUTE FUNCTION set_updated_at();

------------------------------------------------------------
-- 7) School Health
------------------------------------------------------------
CREATE TABLE IF NOT EXISTS health_clinicvisit (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  date DATE NOT NULL,
  reason VARCHAR(200) NOT NULL,
  details_enc BYTEA,                    -- [SENSITIVE: HEALTH-Encrypted]
  student_id UUID NOT NULL REFERENCES people_student(id) DEFERRABLE INITIALLY DEFERRED,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  deleted_at TIMESTAMPTZ,
  row_version INT NOT NULL DEFAULT 1,
  retention_until DATE
);
COMMENT ON COLUMN health_clinicvisit.details_enc IS 'SENSITIVE:HEALTH-ENCRYPTED';

CREATE TABLE IF NOT EXISTS health_medicationlog (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  date DATE NOT NULL,
  medicine VARCHAR(120) NOT NULL,
  dose VARCHAR(60) NOT NULL,
  notes_enc BYTEA,                       -- [SENSITIVE]
  student_id UUID NOT NULL REFERENCES people_student(id) DEFERRABLE INITIALLY DEFERRED,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  deleted_at TIMESTAMPTZ,
  row_version INT NOT NULL DEFAULT 1,
  retention_until DATE
);
COMMENT ON COLUMN health_medicationlog.notes_enc IS 'SENSITIVE:HEALTH-ENCRYPTED';

CREATE TABLE IF NOT EXISTS health_immunization (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  student_id UUID NOT NULL REFERENCES people_student(id) DEFERRABLE INITIALLY DEFERRED,
  vaccine VARCHAR(120) NOT NULL,
  dose_no SMALLINT,
  taken_on DATE,
  notes TEXT,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  deleted_at TIMESTAMPTZ,
  row_version INT NOT NULL DEFAULT 1
);

CREATE TABLE IF NOT EXISTS health_healthalert (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  student_id UUID NOT NULL REFERENCES people_student(id) DEFERRABLE INITIALLY DEFERRED,
  alert_type VARCHAR(60) NOT NULL,   -- Allergy/Emergency/Chronic...
  details_enc BYTEA,
  active BOOLEAN NOT NULL DEFAULT true,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  deleted_at TIMESTAMPTZ,
  row_version INT NOT NULL DEFAULT 1
);

CREATE TRIGGER tr_health_visit_u   BEFORE UPDATE ON health_clinicvisit   FOR EACH ROW EXECUTE FUNCTION set_updated_at();
CREATE TRIGGER tr_health_med_u     BEFORE UPDATE ON health_medicationlog FOR EACH ROW EXECUTE FUNCTION set_updated_at();
CREATE TRIGGER tr_health_immun_u   BEFORE UPDATE ON health_immunization  FOR EACH ROW EXECUTE FUNCTION set_updated_at();
CREATE TRIGGER tr_health_alert_u   BEFORE UPDATE ON health_healthalert   FOR EACH ROW EXECUTE FUNCTION set_updated_at();

------------------------------------------------------------
-- 8) Transport
------------------------------------------------------------
CREATE TABLE IF NOT EXISTS transport_route (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  code VARCHAR(50) NOT NULL UNIQUE,
  capacity INT NOT NULL CHECK (capacity >= 0),
  supervisor_staff_id UUID,
  driver_name VARCHAR(120),
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  deleted_at TIMESTAMPTZ,
  row_version INT NOT NULL DEFAULT 1
);

CREATE TABLE IF NOT EXISTS transport_route_stop (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  route_id UUID NOT NULL REFERENCES transport_route(id) DEFERRABLE INITIALLY DEFERRED,
  seq SMALLINT NOT NULL,
  name VARCHAR(120) NOT NULL,
  lat NUMERIC(9,6),
  lon NUMERIC(9,6),
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  deleted_at TIMESTAMPTZ,
  row_version INT NOT NULL DEFAULT 1,
  CONSTRAINT uq_route_stop UNIQUE(route_id, seq)
);

CREATE TABLE IF NOT EXISTS transport_studentrider (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  route_id UUID NOT NULL REFERENCES transport_route(id) DEFERRABLE INITIALLY DEFERRED,
  student_id UUID NOT NULL REFERENCES people_student(id) DEFERRABLE INITIALLY DEFERRED,
  pickup_stop_id UUID REFERENCES transport_route_stop(id) DEFERRABLE INITIALLY DEFERRED,
  dropoff_stop_id UUID REFERENCES transport_route_stop(id) DEFERRABLE INITIALLY DEFERRED,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  deleted_at TIMESTAMPTZ,
  row_version INT NOT NULL DEFAULT 1,
  CONSTRAINT uq_student_route UNIQUE(student_id, route_id)
);

CREATE TABLE IF NOT EXISTS transport_ride_log (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  route_id UUID NOT NULL REFERENCES transport_route(id) DEFERRABLE INITIALLY DEFERRED,
  date DATE NOT NULL,
  departed_at TIME,
  arrived_at TIME,
  notes TEXT,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  deleted_at TIMESTAMPTZ,
  row_version INT NOT NULL DEFAULT 1,
  CONSTRAINT uq_ride_log UNIQUE(route_id, date)
);

CREATE TABLE IF NOT EXISTS transport_delay_log (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  ride_id UUID NOT NULL REFERENCES transport_ride_log(id) DEFERRABLE INITIALLY DEFERRED,
  minutes_late SMALLINT NOT NULL CHECK (minutes_late >= 0),
  reason VARCHAR(120),
  notified BOOLEAN NOT NULL DEFAULT false,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  deleted_at TIMESTAMPTZ,
  row_version INT NOT NULL DEFAULT 1
);

CREATE TRIGGER tr_transport_route_u      BEFORE UPDATE ON transport_route      FOR EACH ROW EXECUTE FUNCTION set_updated_at();
CREATE TRIGGER tr_transport_route_stop_u BEFORE UPDATE ON transport_route_stop FOR EACH ROW EXECUTE FUNCTION set_updated_at();
CREATE TRIGGER tr_transport_student_u    BEFORE UPDATE ON transport_studentrider FOR EACH ROW EXECUTE FUNCTION set_updated_at();
CREATE TRIGGER tr_transport_ride_u       BEFORE UPDATE ON transport_ride_log   FOR EACH ROW EXECUTE FUNCTION set_updated_at();
CREATE TRIGGER tr_transport_delay_u      BEFORE UPDATE ON transport_delay_log  FOR EACH ROW EXECUTE FUNCTION set_updated_at();

------------------------------------------------------------
-- 9) Library
------------------------------------------------------------
CREATE TABLE IF NOT EXISTS library_librarytitle (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  isbn VARCHAR(20) NOT NULL,
  title VARCHAR(300) NOT NULL,
  author VARCHAR(300) NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  deleted_at TIMESTAMPTZ,
  row_version INT NOT NULL DEFAULT 1
);

CREATE TABLE IF NOT EXISTS library_librarycopy (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  barcode VARCHAR(50) NOT NULL UNIQUE,
  status VARCHAR(20) NOT NULL,  -- available/loaned/reserved/…
  title_id UUID NOT NULL REFERENCES library_librarytitle(id) DEFERRABLE INITIALLY DEFERRED,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  deleted_at TIMESTAMPTZ,
  row_version INT NOT NULL DEFAULT 1
);

CREATE TABLE IF NOT EXISTS library_libraryloan (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  issued_on DATE NOT NULL,
  due_on DATE NOT NULL,
  returned_on DATE,
  borrower_staff_id UUID REFERENCES people_staff(id) DEFERRABLE INITIALLY DEFERRED,
  borrower_student_id UUID REFERENCES people_student(id) DEFERRABLE INITIALLY DEFERRED,
  copy_id UUID NOT NULL REFERENCES library_librarycopy(id) DEFERRABLE INITIALLY DEFERRED,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  deleted_at TIMESTAMPTZ,
  row_version INT NOT NULL DEFAULT 1
);

CREATE TABLE IF NOT EXISTS library_reservation (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  copy_id UUID NOT NULL REFERENCES library_librarycopy(id) DEFERRABLE INITIALLY DEFERRED,
  student_id UUID REFERENCES people_student(id) DEFERRABLE INITIALLY DEFERRED,
  staff_id UUID REFERENCES people_staff(id) DEFERRABLE INITIALLY DEFERRED,
  reserved_on TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  expires_on  TIMESTAMPTZ NOT NULL,
  fulfilled BOOLEAN NOT NULL DEFAULT false,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  deleted_at TIMESTAMPTZ,
  row_version INT NOT NULL DEFAULT 1,
  CONSTRAINT uq_reservation_unique_borrower UNIQUE(copy_id, student_id, staff_id, fulfilled)
);

CREATE TRIGGER tr_library_title_u BEFORE UPDATE ON library_librarytitle FOR EACH ROW EXECUTE FUNCTION set_updated_at();
CREATE TRIGGER tr_library_copy_u  BEFORE UPDATE ON library_librarycopy  FOR EACH ROW EXECUTE FUNCTION set_updated_at();
CREATE TRIGGER tr_library_loan_u  BEFORE UPDATE ON library_libraryloan  FOR EACH ROW EXECUTE FUNCTION set_updated_at();
CREATE TRIGGER tr_library_res_u   BEFORE UPDATE ON library_reservation  FOR EACH ROW EXECUTE FUNCTION set_updated_at();

------------------------------------------------------------
-- 10) HR (school-scoped)
------------------------------------------------------------
CREATE TABLE IF NOT EXISTS hr_leave_request (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  staff_id UUID NOT NULL REFERENCES people_staff(id) DEFERRABLE INITIALLY DEFERRED,
  leave_type VARCHAR(40) NOT NULL,
  start_date DATE NOT NULL,
  end_date   DATE NOT NULL,
  status VARCHAR(20) NOT NULL DEFAULT 'pending',
  notes TEXT,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  deleted_at TIMESTAMPTZ,
  row_version INT NOT NULL DEFAULT 1
);

CREATE TABLE IF NOT EXISTS hr_performance_review (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  staff_id UUID NOT NULL REFERENCES people_staff(id) DEFERRABLE INITIALLY DEFERRED,
  year_id UUID NOT NULL REFERENCES core_year(id) DEFERRABLE INITIALLY DEFERRED,
  score NUMERIC(5,2),
  comments TEXT,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  deleted_at TIMESTAMPTZ,
  row_version INT NOT NULL DEFAULT 1
);

CREATE TRIGGER tr_hr_leave_u   BEFORE UPDATE ON hr_leave_request     FOR EACH ROW EXECUTE FUNCTION set_updated_at();
CREATE TRIGGER tr_hr_review_u  BEFORE UPDATE ON hr_performance_review FOR EACH ROW EXECUTE FUNCTION set_updated_at();

------------------------------------------------------------
-- 11) Quality & Operational Plan (QNSA / School Plan)
------------------------------------------------------------
-- اللجان (يمكن استخدامها كـ Quality/SelfReview/Operational)
CREATE TABLE IF NOT EXISTS quality_committee (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  committee_type VARCHAR(30) NOT NULL DEFAULT 'Quality', -- Quality/SelfReview/Operational
  member_name VARCHAR(200) NOT NULL,
  job_title   VARCHAR(150) NOT NULL,
  role_in_committee VARCHAR(50) NOT NULL, -- رئيس/نائب/مقرر/عضو
  responsibility TEXT,                    -- من ملفك
  domain VARCHAR(150),                    -- المجال المسؤول عنه
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  deleted_at TIMESTAMPTZ,
  row_version INT NOT NULL DEFAULT 1
);

-- المنفّذون (coordinators/executors)
CREATE TABLE IF NOT EXISTS quality_plan_executor (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name VARCHAR(200) NOT NULL,
  job_title VARCHAR(150),
  staff_id UUID REFERENCES people_staff(id) DEFERRABLE INITIALLY DEFERRED,
  is_active BOOLEAN NOT NULL DEFAULT true,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  deleted_at TIMESTAMPTZ,
  row_version INT NOT NULL DEFAULT 1
);

-- عناصر الخطة التشغيلية
CREATE TABLE IF NOT EXISTS quality_operational_plan_item (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  year VARCHAR(20) NOT NULL,                  -- 2025-2026
  domain VARCHAR(200),                        -- rank_name
  target_no VARCHAR(40), target TEXT,
  indicator_no VARCHAR(60), indicator TEXT,
  procedure_no VARCHAR(60), procedure TEXT,
  date_range VARCHAR(120),
  follow_up TEXT,
  comments TEXT,
  evidence_type VARCHAR(120),
  evidence_source_employee VARCHAR(200),
  evidence_source_file VARCHAR(300),
  evaluation VARCHAR(200),
  evaluation_notes TEXT,
  status VARCHAR(40) NOT NULL DEFAULT 'In Progress',
  executor_committee_id UUID REFERENCES quality_committee(id) DEFERRABLE INITIALLY DEFERRED,
  evaluator_committee_id UUID REFERENCES quality_committee(id) DEFERRABLE INITIALLY DEFERRED,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  deleted_at TIMESTAMPTZ,
  row_version INT NOT NULL DEFAULT 1
);

-- ارتباطات متعددة المنفذين بعنصر الخطة (اختياري)
CREATE TABLE IF NOT EXISTS quality_opi_executor (
  id BIGSERIAL PRIMARY KEY,
  opi_id UUID NOT NULL REFERENCES quality_operational_plan_item(id) DEFERRABLE INITIALLY DEFERRED,
  executor_id UUID NOT NULL REFERENCES quality_plan_executor(id) DEFERRABLE INITIALLY DEFERRED,
  UNIQUE(opi_id, executor_id)
);

-- أدلة/بينات داعمة
CREATE TABLE IF NOT EXISTS quality_evidence (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  opi_id UUID REFERENCES quality_operational_plan_item(id) DEFERRABLE INITIALLY DEFERRED,
  kpi_code VARCHAR(60),
  evidence_type VARCHAR(120),
  link TEXT,
  notes TEXT,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  deleted_at TIMESTAMPTZ,
  row_version INT NOT NULL DEFAULT 1
);

-- خطة تحسين (Improvement Plan)
CREATE TABLE IF NOT EXISTS quality_improvement_plan (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  school_id UUID REFERENCES core_school(id) DEFERRABLE INITIALLY DEFERRED,
  year_id UUID REFERENCES core_year(id) DEFERRABLE INITIALLY DEFERRED,
  goal TEXT NOT NULL,
  actions TEXT NOT NULL,
  owner VARCHAR(150) NOT NULL,
  schedule TEXT,
  progress VARCHAR(120),
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  deleted_at TIMESTAMPTZ,
  row_version INT NOT NULL DEFAULT 1
);

-- لقطات مؤشرات أداء
CREATE TABLE IF NOT EXISTS quality_kpi_snapshot (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  kpi_code VARCHAR(60) NOT NULL,
  kpi_label VARCHAR(200) NOT NULL,
  snapshot_on DATE NOT NULL,
  value_numeric NUMERIC(12,4),
  value_text VARCHAR(200),
  school_id UUID REFERENCES core_school(id) DEFERRABLE INITIALLY DEFERRED,
  year_id   UUID REFERENCES core_year(id) DEFERRABLE INITIALLY DEFERRED,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  deleted_at TIMESTAMPTZ,
  row_version INT NOT NULL DEFAULT 1
);

CREATE TRIGGER tr_quality_committee_u  BEFORE UPDATE ON quality_committee  FOR EACH ROW EXECUTE FUNCTION set_updated_at();
CREATE TRIGGER tr_quality_executor_u   BEFORE UPDATE ON quality_plan_executor FOR EACH ROW EXECUTE FUNCTION set_updated_at();
CREATE TRIGGER tr_quality_opi_u        BEFORE UPDATE ON quality_operational_plan_item FOR EACH ROW EXECUTE FUNCTION set_updated_at();
CREATE TRIGGER tr_quality_evidence_u   BEFORE UPDATE ON quality_evidence   FOR EACH ROW EXECUTE FUNCTION set_updated_at();
CREATE TRIGGER tr_quality_improv_u     BEFORE UPDATE ON quality_improvement_plan FOR EACH ROW EXECUTE FUNCTION set_updated_at();
CREATE TRIGGER tr_quality_kpi_u        BEFORE UPDATE ON quality_kpi_snapshot FOR EACH ROW EXECUTE FUNCTION set_updated_at();

------------------------------------------------------------
-- 12) Assets & Safety
------------------------------------------------------------
CREATE TABLE IF NOT EXISTS assets_asset (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  school_id UUID REFERENCES core_school(id) DEFERRABLE INITIALLY DEFERRED,
  category VARCHAR(100) NOT NULL, -- furniture/lab/it/…
  model VARCHAR(150),
  serial_no VARCHAR(150),
  room_id UUID REFERENCES core_room(id) DEFERRABLE INITIALLY DEFERRED,
  notes TEXT,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  deleted_at TIMESTAMPTZ,
  row_version INT NOT NULL DEFAULT 1
);

CREATE TABLE IF NOT EXISTS assets_maintenance_ticket (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  asset_id UUID REFERENCES assets_asset(id) DEFERRABLE INITIALLY DEFERRED,
  type VARCHAR(20) NOT NULL CHECK (type IN ('preventive','corrective')),
  priority VARCHAR(20) NOT NULL DEFAULT 'normal',
  provider VARCHAR(150),
  opened_on DATE NOT NULL DEFAULT CURRENT_DATE,
  closed_on DATE,
  notes TEXT,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  deleted_at TIMESTAMPTZ,
  row_version INT NOT NULL DEFAULT 1
);

CREATE TABLE IF NOT EXISTS assets_safety_certificate (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  school_id UUID REFERENCES core_school(id) DEFERRABLE INITIALLY DEFERRED,
  room_id UUID REFERENCES core_room(id) DEFERRABLE INITIALLY DEFERRED,
  certificate_type VARCHAR(120) NOT NULL, -- Civil Defence/Lifts/Labs
  file_link TEXT,
  valid_until DATE,
  notes TEXT,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  deleted_at TIMESTAMPTZ,
  row_version INT NOT NULL DEFAULT 1
);

CREATE TRIGGER tr_asset_u         BEFORE UPDATE ON assets_asset               FOR EACH ROW EXECUTE FUNCTION set_updated_at();
CREATE TRIGGER tr_asset_mnt_u     BEFORE UPDATE ON assets_maintenance_ticket  FOR EACH ROW EXECUTE FUNCTION set_updated_at();
CREATE TRIGGER tr_asset_cert_u    BEFORE UPDATE ON assets_safety_certificate  FOR EACH ROW EXECUTE FUNCTION set_updated_at();

------------------------------------------------------------
-- 13) Communications
------------------------------------------------------------
CREATE TABLE IF NOT EXISTS comms_message_template (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  code VARCHAR(60) NOT NULL UNIQUE,
  channel VARCHAR(20) NOT NULL CHECK (channel IN ('email','sms','push')),
  subject VARCHAR(200),
  body TEXT NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  deleted_at TIMESTAMPTZ,
  row_version INT NOT NULL DEFAULT 1
);

CREATE TABLE IF NOT EXISTS comms_notice (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  school_id UUID REFERENCES core_school(id) DEFERRABLE INITIALLY DEFERRED,
  audience VARCHAR(60) NOT NULL,  -- staff / students / guardians / class:7A …
  title VARCHAR(200) NOT NULL,
  content TEXT NOT NULL,
  published_on TIMESTAMPTZ,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  deleted_at TIMESTAMPTZ,
  row_version INT NOT NULL DEFAULT 1
);

CREATE TABLE IF NOT EXISTS comms_announcement (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  school_id UUID REFERENCES core_school(id) DEFERRABLE INITIALLY DEFERRED,
  title VARCHAR(200) NOT NULL,
  content TEXT NOT NULL,
  start_on TIMESTAMPTZ,
  end_on   TIMESTAMPTZ,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  deleted_at TIMESTAMPTZ,
  row_version INT NOT NULL DEFAULT 1
);

CREATE TABLE IF NOT EXISTS comms_delivery_log (
  id BIGSERIAL PRIMARY KEY,
  template_id UUID REFERENCES comms_message_template(id) DEFERRABLE INITIALLY DEFERRED,
  channel VARCHAR(20) NOT NULL,
  recipient VARCHAR(254) NOT NULL,  -- email/phone/token
  status VARCHAR(20) NOT NULL DEFAULT 'pending',
  meta JSONB,
  sent_at TIMESTAMPTZ,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  deleted_at TIMESTAMPTZ,
  row_version INT NOT NULL DEFAULT 1
);

CREATE TRIGGER tr_comms_template_u   BEFORE UPDATE ON comms_message_template FOR EACH ROW EXECUTE FUNCTION set_updated_at();
CREATE TRIGGER tr_comms_notice_u     BEFORE UPDATE ON comms_notice           FOR EACH ROW EXECUTE FUNCTION set_updated_at();
CREATE TRIGGER tr_comms_announce_u   BEFORE UPDATE ON comms_announcement     FOR EACH ROW EXECUTE FUNCTION set_updated_at();
CREATE TRIGGER tr_comms_delivery_u   BEFORE UPDATE ON comms_delivery_log     FOR EACH ROW EXECUTE FUNCTION set_updated_at();

------------------------------------------------------------
-- 14) Audit & Outbox
------------------------------------------------------------
CREATE TABLE IF NOT EXISTS audit_log (
  id BIGSERIAL PRIMARY KEY,
  table_name TEXT NOT NULL,
  record_id UUID,
  actor_user_id INT,
  action VARCHAR(20) NOT NULL,     -- insert/update/delete
  old_values JSONB,
  new_values JSONB,
  ip INET,
  user_agent TEXT,
  ts TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS outbox_event (
  id BIGSERIAL PRIMARY KEY,
  event_type VARCHAR(120) NOT NULL,
  payload JSONB NOT NULL,
  status VARCHAR(20) NOT NULL DEFAULT 'pending',
  ts TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

------------------------------------------------------------
-- 15) Refdata (Lookups)
------------------------------------------------------------
CREATE TABLE IF NOT EXISTS refdata_lookup_nationality (
  code VARCHAR(5) PRIMARY KEY,
  name_ar VARCHAR(120) NOT NULL,
  name_en VARCHAR(120) NOT NULL
);

CREATE TABLE IF NOT EXISTS refdata_lookup_religion (
  code VARCHAR(5) PRIMARY KEY,
  name_ar VARCHAR(120) NOT NULL,
  name_en VARCHAR(120) NOT NULL
);

CREATE TABLE IF NOT EXISTS refdata_lookup_absence_reason (
  code VARCHAR(10) PRIMARY KEY,
  name_ar VARCHAR(120) NOT NULL
);

CREATE TABLE IF NOT EXISTS refdata_lookup_behavior_category (
  code VARCHAR(10) PRIMARY KEY,
  name_ar VARCHAR(120) NOT NULL
);

------------------------------------------------------------
-- (اختياري) 16) Seed أساسي للمرجعيات (SAFE ON CONFLICT)
------------------------------------------------------------

-- الدرجات 7..12
INSERT INTO core_grade(code, label_ar, label_en) VALUES
 (7,'الصف السابع','Grade 7'),
 (8,'الصف الثامن','Grade 8'),
 (9,'الصف التاسع','Grade 9'),
(10,'الصف العاشر','Grade 10'),
(11,'الصف الحادي عشر','Grade 11'),
(12,'الصف الثاني عشر','Grade 12')
ON CONFLICT (code) DO NOTHING;

-- أمثلة بسيطة على السلوك/الغياب (يمكنك تعديلها لاحقًا)
INSERT INTO refdata_lookup_behavior_category(code, name_ar) VALUES
('M1','سلوك إيجابي'), ('M2','سلوك يحتاج متابعة'), ('M3','مخالفة')
ON CONFLICT (code) DO NOTHING;

INSERT INTO refdata_lookup_absence_reason(code, name_ar) VALUES
('EXC','عذر مقبول'), ('ILL','مرض'), ('UNK','غير معروف')
ON CONFLICT (code) DO NOTHING;

-- (اختياري) مثال لجنة جودة افتراضية
INSERT INTO quality_committee(id, committee_type, member_name, job_title, role_in_committee, responsibility, domain)
VALUES (gen_random_uuid(), 'Operational', 'لجنة الخطة التشغيلية', 'فريق اللجنة', 'رئيس', 'متابعة تنفيذ الخطة التشغيلية', 'كل المجالات')
ON CONFLICT DO NOTHING;

------------------------------------------------------------
-- END OF FILE
------------------------------------------------------------