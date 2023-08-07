from rest_framework.permissions import IsAuthenticatedOrReadOnly, BasePermission

class IsAdminOrReadOnly(BasePermission):
    
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return bool(request.user and request.user.is_staff)
    
    
class IsAdminOrRead(IsAuthenticatedOrReadOnly):

    def has_permission(self, request, view):
        SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_staff
        )
    
