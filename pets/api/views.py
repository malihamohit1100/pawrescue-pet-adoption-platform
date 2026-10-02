from rest_framework import viewsets

from pets.models import Pet

from .permissions import IsStaffOrReadOnly
from .serializers import PetSerializer


class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = [IsStaffOrReadOnly]

    filterset_fields = [
        "animal_type",
        "gender",
        "status",
    ]

    search_fields = [
        "name",
        "breed",
        "animal_type",
        "location",
        "description",
    ]

    ordering_fields = [
        "name",
        "age",
        "created_at",
    ]

    ordering = ["-created_at"]