from django.contrib import admin

from .models import AdoptionRequest
from .services import (
    approve_adoption_request,
    reject_adoption_request,
)


@admin.register(AdoptionRequest)
class AdoptionRequestAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "pet",
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
    )
    readonly_fields = ("created_at",)


    def save_model(self, request, obj, form, change):
        previous = None

        if change:
            previous = AdoptionRequest.objects.get(pk=obj.pk)

        if (
            change
            and previous.status != obj.status
        ):
            if obj.status == AdoptionRequest.Status.APPROVED:
                approve_adoption_request(previous)

            elif obj.status == AdoptionRequest.Status.REJECTED:
                reject_adoption_request(previous)

        super().save_model(request, obj, form, change)