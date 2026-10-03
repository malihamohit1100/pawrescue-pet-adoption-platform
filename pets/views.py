from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from favorites.models import Favorite

from .models import Pet


def home_view(request):
    featured_pets = Pet.objects.filter(
        status=Pet.AdoptionStatus.AVAILABLE
    )[:6]

    return render(
        request,
        "pets/home.html",
        {
            "featured_pets": featured_pets,
        },
    )


def pet_list_view(request):
    pets = Pet.objects.all()

    search = request.GET.get("search", "").strip()
    animal_type = request.GET.get("animal_type", "").strip()
    breed = request.GET.get("breed", "").strip()
    gender = request.GET.get("gender", "").strip()
    location = request.GET.get("location", "").strip()
    status = request.GET.get("status", "").strip()

    if search:
        pets = pets.filter(
            Q(name__icontains=search)
            | Q(breed__icontains=search)
            | Q(animal_type__icontains=search)
            | Q(location__icontains=search)
        )

    if animal_type:
        pets = pets.filter(animal_type=animal_type)

    if breed:
        pets = pets.filter(breed__icontains=breed)

    if gender:
        pets = pets.filter(gender=gender)

    if location:
        pets = pets.filter(location__icontains=location)

    if status:
        pets = pets.filter(status=status)

    paginator = Paginator(pets, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "pets/pet_list.html",
        {
            "page_obj": page_obj,
            "search": search,
            "animal_type": animal_type,
            "breed": breed,
            "gender": gender,
            "location": location,
            "status": status,
            "animal_types": Pet.AnimalType.choices,
            "genders": Pet.Gender.choices,
            "statuses": Pet.AdoptionStatus.choices,
        },
    )


def pet_detail_view(request, pk):
    pet = get_object_or_404(Pet, pk=pk)

    is_favorite = False

    if request.user.is_authenticated:
        is_favorite = Favorite.objects.filter(
            user=request.user,
            pet=pet,
        ).exists()

    return render(
        request,
        "pets/pet_detail.html",
        {
            "pet": pet,
            "is_favorite": is_favorite,
        },
    )