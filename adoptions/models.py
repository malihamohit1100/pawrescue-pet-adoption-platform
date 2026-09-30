from django.contrib.auth.models import User
from django.db import models

from pets.models import Pet


class AdoptionRequest(models.Model):
    class Status(models.TextChoices):
        PENDING = "Pending", "Pending"
        APPROVED = "Approved", "Approved"
        REJECTED = "Rejected", "Rejected"

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="adoption_requests",
    )
    pet = models.ForeignKey(
        Pet,
        on_delete=models.CASCADE,
        related_name="adoption_requests",
    )
    phone = models.CharField(max_length=20)
    address = models.TextField()
    reason = models.TextField()
    previous_pet_experience = models.BooleanField(default=False)
    message = models.TextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        constraints = [
            models.UniqueConstraint(
                fields=["user", "pet"],
                condition=models.Q(status="Pending"),
                name="unique_pending_adoption_request",
            ),
        ]

    def __str__(self):
        return f"{self.user.username} → {self.pet.name}"