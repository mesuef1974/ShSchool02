
-- جدول auth_user مبسّط (متوافق اسميًا مع مراجع FK في v1)

-- مستخدم مبدئي اختياري لتجارب الإدخال السريع


-- ============================================================================
-- Shahania Smart School – Unified PostgreSQL DDL (v1.0)
-- Generated: 2026-03-12 21:44:07 UTC
-- Notes:
--   * UUID primary keys everywhere (uuid-ossp).
--   * FKs to Django default auth_user where applicable (do not recreate auth tables).
--   * Sensitive (health) fields are stored as BYTEA for app-layer encryption.
--   * Core constraints & indexes added; JSONB fields indexed via GIN where useful.
--   * RLS policies are provided as commented stubs for later activation.
--   * All timestamps are assumed UTC; the app handles time zone display.
-- ============================================================================

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

SET search_path TO public;

-- ============================
-- 0) Utility ENUMs (optional)
-- ============================
-- none for now; we use CHECK constraints on small enumerations.

-- ============================
-- 1) Schools / Academic Structure
-- ============================
CREATE TABLE IF NOT EXISTS school (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name_ar VARCHAR(256) NOT NULL,
    moe_code VARCHAR(32) UNIQUE,
    level VARCHAR(32) -- preparatory/secondary
);

CREATE TABLE IF NOT EXISTS academic_year (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    code VARCHAR(9) UNIQUE NOT NULL -- e.g., 2025-2026
);

CREATE TABLE IF NOT EXISTS term (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    year_id UUID NOT NULL REFERENCES academic_year(id) ON DELETE CASCADE,
    code VARCHAR(8) NOT NULL,
    UNIQUE(year_id, code)
);

-- ============================
-- 2) Students / Guardians / Enrollments
-- ============================
CREATE TABLE IF NOT EXISTS guardian (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    full_name_ar VARCHAR(128) NOT NULL,
    phone VARCHAR(32) NOT NULL,
    relation VARCHAR(32)
);

CREATE TABLE IF NOT EXISTS student (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    national_id VARCHAR(32) UNIQUE NOT NULL,
    first_name_ar VARCHAR(64) NOT NULL,
    last_name_ar VARCHAR(64) NOT NULL,
    dob DATE NOT NULL,
    nationality VARCHAR(64),
    guardian_id UUID REFERENCES guardian(id),
    pdppl_guardian_consent BOOLEAN DEFAULT FALSE,
    consent_ts TIMESTAMP
);

CREATE TABLE IF NOT EXISTS enrollment (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    student_id UUID NOT NULL REFERENCES student(id) ON DELETE CASCADE,
    school_id UUID NOT NULL REFERENCES school(id) ON DELETE CASCADE,
    year_id UUID NOT NULL REFERENCES academic_year(id) ON DELETE CASCADE,
    grade VARCHAR(16) NOT NULL,
    section VARCHAR(8),
    valid_from DATE NOT NULL,
    valid_to DATE,
    UNIQUE(student_id, school_id, year_id, grade, section)
);
CREATE INDEX IF NOT EXISTS idx_enrollment_year_grade_section ON enrollment(year_id, grade, section);

-- ============================
-- 3) Academics (Subjects / Classes / Teachers / Assignments)
-- ============================
CREATE TABLE IF NOT EXISTS subject (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    code VARCHAR(32) UNIQUE NOT NULL,
    name_ar VARCHAR(128) NOT NULL
);

CREATE TABLE IF NOT EXISTS class_room (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    school_id UUID NOT NULL REFERENCES school(id) ON DELETE CASCADE,
    year_id UUID NOT NULL REFERENCES academic_year(id) ON DELETE CASCADE,
    grade VARCHAR(16) NOT NULL,
    section VARCHAR(8) NOT NULL,
    capacity SMALLINT,
    UNIQUE(school_id, year_id, grade, section)
);
CREATE INDEX IF NOT EXISTS idx_class_room_year_grade_section ON class_room(year_id, grade, section);

CREATE TABLE IF NOT EXISTS teacher (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id INTEGER NOT NULL REFERENCES auth_user(id) ON DELETE CASCADE,
    staff_code VARCHAR(32) UNIQUE
);

CREATE TABLE IF NOT EXISTS teaching_assignment (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    teacher_id UUID NOT NULL REFERENCES teacher(id) ON DELETE CASCADE,
    class_id UUID NOT NULL REFERENCES class_room(id) ON DELETE CASCADE,
    subject_id UUID NOT NULL REFERENCES subject(id) ON DELETE CASCADE,
    weekly_load SMALLINT,
    UNIQUE(teacher_id, class_id, subject_id)
);

