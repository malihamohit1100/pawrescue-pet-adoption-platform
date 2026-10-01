from rest_framework import serializers

from pets.models import Pet


class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = [
            "id",
            "name",
            "image",
            "animal_type",
            "breed",
            "age",
            "gender",
            "location",
            "description",
            "status",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]