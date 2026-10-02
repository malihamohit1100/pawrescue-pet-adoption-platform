from django.core.exceptions import ValidationError
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from adoptions.models import AdoptionRequest
from adoptions.services import approve_adoption_request

from .serializers import AdoptionRequestSerializer


class AdoptionRequestViewSet(viewsets.ModelViewSet):
    serializer_class = AdoptionRequestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return (
            AdoptionRequest.objects
            .filter(user=self.request.user)
            .select_related("pet", "user")
        )

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user,
            status=AdoptionRequest.Status.PENDING,
        )

    def update(self, request, *args, **kwargs):
        adoption_request = self.get_object()

        if adoption_request.status != AdoptionRequest.Status.PENDING:
            return Response(
                {
                    "detail": (
                        "Only pending adoption requests "
                        "can be updated."
                    )
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        return super().update(
            request,
            *args,
            **kwargs,
        )


    def destroy(self, request, *args, **kwargs):
        adoption_request = self.get_object()

        if adoption_request.status != AdoptionRequest.Status.PENDING:
            return Response(
                {
                    "detail": (
                        "Only pending adoption requests "
                        "can be deleted."
                    )
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        return super().destroy(
            request,
            *args,
            **kwargs,
        )