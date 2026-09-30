from django.contrib import admin

from .models import AdoptionRequest


@admin.register(AdoptionRequest)
class AdoptionRequestAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "pet",
        "phone",
        "status",
        "created_at",
    )
    list_filter = (
        "status",
        "created_at",
    )
    search_fields = (
        "user__username",
        "user__email",
        "pet__name",
        "phone",
    )
    readonly_fields = ("created_at",)