from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from apps.people.views import StudentViewSet, GuardianViewSet, StaffViewSet, EnrollmentViewSet
from apps.core.views import SchoolViewSet, YearViewSet, TermViewSet, SubjectViewSet, ClassRoomViewSet, RoomViewSet
from apps.timetable.views import TimetableSlotViewSet
from apps.attendance.views import AttendanceRecordViewSet
from apps.assessment.views import ExamViewSet, ExamResultViewSet, AppealViewSet
from apps.behavior.views import BehaviorIncidentViewSet
from apps.health.views import ClinicVisitViewSet
from apps.transport.views import RouteViewSet, StudentRiderViewSet
from apps.library.views import LibraryTitleViewSet, LibraryCopyViewSet, LibraryLoanViewSet

router=DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'guardians', GuardianViewSet)
router.register(r'staff', StaffViewSet)
router.register(r'enrollments', EnrollmentViewSet)
router.register(r'schools', SchoolViewSet)
router.register(r'years', YearViewSet)
router.register(r'terms', TermViewSet)
router.register(r'subjects', SubjectViewSet)
router.register(r'class-rooms', ClassRoomViewSet)
router.register(r'rooms', RoomViewSet)
router.register(r'timetable-slots', TimetableSlotViewSet)
router.register(r'attendance-records', AttendanceRecordViewSet)
router.register(r'exams', ExamViewSet)
router.register(r'exam-results', ExamResultViewSet)
router.register(r'appeals', AppealViewSet)
router.register(r'behavior-incidents', BehaviorIncidentViewSet)
router.register(r'clinic-visits', ClinicVisitViewSet)
router.register(r'routes', RouteViewSet)
router.register(r'student-riders', StudentRiderViewSet)
router.register(r'library-titles', LibraryTitleViewSet)
router.register(r'library-copies', LibraryCopyViewSet)
router.register(r'library-loans', LibraryLoanViewSet)

urlpatterns=[
  path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  path('', include(router.urls)),
]
