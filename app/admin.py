from django.contrib import admin
from .models import EvaluationRequest

# Register your models here.


class EvaluationRequestAdmin(admin.ModelAdmin):
    model = EvaluationRequest
    list_display = ["item_description", "contact_method", "contact_method_detail"]

    def contact_method_detail(self, obj):
        if obj.contact_method == "E":
            return obj.user.email
        else:
            return obj.user.profile.phone_number


admin.site.register(EvaluationRequest, EvaluationRequestAdmin)
