from django.urls import path
from . import views
from patient_user import views
from patient_user.views import PatientRegistrationView, PatientProfileView

urlpatterns = [
    path("register/", PatientRegistrationView.as_view(), name="patient_register"),
    path("profile/", PatientProfileView.as_view(), name="patient_profile"),
    path("success/", views.success, name="success"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]
