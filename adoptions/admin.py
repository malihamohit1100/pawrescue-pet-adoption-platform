from django.contrib import admin
from django.core.exceptions import ValidationError

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
        if obj.status == AdoptionRequest.Status.APPROVED:
            approve_adoption_request(obj)
            return

        if (
            change
            and obj.status == AdoptionRequest.Status.REJECTED
        ):
            previous = AdoptionRequest.objects.get(pk=obj.pk)

            if previous.status != AdoptionRequest.Status.REJECTED:
                reject_adoption_request(obj)

                if previous.status == AdoptionRequest.Status.PENDING:
                    return

        super().save_model(request, obj, form, change)