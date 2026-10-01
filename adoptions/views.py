from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from favorites.models import Favorite
from pets.models import Pet

from .forms import AdoptionRequestForm
from .models import AdoptionRequest


@login_required
def adoption_create_view(request, pet_id):
    pet = get_object_or_404(Pet, pk=pet_id)

    if pet.status != "Available":
        messages.error(
            request,
            "This pet is no longer available for adoption.",
        )
        return redirect("pets:detail", pk=pet.pk)

    active_request_exists = AdoptionRequest.objects.filter(
        user=request.user,
        pet=pet,
        status=AdoptionRequest.Status.PENDING,
    ).exists()

    if active_request_exists:
        messages.warning(
            request,
            "You already have a pending adoption request for this pet.",
        )
        return redirect("pets:detail", pk=pet.pk)

    if request.method == "POST":
        form = AdoptionRequestForm(request.POST)

        if form.is_valid():
            adoption_request = form.save(commit=False)
            adoption_request.user = request.user
            adoption_request.pet = pet
            adoption_request.status = AdoptionRequest.Status.PENDING
            adoption_request.save()

            messages.success(
                request,
                "Your adoption request has been submitted successfully.",
            )

            return redirect("adoptions:dashboard")
    else:
        form = AdoptionRequestForm()

    return render(
        request,
        "adoptions/adoption_form.html",
        {
            "form": form,
            "pet": pet,
        },
    )


@login_required
def dashboard_view(request):
    adoption_requests = (
        AdoptionRequest.objects
        .filter(user=request.user)
        .select_related("pet")
    )

    favorites = Favorite.objects.filter(
        user=request.user
    ).select_related("pet")

    return render(
        request,
        "adoptions/dashboard.html",
        {
            "adoption_requests": adoption_requests,
            "favorites": favorites,
        },
    )