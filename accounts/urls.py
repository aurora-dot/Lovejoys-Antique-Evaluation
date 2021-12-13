from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "accounts"
urlpatterns = [
    path("signup/", views.signup_view, name="signup"),
    path(
        "login/",
        auth_views.LoginView.as_view(
            redirect_authenticated_user=True, template_name="accounts/login.html"
        ),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]