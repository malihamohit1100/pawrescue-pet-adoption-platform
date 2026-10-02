from rest_framework.routers import DefaultRouter

from .views import AdoptionRequestViewSet


router = DefaultRouter()

router.register(
    "adoptions",
    AdoptionRequestViewSet,
    basename="adoption",
)

urlpatterns = router.urls