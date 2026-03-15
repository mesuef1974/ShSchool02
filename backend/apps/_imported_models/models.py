# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AssessmentAppeal(models.Model):
    id = models.UUIDField(primary_key=True)
    reason = models.TextField()
    decision = models.TextField()
    enrollment = models.ForeignKey('PeopleEnrollment', models.DO_NOTHING)
    exam = models.ForeignKey('AssessmentExam', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'assessment_appeal'
        unique_together = (('enrollment', 'exam'),)


class AssessmentExam(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=150)
    term_code = models.CharField(max_length=10)
    subject = models.ForeignKey('CoreSubject', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'assessment_exam'


class AssessmentExamresult(models.Model):
    id = models.UUIDField(primary_key=True)
    score = models.DecimalField(max_digits=6, decimal_places=2)
    enrollment = models.ForeignKey('PeopleEnrollment', models.DO_NOTHING)
    exam = models.ForeignKey(AssessmentExam, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'assessment_examresult'
        unique_together = (('enrollment', 'exam'),)


class AssessmentExamsession(models.Model):
    id = models.UUIDField(primary_key=True)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    exam = models.ForeignKey(AssessmentExam, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'assessment_examsession'


class AssetsAsset(models.Model):
    id = models.UUIDField(primary_key=True)
    school = models.ForeignKey('CoreSchool', models.DO_NOTHING, blank=True, null=True)
    category = models.CharField(max_length=100)
    model = models.CharField(max_length=150, blank=True, null=True)
    serial_no = models.CharField(max_length=150, blank=True, null=True)
    room = models.ForeignKey('CoreRoom', models.DO_NOTHING, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    row_version = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'assets_asset'


class AssetsMaintenanceTicket(models.Model):
    id = models.UUIDField(primary_key=True)
    asset = models.ForeignKey(AssetsAsset, models.DO_NOTHING, blank=True, null=True)
    type = models.CharField(max_length=20)
    priority = models.CharField(max_length=20)
    provider = models.CharField(max_length=150, blank=True, null=True)
    opened_on = models.DateField()
    closed_on = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    row_version = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'assets_maintenance_ticket'


class AssetsSafetyCertificate(models.Model):
    id = models.UUIDField(primary_key=True)
    school = models.ForeignKey('CoreSchool', models.DO_NOTHING, blank=True, null=True)
    room = models.ForeignKey('CoreRoom', models.DO_NOTHING, blank=True, null=True)
    certificate_type = models.CharField(max_length=120)
    file_link = models.TextField(blank=True, null=True)
    valid_until = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    row_version = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'assets_safety_certificate'


class AttendanceAttendancerecord(models.Model):
    id = models.UUIDField(primary_key=True)
    date = models.DateField()
    period = models.SmallIntegerField()
    status = models.CharField(max_length=10)
    note = models.TextField()
    enrollment = models.ForeignKey('PeopleEnrollment', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'attendance_attendancerecord'
        unique_together = (('enrollment', 'date', 'period'),)


class AuditLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    table_name = models.TextField()
    record_id = models.UUIDField(blank=True, null=True)
    actor_user_id = models.IntegerField(blank=True, null=True)
    action = models.CharField(max_length=20)
    old_values = models.JSONField(blank=True, null=True)
    new_values = models.JSONField(blank=True, null=True)
    ip = models.GenericIPAddressField(blank=True, null=True)
    user_agent = models.TextField(blank=True, null=True)
    ts = models.DateTimeField()

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


class BehaviorBehaviorincident(models.Model):
    id = models.UUIDField(primary_key=True)
    date = models.DateField()
    period = models.SmallIntegerField(blank=True, null=True)
    place = models.CharField(max_length=120)
    category = models.CharField(max_length=80)
    description = models.TextField(db_comment='SENSITIVE:Behavior')
    student = models.ForeignKey('PeopleStudent', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'behavior_behaviorincident'


class BehaviorCommittee(models.Model):
    id = models.UUIDField(primary_key=True)
    incident = models.OneToOneField(BehaviorBehaviorincident, models.DO_NOTHING)
    meeting_date = models.DateField()
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    row_version = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'behavior_committee'


class BehaviorSanction(models.Model):
    id = models.UUIDField(primary_key=True)
    incident = models.ForeignKey(BehaviorBehaviorincident, models.DO_NOTHING)
    sanction_type = models.CharField(max_length=80)
    level = models.SmallIntegerField()
    decided_on = models.DateField()
    executed = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    row_version = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'behavior_sanction'


class CommsAnnouncement(models.Model):
    id = models.UUIDField(primary_key=True)
    school = models.ForeignKey('CoreSchool', models.DO_NOTHING, blank=True, null=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    start_on = models.DateTimeField(blank=True, null=True)
    end_on = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    row_version = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'comms_announcement'


class CommsDeliveryLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    template = models.ForeignKey('CommsMessageTemplate', models.DO_NOTHING, blank=True, null=True)
    channel = models.CharField(max_length=20)
    recipient = models.CharField(max_length=254)
    status = models.CharField(max_length=20)
    meta = models.JSONField(blank=True, null=True)
    sent_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    row_version = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'comms_delivery_log'


class CommsMessageTemplate(models.Model):
    id = models.UUIDField(primary_key=True)
    code = models.CharField(unique=True, max_length=60)
    channel = models.CharField(max_length=20)
    subject = models.CharField(max_length=200, blank=True, null=True)
    body = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    row_version = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'comms_message_template'


class CommsNotice(models.Model):
    id = models.UUIDField(primary_key=True)
    school = models.ForeignKey('CoreSchool', models.DO_NOTHING, blank=True, null=True)
    audience = models.CharField(max_length=60)
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_on = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    row_version = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'comms_notice'


class CoreClassroom(models.Model):
    id = models.UUIDField(primary_key=True)
    grade = models.SmallIntegerField()
    section = models.CharField(max_length=10)
    school = models.ForeignKey('CoreSchool', models.DO_NOTHING)
    year = models.ForeignKey('CoreYear', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'core_classroom'
        unique_together = (('school', 'year', 'grade', 'section'),)


class CoreGrade(models.Model):
    code = models.SmallIntegerField(primary_key=True)
    label_ar = models.CharField(max_length=50)
    label_en = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'core_grade'


class CoreRoom(models.Model):
    id = models.UUIDField(primary_key=True)
    code = models.CharField(unique=True, max_length=50)
    room_type = models.CharField(max_length=50)
    capacity = models.IntegerField()
    school = models.ForeignKey('CoreSchool', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'core_room'


class CoreSchool(models.Model):
    id = models.UUIDField(primary_key=True)
    name_ar = models.CharField(max_length=200)
    name_en = models.CharField(max_length=200)
    moehe_code = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'core_school'


class CoreSubject(models.Model):
    id = models.UUIDField(primary_key=True)
    name_ar = models.CharField(max_length=200)
    name_en = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'core_subject'


class CoreTerm(models.Model):
    id = models.UUIDField(primary_key=True)
    code = models.CharField(max_length=10)
    start_date = models.DateField()
    end_date = models.DateField()
    year = models.ForeignKey('CoreYear', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'core_term'
        unique_together = (('year', 'code'),)


class CoreYear(models.Model):
    id = models.UUIDField(primary_key=True)
    label = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()
    school = models.ForeignKey(CoreSchool, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'core_year'


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


class HealthClinicvisit(models.Model):
    id = models.UUIDField(primary_key=True)
    date = models.DateField()
    reason = models.CharField(max_length=200)
    details_enc = models.BinaryField(blank=True, null=True, db_comment='SENSITIVE:HEALTH-ENCRYPTED')
    student = models.ForeignKey('PeopleStudent', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'health_clinicvisit'


class HealthHealthalert(models.Model):
    id = models.UUIDField(primary_key=True)
    student = models.ForeignKey('PeopleStudent', models.DO_NOTHING)
    alert_type = models.CharField(max_length=60)
    details_enc = models.BinaryField(blank=True, null=True)
    active = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    row_version = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'health_healthalert'


class HealthImmunization(models.Model):
    id = models.UUIDField(primary_key=True)
    student = models.ForeignKey('PeopleStudent', models.DO_NOTHING)
    vaccine = models.CharField(max_length=120)
    dose_no = models.SmallIntegerField(blank=True, null=True)
    taken_on = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    row_version = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'health_immunization'


class HealthMedicationlog(models.Model):
    id = models.UUIDField(primary_key=True)
    date = models.DateField()
    medicine = models.CharField(max_length=120)
    dose = models.CharField(max_length=60)
    notes_enc = models.BinaryField(blank=True, null=True, db_comment='SENSITIVE:HEALTH-ENCRYPTED')
    student = models.ForeignKey('PeopleStudent', models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    row_version = models.IntegerField()
    retention_until = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'health_medicationlog'


class HrLeaveRequest(models.Model):
    id = models.UUIDField(primary_key=True)
    staff = models.ForeignKey('PeopleStaff', models.DO_NOTHING)
    leave_type = models.CharField(max_length=40)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    row_version = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'hr_leave_request'


class HrPerformanceReview(models.Model):
    id = models.UUIDField(primary_key=True)
    staff = models.ForeignKey('PeopleStaff', models.DO_NOTHING)
    year = models.ForeignKey(CoreYear, models.DO_NOTHING)
    score = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    row_version = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'hr_performance_review'


class IdentityPermission(models.Model):
    id = models.UUIDField(primary_key=True)
    code = models.CharField(unique=True, max_length=150)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'identity_permission'


class IdentityRole(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(unique=True, max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'identity_role'


class IdentityRoleScope(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    role = models.ForeignKey(IdentityRole, models.DO_NOTHING)
    school_id = models.UUIDField(blank=True, null=True)
    year_id = models.UUIDField(blank=True, null=True)
    class_room_id = models.UUIDField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    row_version = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'identity_role_scope'
        unique_together = (('user', 'role', 'school_id', 'year_id', 'class_room_id'),)


class IdentityRolepermission(models.Model):
    id = models.BigAutoField(primary_key=True)
    permission = models.ForeignKey(IdentityPermission, models.DO_NOTHING)
    role = models.ForeignKey(IdentityRole, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'identity_rolepermission'
        unique_together = (('role', 'permission'),)


class IdentityUserrole(models.Model):
    id = models.BigAutoField(primary_key=True)
    role = models.ForeignKey(IdentityRole, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'identity_userrole'
        unique_together = (('user', 'role'),)


class LibraryLibrarycopy(models.Model):
    id = models.UUIDField(primary_key=True)
    barcode = models.CharField(unique=True, max_length=50)
    status = models.CharField(max_length=20)
    title = models.ForeignKey('LibraryLibrarytitle', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'library_librarycopy'


class LibraryLibraryloan(models.Model):
    id = models.UUIDField(primary_key=True)
    issued_on = models.DateField()
    due_on = models.DateField()
    returned_on = models.DateField(blank=True, null=True)
    borrower_staff = models.ForeignKey('PeopleStaff', models.DO_NOTHING, blank=True, null=True)
    borrower_student = models.ForeignKey('PeopleStudent', models.DO_NOTHING, blank=True, null=True)
    copy = models.ForeignKey(LibraryLibrarycopy, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'library_libraryloan'


class LibraryLibrarytitle(models.Model):
    id = models.UUIDField(primary_key=True)
    isbn = models.CharField(max_length=20)
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'library_librarytitle'


class LibraryReservation(models.Model):
    id = models.UUIDField(primary_key=True)
    copy = models.ForeignKey(LibraryLibrarycopy, models.DO_NOTHING)
    student = models.ForeignKey('PeopleStudent', models.DO_NOTHING, blank=True, null=True)
    staff = models.ForeignKey('PeopleStaff', models.DO_NOTHING, blank=True, null=True)
    reserved_on = models.DateTimeField()
    expires_on = models.DateTimeField()
    fulfilled = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    row_version = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'library_reservation'
        unique_together = (('copy', 'student', 'staff', 'fulfilled'),)


class OutboxEvent(models.Model):
    id = models.BigAutoField(primary_key=True)
    event_type = models.CharField(max_length=120)
    payload = models.JSONField()
    status = models.CharField(max_length=20)
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'outbox_event'


class PeopleEnrollment(models.Model):
    id = models.UUIDField(primary_key=True)
    grade = models.SmallIntegerField()
    status = models.CharField(max_length=20)
    class_room = models.ForeignKey(CoreClassroom, models.DO_NOTHING)
    school = models.ForeignKey(CoreSchool, models.DO_NOTHING)
    year = models.ForeignKey(CoreYear, models.DO_NOTHING)
    student = models.ForeignKey('PeopleStudent', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'people_enrollment'
        unique_together = (('student', 'school', 'year', 'grade', 'class_room'),)


class PeopleGuardian(models.Model):
    id = models.UUIDField(primary_key=True)
    first_name_ar = models.CharField(max_length=100)
    last_name_ar = models.CharField(max_length=100)
    phone = models.CharField(max_length=32, db_comment='SENSITIVE:PDPPL-CONTACT')
    email = models.CharField(max_length=254, db_comment='SENSITIVE:PDPPL-CONTACT')

    class Meta:
        managed = False
        db_table = 'people_guardian'


class PeopleStaff(models.Model):
    id = models.UUIDField(primary_key=True)
    first_name_ar = models.CharField(max_length=100)
    last_name_ar = models.CharField(max_length=100)
    job_title = models.CharField(max_length=120)
    email = models.CharField(max_length=254)

    class Meta:
        managed = False
        db_table = 'people_staff'


class PeopleStudent(models.Model):
    id = models.UUIDField(primary_key=True)
    first_name_ar = models.CharField(max_length=100)
    last_name_ar = models.CharField(max_length=100)
    first_name_en = models.CharField(max_length=100)
    last_name_en = models.CharField(max_length=100)
    national_id = models.CharField(max_length=32, blank=True, null=True, db_comment='SENSITIVE:PDPPL-ID')
    birth_date = models.DateField(db_comment='SENSITIVE:PDPPL-DOB')
    gender = models.CharField(max_length=1)
    phone = models.CharField(max_length=32, db_comment='SENSITIVE:PDPPL-CONTACT')
    email = models.CharField(max_length=254, db_comment='SENSITIVE:PDPPL-CONTACT')

    class Meta:
        managed = False
        db_table = 'people_student'


class PeopleStudentguardian(models.Model):
    id = models.BigAutoField(primary_key=True)
    relation = models.CharField(max_length=30)
    is_primary = models.BooleanField()
    guardian = models.ForeignKey(PeopleGuardian, models.DO_NOTHING)
    student = models.ForeignKey(PeopleStudent, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'people_studentguardian'
        unique_together = (('student', 'guardian'),)


class PeopleTeachingassignment(models.Model):
    id = models.BigAutoField(primary_key=True)
    class_room = models.ForeignKey(CoreClassroom, models.DO_NOTHING)
    subject = models.ForeignKey(CoreSubject, models.DO_NOTHING)
    teacher = models.ForeignKey(PeopleStaff, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'people_teachingassignment'
        unique_together = (('teacher', 'class_room', 'subject'),)


class QualityCommittee(models.Model):
    id = models.UUIDField(primary_key=True)
    committee_type = models.CharField(max_length=30)
    member_name = models.CharField(max_length=200)
    job_title = models.CharField(max_length=150)
    role_in_committee = models.CharField(max_length=50)
    responsibility = models.TextField(blank=True, null=True)
    domain = models.CharField(max_length=150, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    row_version = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'quality_committee'


class QualityEvidence(models.Model):
    id = models.UUIDField(primary_key=True)
    opi = models.ForeignKey('QualityOperationalPlanItem', models.DO_NOTHING, blank=True, null=True)
    kpi_code = models.CharField(max_length=60, blank=True, null=True)
    evidence_type = models.CharField(max_length=120, blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    row_version = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'quality_evidence'


class QualityImprovementPlan(models.Model):
    id = models.UUIDField(primary_key=True)
    school = models.ForeignKey(CoreSchool, models.DO_NOTHING, blank=True, null=True)
    year = models.ForeignKey(CoreYear, models.DO_NOTHING, blank=True, null=True)
    goal = models.TextField()
    actions = models.TextField()
    owner = models.CharField(max_length=150)
    schedule = models.TextField(blank=True, null=True)
    progress = models.CharField(max_length=120, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    row_version = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'quality_improvement_plan'


class QualityKpiSnapshot(models.Model):
    id = models.UUIDField(primary_key=True)
    kpi_code = models.CharField(max_length=60)
    kpi_label = models.CharField(max_length=200)
    snapshot_on = models.DateField()
    value_numeric = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    value_text = models.CharField(max_length=200, blank=True, null=True)
    school = models.ForeignKey(CoreSchool, models.DO_NOTHING, blank=True, null=True)
    year = models.ForeignKey(CoreYear, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    row_version = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'quality_kpi_snapshot'


class QualityOperationalPlanItem(models.Model):
    id = models.UUIDField(primary_key=True)
    year = models.CharField(max_length=20)
    domain = models.CharField(max_length=200, blank=True, null=True)
    target_no = models.CharField(max_length=40, blank=True, null=True)
    target = models.TextField(blank=True, null=True)
    indicator_no = models.CharField(max_length=60, blank=True, null=True)
    indicator = models.TextField(blank=True, null=True)
    procedure_no = models.CharField(max_length=60, blank=True, null=True)
    procedure = models.TextField(blank=True, null=True)
    date_range = models.CharField(max_length=120, blank=True, null=True)
    follow_up = models.TextField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    evidence_type = models.CharField(max_length=120, blank=True, null=True)
    evidence_source_employee = models.CharField(max_length=200, blank=True, null=True)
    evidence_source_file = models.CharField(max_length=300, blank=True, null=True)
    evaluation = models.CharField(max_length=200, blank=True, null=True)
    evaluation_notes = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=40)
    executor_committee = models.ForeignKey(QualityCommittee, models.DO_NOTHING, blank=True, null=True)
    evaluator_committee = models.ForeignKey(QualityCommittee, models.DO_NOTHING, related_name='qualityoperationalplanitem_evaluator_committee_set', blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    row_version = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'quality_operational_plan_item'


class QualityOpiExecutor(models.Model):
    id = models.BigAutoField(primary_key=True)
    opi = models.ForeignKey(QualityOperationalPlanItem, models.DO_NOTHING)
    executor = models.ForeignKey('QualityPlanExecutor', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'quality_opi_executor'
        unique_together = (('opi', 'executor'),)


class QualityPlanExecutor(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=200)
    job_title = models.CharField(max_length=150, blank=True, null=True)
    staff = models.ForeignKey(PeopleStaff, models.DO_NOTHING, blank=True, null=True)
    is_active = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    row_version = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'quality_plan_executor'


class RefdataLookupAbsenceReason(models.Model):
    code = models.CharField(primary_key=True, max_length=10)
    name_ar = models.CharField(max_length=120)

    class Meta:
        managed = False
        db_table = 'refdata_lookup_absence_reason'


class RefdataLookupBehaviorCategory(models.Model):
    code = models.CharField(primary_key=True, max_length=10)
    name_ar = models.CharField(max_length=120)

    class Meta:
        managed = False
        db_table = 'refdata_lookup_behavior_category'


class RefdataLookupNationality(models.Model):
    code = models.CharField(primary_key=True, max_length=5)
    name_ar = models.CharField(max_length=120)
    name_en = models.CharField(max_length=120)

    class Meta:
        managed = False
        db_table = 'refdata_lookup_nationality'


class RefdataLookupReligion(models.Model):
    code = models.CharField(primary_key=True, max_length=5)
    name_ar = models.CharField(max_length=120)
    name_en = models.CharField(max_length=120)

    class Meta:
        managed = False
        db_table = 'refdata_lookup_religion'


class RefdataLookupabsencereason(models.Model):
    code = models.CharField(primary_key=True, max_length=10)
    name_ar = models.CharField(max_length=120)

    class Meta:
        managed = False
        db_table = 'refdata_lookupabsencereason'


class RefdataLookupnationality(models.Model):
    code = models.CharField(primary_key=True, max_length=5)
    name_ar = models.CharField(max_length=120)
    name_en = models.CharField(max_length=120)

    class Meta:
        managed = False
        db_table = 'refdata_lookupnationality'


class TimetableTimetablerule(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=120)

    class Meta:
        managed = False
        db_table = 'timetable_timetablerule'


class TimetableTimetableslot(models.Model):
    id = models.UUIDField(primary_key=True)
    day_of_week = models.SmallIntegerField()
    period = models.SmallIntegerField()
    class_room = models.ForeignKey(CoreClassroom, models.DO_NOTHING)
    room = models.ForeignKey(CoreRoom, models.DO_NOTHING, blank=True, null=True)
    subject = models.ForeignKey(CoreSubject, models.DO_NOTHING)
    teacher = models.ForeignKey(PeopleStaff, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'timetable_timetableslot'
        unique_together = (('class_room', 'day_of_week', 'period'),)


class TransportDelayLog(models.Model):
    id = models.UUIDField(primary_key=True)
    ride = models.ForeignKey('TransportRideLog', models.DO_NOTHING)
    minutes_late = models.SmallIntegerField()
    reason = models.CharField(max_length=120, blank=True, null=True)
    notified = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    row_version = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'transport_delay_log'


class TransportRideLog(models.Model):
    id = models.UUIDField(primary_key=True)
    route = models.ForeignKey('TransportRoute', models.DO_NOTHING)
    date = models.DateField()
    departed_at = models.TimeField(blank=True, null=True)
    arrived_at = models.TimeField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    row_version = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'transport_ride_log'
        unique_together = (('route', 'date'),)


class TransportRoute(models.Model):
    id = models.UUIDField(primary_key=True)
    code = models.CharField(unique=True, max_length=50)
    capacity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'transport_route'


class TransportRouteStop(models.Model):
    id = models.UUIDField(primary_key=True)
    route = models.ForeignKey(TransportRoute, models.DO_NOTHING)
    seq = models.SmallIntegerField()
    name = models.CharField(max_length=120)
    lat = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    lon = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    row_version = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'transport_route_stop'
        unique_together = (('route', 'seq'),)


class TransportStudentrider(models.Model):
    id = models.UUIDField(primary_key=True)
    route = models.ForeignKey(TransportRoute, models.DO_NOTHING)
    student = models.ForeignKey(PeopleStudent, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'transport_studentrider'
        unique_together = (('student', 'route'),)
