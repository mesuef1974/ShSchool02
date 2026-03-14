# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AcademicYear(models.Model):
    id = models.UUIDField(primary_key=True)
    code = models.CharField(unique=True, max_length=9)

    class Meta:
        managed = False
        db_table = 'academic_year'


class Appeal(models.Model):
    id = models.UUIDField(primary_key=True)
    enrollment = models.ForeignKey('Enrollment', models.DO_NOTHING)
    exam = models.ForeignKey('Exam', models.DO_NOTHING)
    reason = models.TextField()
    decision = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'appeal'
        unique_together = (('enrollment', 'exam'),)


class AttendanceRecord(models.Model):
    id = models.UUIDField(primary_key=True)
    enrollment = models.ForeignKey('Enrollment', models.DO_NOTHING)
    date = models.DateField()
    period = models.SmallIntegerField(blank=True, null=True)
    status = models.CharField(max_length=2)
    reason_code = models.CharField(max_length=32, blank=True, null=True)
    recorded_by = models.ForeignKey('AuthUser', models.DO_NOTHING, db_column='recorded_by', blank=True, null=True)
    recorded_at = models.DateTimeField()
    archived = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'attendance_record'
        unique_together = (('enrollment', 'date', 'period'),)


class AuditLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    actor = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    action = models.CharField(max_length=16)
    entity = models.CharField(max_length=64)
    entity_id = models.UUIDField(blank=True, null=True)
    ts = models.DateTimeField()
    meta = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'audit_log'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BehaviorCommittee(models.Model):
    id = models.UUIDField(primary_key=True)
    incident = models.OneToOneField('BehaviorIncident', models.DO_NOTHING)
    meeting_date = models.DateTimeField()
    decision = models.TextField()

    class Meta:
        managed = False
        db_table = 'behavior_committee'


class BehaviorIncident(models.Model):
    id = models.UUIDField(primary_key=True)
    student = models.ForeignKey('Student', models.DO_NOTHING)
    date = models.DateTimeField()
    offense_code = models.ForeignKey('OffenseCode', models.DO_NOTHING, db_column='offense_code')
    reporter = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    narrative = models.TextField(blank=True, null=True)
    evidence_ref = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'behavior_incident'


class BehaviorSanction(models.Model):
    id = models.UUIDField(primary_key=True)
    incident = models.ForeignKey(BehaviorIncident, models.DO_NOTHING)
    sanction_type = models.CharField(max_length=32)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'behavior_sanction'


class Bus(models.Model):
    id = models.UUIDField(primary_key=True)
    plate = models.CharField(unique=True, max_length=16)
    capacity = models.SmallIntegerField(blank=True, null=True)
    gps_enabled = models.BooleanField(blank=True, null=True)
    cctv_enabled = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bus'


class ClassRoom(models.Model):
    id = models.UUIDField(primary_key=True)
    school = models.ForeignKey('School', models.DO_NOTHING)
    year = models.ForeignKey(AcademicYear, models.DO_NOTHING)
    grade = models.CharField(max_length=16)
    section = models.CharField(max_length=8)
    capacity = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'class_room'
        unique_together = (('school', 'year', 'grade', 'section'),)


class ClinicVisit(models.Model):
    id = models.UUIDField(primary_key=True)
    student = models.ForeignKey('Student', models.DO_NOTHING)
    visited_at = models.DateTimeField()
    complaint_enc = models.BinaryField(blank=True, null=True)
    vitals = models.JSONField(blank=True, null=True)
    diagnosis_enc = models.BinaryField(blank=True, null=True)
    action_taken_enc = models.BinaryField(blank=True, null=True)
    attended_by = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='attended_by', blank=True, null=True)
    retention_until = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clinic_visit'


class DelayLog(models.Model):
    id = models.UUIDField(primary_key=True)
    route = models.ForeignKey('Route', models.DO_NOTHING)
    date = models.DateField()
    arrival_time = models.TimeField(blank=True, null=True)
    delay_minutes = models.SmallIntegerField(blank=True, null=True)
    reason = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'delay_log'


class DisciplinaryAction(models.Model):
    id = models.UUIDField(primary_key=True)
    staff = models.ForeignKey('Staff', models.DO_NOTHING)
    article_ref = models.CharField(max_length=64, blank=True, null=True)
    penalty = models.CharField(max_length=64, blank=True, null=True)
    decision_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'disciplinary_action'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Enrollment(models.Model):
    id = models.UUIDField(primary_key=True)
    student = models.ForeignKey('Student', models.DO_NOTHING)
    school = models.ForeignKey('School', models.DO_NOTHING)
    year = models.ForeignKey(AcademicYear, models.DO_NOTHING)
    grade = models.CharField(max_length=16)
    section = models.CharField(max_length=8, blank=True, null=True)
    valid_from = models.DateField()
    valid_to = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enrollment'
        unique_together = (('student', 'school', 'year', 'grade', 'section'),)


