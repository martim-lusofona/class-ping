from django.urls import path, re_path
from .views import *

app_name = "class_attendance"

urlpatterns = [
    path("", courses_view, name="courses"),

    path("courses/", courses_view, name="courses"),

    path("courses/<int:course_id>/school-classes", school_classes_view, name="school-classes"),

    path("courses/<int:course_id>/school-classes/<int:school_class_id>/sessions", sessions_view, name="sessions"),

    path("sessions/<uuid:session_id>/join", join_session_view, name="attendance"),
]