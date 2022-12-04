from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.views import (
    LoginView,
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from django.contrib import auth
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from .forms import ReaderCreationForm, CustomUserChangeForm
from .models import CustomUser


class SignUpView(CreateView):
    form_class = ReaderCreationForm
    success_url = reverse_lazy("login")
    template_name = "users/signup.html"


class LogInView(LoginView):
    success_url = reverse_lazy("home")
    template_name = "users/login.html"


class CustomPasswordChangeView(PasswordChangeView):
    template_name = "users/password_change/change_password.html"
    success_url = reverse_lazy("password_changed")


class CustomPasswordChangedView(PasswordChangeDoneView):
    template_name = "users/password_change/password_changed.html"


class CustomPasswordResetView(PasswordResetView):
    template_name = "users/password_reset/password_reset_form.html"


class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = "users/password_reset/password_reset_done.html"


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = "users/password_reset/password_reset_confirm.html"


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = "users/password_reset/password_reset_complete.html"


class MyAccountView(UpdateView):
    form_class = CustomUserChangeForm
    model = CustomUser
    template_name = "users/myaccount.html"

    def get_object(self, queryset=None):
        return self.request.user


# def signup(request):
#     if request.method == "POST":
#         # the user wants to sign up
#         if request.POST.get("password") == request.POST.get("passwordCheck"):
#             try:
#                 user = User.objects.get(username=request.POST.get("userName"))
#                 return render(
#                     request,
#                     "users/signup.html",
#                     {"error": "Username has already been taken!"},
#                 )
#             except User.DoesNotExist:
#                 user = User.objects.create_user(
#                     username=request.POST.get("userName"),
#                     password=request.POST.get("password"),
#                     email=request.POST.get("email"),
#                     first_name=request.POST.get("firstName"),
#                     last_name=request.POST.get("lastName"),
#                 )
#                 auth.login(request, user)
#                 return redirect("home")
#         else:
#             return render(
#                 request, "users/signup.html", {"error": "Passwords do not match!"}
#             )

#     else:
#         # user wants to enter info
#         return render(request, "users/signup.html")


# def login(request):
#     if request.method == "POST":
#         # the user wants to sign up
#         user = auth.authenticate(
#             username=request.POST.get("userName"), password=request.POST.get("password")
#         )
#         if user is not None:
#             auth.login(request, user)
#             return redirect("home")
#         else:
#             return render(
#                 request,
#                 "users/login.html",
#                 {"error": "Username or password is incorrect!"},
#             )
#     else:
#         # user wants to enter info
#         return render(request, "users/login.html")


# def logout(request):
#     if request.method == "POST":
#         # need to route to homepage
#         auth.logout(request)
#         return redirect("home")


# def myaccount(request):
#     return render(request, "users/myaccount.html")


# def mybooks(request):
#     return render(request, "users/mybooks.html")
