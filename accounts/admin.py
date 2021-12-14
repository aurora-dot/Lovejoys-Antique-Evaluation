from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# from .forms import UserCreationForm
from .models import User, Profile

# Register your models here.


class UserAdmin(UserAdmin):
    model = User
    list_display = ["email", "username", "first_name", "last_name", "phone_number"]

    def phone_number(self, obj):
        return obj.profile.phone_number


class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = ["username", "phone_number"]

    def username(self, obj):
        return obj.user.username


admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)
