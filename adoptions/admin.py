from django.contrib import admin
from django.core.exceptions import ValidationError
from django.db import transaction

from .models import AdoptionRequest


@admin.register(AdoptionRequest)
class AdoptionRequestAdmin(admin.ModelAdmin):
    list_display = ("user", "pet", "phone", "status", "created_at")
    list_filter = ("status", "created_at")
    search_fields = ("user__username", "user__email", "pet__name", "phone")
    readonly_fields = ("created_at",)

    def save_model(self, request, obj, form, change):
        if obj.status == AdoptionRequest.Status.APPROVED:
            if obj.pet.status != "Available":
                # Allow an already-approved request to be saved
                # without trying to approve the pet again.
                if change:
                    previous = AdoptionRequest.objects.get(pk=obj.pk)

                    if previous.status == AdoptionRequest.Status.APPROVED:
                        super().save_model(request, obj, form, change)
                        return

                raise ValidationError(
                    "This pet is no longer available for adoption."
                )

            with transaction.atomic():
                obj.save()

                obj.pet.status = "Adopted"
                obj.pet.save(update_fields=["status"])

                AdoptionRequest.objects.filter(
                    pet=obj.pet,
                    status=AdoptionRequest.Status.PENDING,
                ).exclude(
                    pk=obj.pk
                ).update(
                    status=AdoptionRequest.Status.REJECTED
                )

        else:
            super().save_model(request, obj, form, change)
