from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UserCreationForm
from .models import User

# Register your models here.


class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    model = User
    list_display = ["email", "username", "phone_number", "first_name", "last_name"]


admin.site.register(User, UserAdmin)
