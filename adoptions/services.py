from django.core.exceptions import ValidationError
from django.db import transaction

from .models import AdoptionRequest


def approve_adoption_request(adoption_request):
    with transaction.atomic():
        pet = adoption_request.pet

        if adoption_request.status != AdoptionRequest.Status.PENDING:
            raise ValidationError(
                "Only pending adoption requests can be approved."
            )

        if pet.status != "Available":
            raise ValidationError(
                "This pet is no longer available for adoption."
            )

        adoption_request.status = AdoptionRequest.Status.APPROVED
        adoption_request.save(update_fields=["status"])

        pet.status = "Adopted"
        pet.save(update_fields=["status"])

        AdoptionRequest.objects.filter(
            pet=pet,
            status=AdoptionRequest.Status.PENDING,
        ).exclude(
            pk=adoption_request.pk
        ).update(
            status=AdoptionRequest.Status.REJECTED
        )


def reject_adoption_request(adoption_request):
    if adoption_request.status != AdoptionRequest.Status.PENDING:
        raise ValidationError(
            "Only pending adoption requests can be rejected."
        )

    adoption_request.status = AdoptionRequest.Status.REJECTED
    adoption_request.save(update_fields=["status"])