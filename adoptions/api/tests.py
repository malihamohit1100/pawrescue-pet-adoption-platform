from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

from adoptions.models import AdoptionRequest
from pets.models import Pet


class AdoptionAPITests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="adopter",
            password="TestPassword123",
        )

        self.other_user = User.objects.create_user(
            username="otheruser",
            password="TestPassword123",
        )

        self.pet = Pet.objects.create(
            name="Buddy",
            animal_type="Dog",
            breed="Labrador",
            age=3,
            gender="Male",
            location="Dhaka",
            description="Friendly dog.",
            status="Available",
        )

    def authenticate(self):
        self.client.force_authenticate(
            user=self.user
        )

    def test_anonymous_user_cannot_list_adoptions(self):
        response = self.client.get(
            "/api/adoptions/"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED,
        )

    def test_authenticated_user_can_create_adoption(self):
        self.authenticate()

        response = self.client.post(
            "/api/adoptions/",
            {
                "pet": self.pet.id,
                "phone": "01700000000",
                "address": "Dhaka",
                "reason": "I can provide a safe home.",
                "previous_pet_experience": True,
                "message": "I love dogs.",
            },
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )

        self.assertEqual(
            response.data["status"],
            "Pending",
        )

    def test_user_can_only_see_own_adoptions(self):
        AdoptionRequest.objects.create(
            user=self.other_user,
            pet=self.pet,
            phone="01800000000",
            address="Dhaka",
            reason="Other user request",
            previous_pet_experience=False,
        )

        self.authenticate()

        response = self.client.get(
            "/api/adoptions/"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        self.assertEqual(
            response.data["count"],
            0,
        )

    def test_cannot_apply_for_adopted_pet(self):
        self.pet.status = "Adopted"
        self.pet.save(update_fields=["status"])

        self.authenticate()

        response = self.client.post(
            "/api/adoptions/",
            {
                "pet": self.pet.id,
                "phone": "01700000000",
                "address": "Dhaka",
                "reason": "I want to adopt.",
                "previous_pet_experience": True,
                "message": "",
            },
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
        )