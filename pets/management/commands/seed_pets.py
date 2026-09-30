from django.core.management.base import BaseCommand

from pets.models import Pet


class Command(BaseCommand):
    help = "Create sample pets for development"

    def handle(self, *args, **options):
        pets = [
            {
                "name": "Max",
                "animal_type": "Dog",
                "breed": "Golden Retriever",
                "age": 2,
                "gender": "Male",
                "location": "Dhaka",
                "description": (
                    "Max is friendly, playful, and enjoys spending time "
                    "with people. He is looking for a caring family."
                ),
                "status": "Available",
            },
            {
                "name": "Luna",
                "animal_type": "Cat",
                "breed": "Domestic Shorthair",
                "age": 1,
                "gender": "Female",
                "location": "Dhaka",
                "description": (
                    "Luna is a calm and affectionate cat who enjoys "
                    "quiet surroundings and gentle attention."
                ),
                "status": "Available",
            },
            {
                "name": "Coco",
                "animal_type": "Rabbit",
                "breed": "Holland Lop",
                "age": 2,
                "gender": "Female",
                "location": "Chattogram",
                "description": (
                    "Coco is a gentle rabbit who is comfortable around "
                    "people and enjoys a peaceful environment."
                ),
                "status": "Available",
            },
            {
                "name": "Rocky",
                "animal_type": "Dog",
                "breed": "Labrador Retriever",
                "age": 3,
                "gender": "Male",
                "location": "Dhaka",
                "description": (
                    "Rocky is energetic and social. He enjoys outdoor "
                    "activities and is comfortable around people."
                ),
                "status": "Available",
            },
            {
                "name": "Milo",
                "animal_type": "Cat",
                "breed": "Persian",
                "age": 4,
                "gender": "Male",
                "location": "Sylhet",
                "description": (
                    "Milo is a relaxed and affectionate cat who enjoys "
                    "a comfortable home environment."
                ),
                "status": "Adopted",
            },
            {
                "name": "Kiwi",
                "animal_type": "Bird",
                "breed": "Budgerigar",
                "age": 1,
                "gender": "Female",
                "location": "Rajshahi",
                "description": (
                    "Kiwi is a lively little bird who enjoys interaction "
                    "and a safe indoor environment."
                ),
                "status": "Available",
            },
            {
                "name": "Bruno",
                "animal_type": "Dog",
                "breed": "Beagle",
                "age": 2,
                "gender": "Male",
                "location": "Khulna",
                "description": (
                    "Bruno is curious, friendly, and enjoys playing "
                    "and exploring new surroundings."
                ),
                "status": "Available",
            },
            {
                "name": "Bella",
                "animal_type": "Cat",
                "breed": "Domestic Shorthair",
                "age": 3,
                "gender": "Female",
                "location": "Dhaka",
                "description": (
                    "Bella is gentle and independent while still enjoying "
                    "affection from people."
                ),
                "status": "Adopted",
            },
        ]

        created_count = 0

        for pet_data in pets:
            pet, created = Pet.objects.get_or_create(
                name=pet_data["name"],
                defaults=pet_data,
            )

            if created:
                created_count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully created {created_count} sample pets."
            )
        )