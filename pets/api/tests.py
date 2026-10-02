from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

from pets.models import Pet


class PetAPITests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="normaluser",
            password="TestPassword123",
        )

        self.staff = User.objects.create_user(
            username="staffuser",
            password="TestPassword123",
            is_staff=True,
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

    def test_anyone_can_list_pets(self):
        response = self.client.get("/api/pets/")

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

    def test_pet_search(self):
        response = self.client.get(
            "/api/pets/?search=Buddy"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        self.assertEqual(
            response.data["count"],
            1,
        )

    def test_normal_user_cannot_create_pet(self):
        self.client.force_authenticate(
            user=self.user
        )

        response = self.client.post(
            "/api/pets/",
            {
                "name": "Max",
                "animal_type": "Dog",
                "breed": "Beagle",
                "age": 2,
                "gender": "Male",
                "location": "Dhaka",
                "description": "Friendly dog.",
                "status": "Available",
            },
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN,
        )

    def test_staff_can_create_pet(self):
        self.client.force_authenticate(
            user=self.staff
        )

        response = self.client.post(
            "/api/pets/",
            {
                "name": "Max",
                "animal_type": "Dog",
                "breed": "Beagle",
                "age": 2,
                "gender": "Male",
                "location": "Dhaka",
                "description": "Friendly dog.",
                "status": "Available",
            },
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )