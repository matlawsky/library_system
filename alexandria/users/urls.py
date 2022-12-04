from django.contrib import admin
from django.urls import path
from .views import (
    SignUpView,
    LogInView,
    MyAccountView,
    CustomPasswordChangeView,
    CustomPasswordChangedView,
    CustomPasswordResetCompleteView,
    CustomPasswordResetConfirmView,
    CustomPasswordResetDoneView,
    CustomPasswordResetView,
)

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", LogInView.as_view(), name="login"),
    path("myaccount/", MyAccountView.as_view(), name="myaccount"),
    path(
        "password_change/", CustomPasswordChangeView.as_view(), name="password_change"
    ),
    path(
        "password_change_done/",
        CustomPasswordChangedView.as_view(),
        name="password_change_done",
    ),
    path(
        "password_reset/",
        CustomPasswordResetView.as_view(),
        name="password_reset",
    ),
    path(
        "password_reset_done/",
        CustomPasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "password_reset_complete/",
        CustomPasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
    path(
        "password_reset_confirm/",
        CustomPasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
]
# path("mybooks/", MyBooksView.as_view(), name="mybooks"),
