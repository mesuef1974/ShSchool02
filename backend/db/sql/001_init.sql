-- Optional DDL complement (you may rely on Django migrations instead)
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS pgcrypto;
-- مثال: قيود مطابقة للفهرس الفريد المطلوب (تُنشأ عادة عبر مهاجرات Django)
-- term: uq_term_year_code, class_room: uq_class_room_school_year_grade_section,
-- attendance_record: uq_attendance_record_enrollment_date_period,
-- exam_result: uq_exam_result_enrollment_exam, appeal: uq_appeal_enrollment_exam
