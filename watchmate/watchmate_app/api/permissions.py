from rest_framework import permissions

class AdminOrReadOnly(permissions.IsAdminUser):
    def has_permission(self,request,view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            try:
                user=request.user()
                if request.user.is_staff():
                    return True
            except:
                return False
            # if request.is_authenticated():
            #     if request.user.is_staff():
            #         return True
            # return False

class ReviewUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self,request,view,obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.review_user == request.user
         
        