from rest_framework import permissions

class IsStaffOrReadOnly(permissions.IsAdminUser):
    #! category işlemlerininde sadece get işlemini her kullanıcı yapabilir, put post delete işlemlerini sadece staff user yapabilir:
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return bool(request.user and request.user.is_staff)
    

class IsOwnerOrReadOnly(permissions.BasePermission):
    #! Bloglarda get işlemini her kullanıcı yapabilecek update ve delete işlemlerini yalnızca blog sahibi ve staff user yapabilecek:
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True 
        return bool(obj.user == request.user or request.user.is_staff)
        

class IsOwnerOrReadOnlyComment(permissions.BasePermission):
    #! Her kullanıcı kendi yorumunu düzenleyebilecek herkesin yorumunu görüntüleyebilecek:
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True 
        return bool(obj.user == request.user)