-- ============================
-- 4) Attendance
-- ============================
CREATE TABLE IF NOT EXISTS attendance_record (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    enrollment_id UUID NOT NULL REFERENCES enrollment(id) ON DELETE CASCADE,
    date DATE NOT NULL,
    period SMALLINT,
    status VARCHAR(2) NOT NULL CHECK (status IN ('P','A','E','L','ED')),
    reason_code VARCHAR(32),
    recorded_by INTEGER REFERENCES auth_user(id),
    recorded_at TIMESTAMP NOT NULL DEFAULT NOW(),
    archived BOOLEAN NOT NULL DEFAULT FALSE,
    UNIQUE(enrollment_id, date, period)
);
CREATE INDEX IF NOT EXISTS idx_attendance_date ON attendance_record(date);

-- ============================
-- 5) Behavior (Incidents / Committee / Sanctions)
-- ============================
CREATE TABLE IF NOT EXISTS offense_code (
    code VARCHAR(16) PRIMARY KEY,
    severity VARCHAR(6) NOT NULL CHECK (severity IN ('MINOR','MOD','MAJOR')),
    description TEXT
);

CREATE TABLE IF NOT EXISTS behavior_incident (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    student_id UUID NOT NULL REFERENCES student(id) ON DELETE CASCADE,
    date TIMESTAMP NOT NULL DEFAULT NOW(),
    offense_code VARCHAR(16) NOT NULL REFERENCES offense_code(code),
    reporter_id INTEGER REFERENCES auth_user(id),
    narrative TEXT,
    evidence_ref VARCHAR(256)
);
CREATE INDEX IF NOT EXISTS idx_behavior_student ON behavior_incident(student_id);

CREATE TABLE IF NOT EXISTS behavior_committee (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    incident_id UUID UNIQUE NOT NULL REFERENCES behavior_incident(id) ON DELETE CASCADE,
    meeting_date TIMESTAMP NOT NULL,
    decision TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS behavior_sanction (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    incident_id UUID NOT NULL REFERENCES behavior_incident(id) ON DELETE CASCADE,
    sanction_type VARCHAR(32) NOT NULL,
    start_date DATE,
    end_date DATE
);

-- ============================
-- 6) Assessments (Exams / Sessions / Results / Appeals)
-- ============================
CREATE TABLE IF NOT EXISTS exam (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    subject_id UUID NOT NULL REFERENCES subject(id) ON DELETE CASCADE,
    grade VARCHAR(16) NOT NULL,
    term_id UUID NOT NULL REFERENCES term(id) ON DELETE CASCADE,
    is_makeup BOOLEAN DEFAULT FALSE
);

CREATE TABLE IF NOT EXISTS exam_session (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    exam_id UUID NOT NULL REFERENCES exam(id) ON DELETE CASCADE,
    session_date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL
);

CREATE TABLE IF NOT EXISTS exam_result (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    enrollment_id UUID NOT NULL REFERENCES enrollment(id) ON DELETE CASCADE,
    exam_id UUID NOT NULL REFERENCES exam(id) ON DELETE CASCADE,
    score NUMERIC(5,2),
    UNIQUE(enrollment_id, exam_id)
);

CREATE TABLE IF NOT EXISTS appeal (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    enrollment_id UUID NOT NULL REFERENCES enrollment(id) ON DELETE CASCADE,
    exam_id UUID NOT NULL REFERENCES exam(id) ON DELETE CASCADE,
    reason TEXT NOT NULL,
    decision TEXT,
    UNIQUE(enrollment_id, exam_id)
);

-- ============================
-- 7) Health (Sensitive; encrypted at app layer)
-- ============================
CREATE TABLE IF NOT EXISTS clinic_visit (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    student_id UUID NOT NULL REFERENCES student(id) ON DELETE CASCADE,
    visited_at TIMESTAMP NOT NULL DEFAULT NOW(),
    complaint_enc BYTEA,
    vitals JSONB,
    diagnosis_enc BYTEA,
    action_taken_enc BYTEA,
    attended_by INTEGER REFERENCES auth_user(id),
    retention_until DATE
);
CREATE INDEX IF NOT EXISTS idx_clinic_visit_student ON clinic_visit(student_id);

CREATE TABLE IF NOT EXISTS medication_log (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    clinic_visit_id UUID NOT NULL REFERENCES clinic_visit(id) ON DELETE CASCADE,
    med_name_enc BYTEA NOT NULL,
    dose VARCHAR(32),
    administered_at TIMESTAMP NOT NULL DEFAULT NOW()
);

