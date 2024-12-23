from rest_framework.views import APIView
from .serializers import PatientSerializer
from rest_framework.response import Response
from rest_framework import status
from .forms import PatientRegistrationForm
from django.shortcuts import render, redirect
from rest_framework.generics import RetrieveUpdateAPIView
from .models import Patient
from rest_framework.permissions import IsAuthenticated
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout


class PatientRegistrationView(APIView):
    def get(self, request, *args, **kwargs):
        form = PatientRegistrationForm()
        return render(request, "patient_user/register.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(
                request,
                "patient_user/success.html",
                {"message": "Registration Successful"},
            )
        return render(
            request,
            "patient_user/register.html",
            {"form": form, "error": "Form is not valid"},
        )


class PatientProfileView(RetrieveUpdateAPIView):
    queryset = Patient.objects.all()
    serializer = PatientSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data("username")
            password = form.cleaned_data("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("dashboard")
            else:
                form.add_error(None, "Invalid username or password")
    else:
        form = LoginForm()

    return render(request, "patient_user/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("login")


def success(request):
    return render(request, "success.html", {"message": "Registration Successful"})