class Exam(models.Model):
    id = models.UUIDField(primary_key=True)
    subject = models.ForeignKey('Subject', models.DO_NOTHING)
    grade = models.CharField(max_length=16)
    term = models.ForeignKey('Term', models.DO_NOTHING)
    is_makeup = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'exam'


class ExamResult(models.Model):
    id = models.UUIDField(primary_key=True)
    enrollment = models.ForeignKey(Enrollment, models.DO_NOTHING)
    exam = models.ForeignKey(Exam, models.DO_NOTHING)
    score = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'exam_result'
        unique_together = (('enrollment', 'exam'),)


class ExamSession(models.Model):
    id = models.UUIDField(primary_key=True)
    exam = models.ForeignKey(Exam, models.DO_NOTHING)
    session_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'exam_session'


class Guardian(models.Model):
    id = models.UUIDField(primary_key=True)
    full_name_ar = models.CharField(max_length=128)
    phone = models.CharField(max_length=32)
    relation = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guardian'


class ImprovementPlan(models.Model):
    id = models.UUIDField(primary_key=True)
    weak_points = models.TextField()
    actions = models.TextField()
    owner = models.CharField(max_length=128, blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'improvement_plan'


class LeaveRequest(models.Model):
    id = models.UUIDField(primary_key=True)
    staff = models.ForeignKey('Staff', models.DO_NOTHING)
    leave_type = models.CharField(max_length=24)
    date_from = models.DateField()
    date_to = models.DateField()
    balance_before = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'leave_request'


class LibraryCopy(models.Model):
    id = models.UUIDField(primary_key=True)
    title = models.ForeignKey('LibraryTitle', models.DO_NOTHING)
    copy_code = models.CharField(unique=True, max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'library_copy'


class LibraryLoan(models.Model):
    id = models.UUIDField(primary_key=True)
    copy = models.ForeignKey(LibraryCopy, models.DO_NOTHING)
    borrower_id = models.UUIDField()
    loan_date = models.DateField()
    due_date = models.DateField()
    return_date = models.DateField(blank=True, null=True)
    fine_amount = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'library_loan'


class LibraryTitle(models.Model):
    id = models.UUIDField(primary_key=True)
    isbn = models.CharField(max_length=32, blank=True, null=True)
    title_ar = models.CharField(max_length=256)
    author_ar = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'library_title'


class MedicationLog(models.Model):
    id = models.UUIDField(primary_key=True)
    clinic_visit = models.ForeignKey(ClinicVisit, models.DO_NOTHING)
    med_name_enc = models.BinaryField()
    dose = models.CharField(max_length=32, blank=True, null=True)
    administered_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'medication_log'


class Notice(models.Model):
    id = models.UUIDField(primary_key=True)
    student = models.ForeignKey('Student', models.DO_NOTHING)
    notice_type = models.CharField(max_length=32)
    channel = models.CharField(max_length=32)
    sent_at = models.DateTimeField()
    payload = models.JSONField(blank=True, null=True)
    template = models.ForeignKey('NoticeTemplate', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notice'


class NoticeTemplate(models.Model):
    id = models.UUIDField(primary_key=True)
    code = models.CharField(unique=True, max_length=32)
    channel = models.CharField(max_length=16)
    subject = models.CharField(max_length=128, blank=True, null=True)
    body = models.TextField()

    class Meta:
        managed = False
        db_table = 'notice_template'


class OffenseCode(models.Model):
    code = models.CharField(primary_key=True, max_length=16)
    severity = models.CharField(max_length=6)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'offense_code'


class PerformanceReview(models.Model):
    id = models.UUIDField(primary_key=True)
    staff = models.ForeignKey('Staff', models.DO_NOTHING)
    kpi_scores = models.JSONField()
    overall = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'performance_review'


class QualityEvidence(models.Model):
    id = models.UUIDField(primary_key=True)
    indicator = models.ForeignKey('QualityIndicator', models.DO_NOTHING)
    file_ref = models.CharField(max_length=256)
    collected_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'quality_evidence'


class QualityIndicator(models.Model):
    id = models.UUIDField(primary_key=True)
    standard_code = models.ForeignKey('QualityStandard', models.DO_NOTHING, db_column='standard_code')
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'quality_indicator'


class QualityStandard(models.Model):
    code = models.CharField(primary_key=True, max_length=16)
    title = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'quality_standard'


class Reservation(models.Model):
    id = models.UUIDField(primary_key=True)
    title = models.ForeignKey(LibraryTitle, models.DO_NOTHING)
    requester_id = models.UUIDField()
    reserved_at = models.DateTimeField()
    fulfilled = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reservation'


class RideLog(models.Model):
    id = models.UUIDField(primary_key=True)
    route = models.ForeignKey('Route', models.DO_NOTHING)
    date = models.DateField()
    boarded = models.SmallIntegerField(blank=True, null=True)
    safety_check_pre = models.BooleanField(blank=True, null=True)
    safety_check_post = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ride_log'
        unique_together = (('route', 'date'),)


class Room(models.Model):
    id = models.UUIDField(primary_key=True)
    school = models.ForeignKey('School', models.DO_NOTHING)
    name = models.CharField(max_length=64)
    capacity = models.SmallIntegerField(blank=True, null=True)
    room_type = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'room'


class Route(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=64)
    bus = models.ForeignKey(Bus, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'route'


class RouteStop(models.Model):
    id = models.UUIDField(primary_key=True)
    route = models.ForeignKey(Route, models.DO_NOTHING)
    seq = models.SmallIntegerField()
    location = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'route_stop'
        unique_together = (('route', 'seq'),)


class School(models.Model):
    id = models.UUIDField(primary_key=True)
    name_ar = models.CharField(max_length=256)
    moe_code = models.CharField(unique=True, max_length=32, blank=True, null=True)
    level = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'school'


class Staff(models.Model):
    id = models.UUIDField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    job_title = models.CharField(max_length=128, blank=True, null=True)
    hire_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staff'


class StaffAttendance(models.Model):
    id = models.UUIDField(primary_key=True)
    staff = models.ForeignKey(Staff, models.DO_NOTHING)
    date = models.DateField()
    check_in = models.DateTimeField(blank=True, null=True)
    check_out = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'staff_attendance'
        unique_together = (('staff', 'date'),)


class Student(models.Model):
    id = models.UUIDField(primary_key=True)
    national_id = models.CharField(unique=True, max_length=32)
    first_name_ar = models.CharField(max_length=64)
    last_name_ar = models.CharField(max_length=64)
    dob = models.DateField()
    nationality = models.CharField(max_length=64, blank=True, null=True)
    guardian = models.ForeignKey(Guardian, models.DO_NOTHING, blank=True, null=True)
    pdppl_guardian_consent = models.BooleanField(blank=True, null=True)
    consent_ts = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student'


class StudentRider(models.Model):
    id = models.UUIDField(primary_key=True)
    student = models.ForeignKey(Student, models.DO_NOTHING)
    route = models.ForeignKey(Route, models.DO_NOTHING)
    stop = models.ForeignKey(RouteStop, models.DO_NOTHING, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student_rider'
        unique_together = (('student', 'route'),)


class Subject(models.Model):
    id = models.UUIDField(primary_key=True)
    code = models.CharField(unique=True, max_length=32)
    name_ar = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'subject'


class Teacher(models.Model):
    id = models.UUIDField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    staff_code = models.CharField(unique=True, max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teacher'


class TeachingAssignment(models.Model):
    id = models.UUIDField(primary_key=True)
    teacher = models.ForeignKey(Teacher, models.DO_NOTHING)
    class_field = models.ForeignKey(ClassRoom, models.DO_NOTHING, db_column='class_id')  # Field renamed because it was a Python reserved word.
    subject = models.ForeignKey(Subject, models.DO_NOTHING)
    weekly_load = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teaching_assignment'
        unique_together = (('teacher', 'class_field', 'subject'),)


class Term(models.Model):
    id = models.UUIDField(primary_key=True)
    year = models.ForeignKey(AcademicYear, models.DO_NOTHING)
    code = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'term'
        unique_together = (('year', 'code'),)


class TimetableRule(models.Model):
    id = models.UUIDField(primary_key=True)
    school = models.ForeignKey(School, models.DO_NOTHING)
    year = models.ForeignKey(AcademicYear, models.DO_NOTHING)
    json_rule = models.JSONField()

    class Meta:
        managed = False
        db_table = 'timetable_rule'


class TimetableSlot(models.Model):
    id = models.UUIDField(primary_key=True)
    class_field = models.ForeignKey(ClassRoom, models.DO_NOTHING, db_column='class_id')  # Field renamed because it was a Python reserved word.
    day_of_week = models.SmallIntegerField()
    period = models.SmallIntegerField()
    subject = models.ForeignKey(Subject, models.DO_NOTHING)
    teacher = models.ForeignKey(Teacher, models.DO_NOTHING)
    room = models.ForeignKey(Room, models.DO_NOTHING, blank=True, null=True)
    is_fixed = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'timetable_slot'
        unique_together = (('class_field', 'day_of_week', 'period'),)


class Visit(models.Model):
    id = models.UUIDField(primary_key=True)
    visit_date = models.DateField()
    team_members = models.TextField()
    notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'visit'