-- ============================
-- 8) Transport (Bus / Routes)
-- ============================
CREATE TABLE IF NOT EXISTS bus (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    plate VARCHAR(16) UNIQUE NOT NULL,
    capacity SMALLINT,
    gps_enabled BOOLEAN DEFAULT TRUE,
    cctv_enabled BOOLEAN DEFAULT TRUE
);

CREATE TABLE IF NOT EXISTS route (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(64) NOT NULL,
    bus_id UUID NOT NULL REFERENCES bus(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS route_stop (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    route_id UUID NOT NULL REFERENCES route(id) ON DELETE CASCADE,
    seq SMALLINT NOT NULL,
    location VARCHAR(256),
    UNIQUE(route_id, seq)
);

CREATE TABLE IF NOT EXISTS student_rider (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    student_id UUID NOT NULL REFERENCES student(id) ON DELETE CASCADE,
    route_id UUID NOT NULL REFERENCES route(id) ON DELETE CASCADE,
    stop_id UUID REFERENCES route_stop(id),
    active BOOLEAN DEFAULT TRUE,
    UNIQUE(student_id, route_id)
);

CREATE TABLE IF NOT EXISTS ride_log (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    route_id UUID NOT NULL REFERENCES route(id) ON DELETE CASCADE,
    date DATE NOT NULL,
    boarded SMALLINT DEFAULT 0,
    safety_check_pre BOOLEAN DEFAULT FALSE,
    safety_check_post BOOLEAN DEFAULT FALSE,
    UNIQUE(route_id, date)
);
CREATE INDEX IF NOT EXISTS idx_ride_log_date ON ride_log(date);

CREATE TABLE IF NOT EXISTS delay_log (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    route_id UUID NOT NULL REFERENCES route(id) ON DELETE CASCADE,
    date DATE NOT NULL,
    arrival_time TIME,
    delay_minutes SMALLINT DEFAULT 0,
    reason VARCHAR(128)
);

-- ============================
-- 9) Library (Titles / Copies / Loans / Reservations)
-- ============================
CREATE TABLE IF NOT EXISTS library_title (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    isbn VARCHAR(32),
    title_ar VARCHAR(256) NOT NULL,
    author_ar VARCHAR(256)
);

CREATE TABLE IF NOT EXISTS library_copy (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    title_id UUID NOT NULL REFERENCES library_title(id) ON DELETE CASCADE,
    copy_code VARCHAR(64) UNIQUE
);

CREATE TABLE IF NOT EXISTS library_loan (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    copy_id UUID NOT NULL REFERENCES library_copy(id) ON DELETE CASCADE,
    borrower_id UUID NOT NULL,
    loan_date DATE NOT NULL,
    due_date DATE NOT NULL,
    return_date DATE,
    fine_amount NUMERIC(6,2)
);

CREATE TABLE IF NOT EXISTS reservation (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    title_id UUID NOT NULL REFERENCES library_title(id) ON DELETE CASCADE,
    requester_id UUID NOT NULL,
    reserved_at TIMESTAMP NOT NULL DEFAULT NOW(),
    fulfilled BOOLEAN DEFAULT FALSE
);

-- ============================
-- 10) Quality / QNSA
-- ============================
CREATE TABLE IF NOT EXISTS quality_standard (
    code VARCHAR(16) PRIMARY KEY,
    title VARCHAR(128) NOT NULL
);

