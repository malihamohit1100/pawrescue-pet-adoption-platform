from django.urls import path

from . import views


app_name = "favorites"


urlpatterns = [
    path(
        "pets/<int:pet_id>/toggle/",
        views.toggle_favorite,
        name="toggle",
    ),
]