from rest_framework import serializers

from adoptions.models import AdoptionRequest
from pets.models import Pet


class AdoptionRequestSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")
    pet_name = serializers.ReadOnlyField(source="pet.name")

    class Meta:
        model = AdoptionRequest
        fields = [
            "id",
            "user",
            "pet",
            "pet_name",
            "phone",
            "address",
            "reason",
            "previous_pet_experience",
            "message",
            "status",
            "created_at",
        ]
        read_only_fields = [
            "id",
            "user",
            "pet_name",
            "status",
            "created_at",
        ]

    def validate_pet(self, pet):
        if pet.status != Pet.AdoptionStatus.AVAILABLE:
            raise serializers.ValidationError(
                "This pet is no longer available for adoption."
            )

        return pet