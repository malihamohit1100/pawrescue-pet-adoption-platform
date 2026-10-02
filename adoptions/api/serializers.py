from rest_framework import serializers

from adoptions.models import AdoptionRequest


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