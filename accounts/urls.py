from django.contrib.auth import views as auth_views
from django.urls import path, re_path

from . import views

app_name = "accounts"
urlpatterns = [
    path("signup/", views.signup_view, name="signup"),
    path(
        "login/",
        views.login_view,
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    re_path(
        r"^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,32})/$",  # noqa: E501
        views.validate_email,
        name="verify_email",
    ),
    path("login/verify/", views.verify_view, name="verify_login"),
]
