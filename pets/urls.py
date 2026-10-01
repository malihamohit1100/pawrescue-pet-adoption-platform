from django.urls import path

from . import views

app_name = "pets"

urlpatterns = [
    path(
        "",
        views.home_view,
        name="home",
    ),
    path(
        "pets/",
        views.pet_list_view,
        name="list",
    ),
    path(
        "pets/<int:pk>/",
        views.pet_detail_view,
        name="detail",
    ),
]