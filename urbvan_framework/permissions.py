from rest_framework import permissions


class IsManagerOrReadOnly(permissions.BasePermission):
    """
    Global-Object-level permissions to only allow managers to edit it
    Urbvan administrator to delete it.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS or request.user.has_perm('user.is_urbvan_administrator'):
            return True
        if request.method == 'POST':
            if view.get_view_name() in ['Location', 'Station']:
                return request.user.has_perm('users.is_station_manager')
            elif view.get_view_name() in ['Line', 'Route']:
                return request.user.has_perm('users.is_line_manager')
        else:
            return True


    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS or request.user.has_perm('user.is_urbvan_administrator'):
            return True
        else:
            if request.method == 'DELETE':
                return False
            elif view.get_view_name() in ['Location Detail', 'Station Detail']:
                return request.user.has_perm('users.is_station_manager')
            elif view.get_view_name() in ['Line Detail', 'Route Detail']:
                return request.user.has_perm('users.is_line_manager')
            else:
                return False