CREATE TABLE IF NOT EXISTS quality_indicator (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    standard_code VARCHAR(16) NOT NULL REFERENCES quality_standard(code) ON DELETE CASCADE,
    description TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS quality_evidence (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    indicator_id UUID NOT NULL REFERENCES quality_indicator(id) ON DELETE CASCADE,
    file_ref VARCHAR(256) NOT NULL,
    collected_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS visit (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    visit_date DATE NOT NULL,
    team_members TEXT NOT NULL,
    notes TEXT
);

CREATE TABLE IF NOT EXISTS improvement_plan (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    weak_points TEXT NOT NULL,
    actions TEXT NOT NULL,
    owner VARCHAR(128),
    due_date DATE
);

-- ============================
-- 11) HR (Staff / Attendance / Leave / Disciplinary / Performance)
-- ============================
CREATE TABLE IF NOT EXISTS staff (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id INTEGER NOT NULL REFERENCES auth_user(id) ON DELETE CASCADE,
    job_title VARCHAR(128),
    hire_date DATE
);

CREATE TABLE IF NOT EXISTS staff_attendance (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    staff_id UUID NOT NULL REFERENCES staff(id) ON DELETE CASCADE,
    date DATE NOT NULL,
    check_in TIMESTAMP,
    check_out TIMESTAMP,
    status VARCHAR(16) NOT NULL CHECK (status IN ('present','absent','leave')),
    UNIQUE(staff_id, date)
);
CREATE INDEX IF NOT EXISTS idx_staff_att_date ON staff_attendance(date);

CREATE TABLE IF NOT EXISTS leave_request (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    staff_id UUID NOT NULL REFERENCES staff(id) ON DELETE CASCADE,
    leave_type VARCHAR(24) NOT NULL,
    date_from DATE NOT NULL,
    date_to DATE NOT NULL,
    balance_before NUMERIC(5,2),
    status VARCHAR(16) DEFAULT 'pending'
);

CREATE TABLE IF NOT EXISTS disciplinary_action (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    staff_id UUID NOT NULL REFERENCES staff(id) ON DELETE CASCADE,
    article_ref VARCHAR(64),
    penalty VARCHAR(64),
    decision_date DATE DEFAULT CURRENT_DATE
);

CREATE TABLE IF NOT EXISTS performance_review (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    staff_id UUID NOT NULL REFERENCES staff(id) ON DELETE CASCADE,
    kpi_scores JSONB NOT NULL,
    overall NUMERIC(4,2)
);
CREATE INDEX IF NOT EXISTS idx_performance_kpi_gin ON performance_review USING GIN (kpi_scores);

-- ============================
-- 12) Timetable (Rooms / Rules / Slots)
-- ============================
CREATE TABLE IF NOT EXISTS room (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    school_id UUID NOT NULL REFERENCES school(id) ON DELETE CASCADE,
    name VARCHAR(64) NOT NULL,
    capacity SMALLINT,
    room_type VARCHAR(32)
);

CREATE TABLE IF NOT EXISTS timetable_rule (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    school_id UUID NOT NULL REFERENCES school(id) ON DELETE CASCADE,
    year_id UUID NOT NULL REFERENCES academic_year(id) ON DELETE CASCADE,
    json_rule JSONB NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_timetable_rule_gin ON timetable_rule USING GIN (json_rule);

CREATE TABLE IF NOT EXISTS timetable_slot (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    class_id UUID NOT NULL REFERENCES class_room(id) ON DELETE CASCADE,
    day_of_week SMALLINT NOT NULL CHECK (day_of_week BETWEEN 1 AND 7),
    period SMALLINT NOT NULL,
    subject_id UUID NOT NULL REFERENCES subject(id) ON DELETE CASCADE,
    teacher_id UUID NOT NULL REFERENCES teacher(id) ON DELETE CASCADE,
    room_id UUID REFERENCES room(id),
    is_fixed BOOLEAN DEFAULT FALSE,
    UNIQUE(class_id, day_of_week, period)
);
CREATE INDEX IF NOT EXISTS idx_timetable_day_period ON timetable_slot(day_of_week, period);

-- ============================
-- 13) Notifications / Templates
-- ============================
CREATE TABLE IF NOT EXISTS notice_template (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    code VARCHAR(32) UNIQUE NOT NULL,
    channel VARCHAR(16) NOT NULL, -- SMS/Email/Letter
    subject VARCHAR(128),
    body TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS notice (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    student_id UUID NOT NULL REFERENCES student(id) ON DELETE CASCADE,
    notice_type VARCHAR(32) NOT NULL,
    channel VARCHAR(32) NOT NULL,
    sent_at TIMESTAMP NOT NULL DEFAULT NOW(),
    payload JSONB,
    template_id UUID REFERENCES notice_template(id)
);
CREATE INDEX IF NOT EXISTS idx_notice_student ON notice(student_id);

-- ============================
-- 14) Audit Log
-- ============================
CREATE TABLE IF NOT EXISTS audit_log (
    id BIGSERIAL PRIMARY KEY,
    actor_id INTEGER REFERENCES auth_user(id),
    action VARCHAR(16) NOT NULL, -- read/write/delete
    entity VARCHAR(64) NOT NULL,
    entity_id UUID,
    ts TIMESTAMP NOT NULL DEFAULT NOW(),
    meta JSONB
);
CREATE INDEX IF NOT EXISTS idx_audit_entity ON audit_log(entity, entity_id, ts);

-- ============================
-- 15) Suggested RLS (commented) – enable after app wiring
-- ============================
-- Example: protect health data rows per user groups (set via app GUC)
-- ALTER TABLE clinic_visit ENABLE ROW LEVEL SECURITY;
-- CREATE POLICY clinic_visit_nurse_policy
--   ON clinic_visit FOR SELECT
--   USING (
--     current_setting('app.current_groups', true) LIKE '%ClinicNurse%'
--     OR current_setting('app.current_groups', true) LIKE '%SchoolManager%'
--   );

-- ============================
-- End of DDL
-- ============================
