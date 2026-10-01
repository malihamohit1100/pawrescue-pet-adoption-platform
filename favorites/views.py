from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

from pets.models import Pet

from .models import Favorite


@login_required
def toggle_favorite(request, pet_id):
    pet = get_object_or_404(Pet, pk=pet_id)

    favorite, created = Favorite.objects.get_or_create(
        user=request.user,
        pet=pet,
    )

    if created:
        messages.success(
            request,
            f"{pet.name} was added to your favorites.",
        )
    else:
        favorite.delete()

        messages.info(
            request,
            f"{pet.name} was removed from your favorites.",
        )

    return redirect("pets:detail", pk=pet.pk)