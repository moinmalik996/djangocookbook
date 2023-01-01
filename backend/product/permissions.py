from rest_framework import permissions

class IsStaffProductPermission(permissions.DjangoModelPermissions):

    """
    Some Deep Insights in DRF Permissions
    """
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }

    def has_permission(self, request, view):
        
        user = request.user
        if not user.is_staff:
            return False
        
        return super().has_permission(request, view)
    
    # This method for checking permissions will not check
    # the actio permissions like view, add, change or delete.
    # Infact if any one permission is given this function will
    # return True which will give user every permission on the API.

    # However this can be checked whether a user is staff member
    # or not. :)
    
    # def has_permission(self, request, view):
    #     user = request.user
    #     if user.is_staff:
    #         print(user.get_all_permissions())

    #         if user.has_perm('product.view_product'):
    #             print('Has View Permission')
    #             return True
    #         if user.has_perm('product.add_product'):
    #             print('Has  Add Permission')
    #             return True
    #         if user.has_perm('product.change_product'):
    #             print('Has  Update Permission')
    #             return True
    #         if user.has_perm('product.delete_product'):
    #             print('Has Delete Permission')
    #             return True
    #     return False