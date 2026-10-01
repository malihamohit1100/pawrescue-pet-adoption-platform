from django.urls import path

from . import views


app_name = "adoptions"


urlpatterns = [
    path(
        "pets/<int:pet_id>/apply/",
        views.adoption_create_view,
        name="create",
    ),
    path(
        "dashboard/",
        views.dashboard_view,
        name="dashboard",
    ),
]