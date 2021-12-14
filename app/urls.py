from django.urls import path
from . import views

app_name = "app"
urlpatterns = [
    path("", views.index, name="index"),
    path("request_evaluation/", views.request_evaluation, name="request_evaluation"),
    path("view_requests/", views.admin_view_requests, name="admin_view_requests"),
]
