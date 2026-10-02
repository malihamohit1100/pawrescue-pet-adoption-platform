from rest_framework.permissions import BasePermission


class IsStaffOrReadOnly(BasePermission):
    """
    Anyone can read pet data.
    Only staff users can create, update, or delete pets.
    """

    def has_permission(self, request, view):
        if request.method in ("GET", "HEAD", "OPTIONS"):
            return True

        return (
            request.user.is_authenticated
            and request.user.is_staff
        )