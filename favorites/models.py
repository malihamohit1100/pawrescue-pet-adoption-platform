from django.contrib.auth.models import User
from django.db import models

from pets.models import Pet


class Favorite(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="favorites",
    )
    pet = models.ForeignKey(
        Pet,
        on_delete=models.CASCADE,
        related_name="favorited_by",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        constraints = [
            models.UniqueConstraint(
                fields=["user", "pet"],
                name="unique_user_favorite",
            ),
        ]

    def __str__(self):
        return f"{self.user.username} ❤️ {self.pet.name}"