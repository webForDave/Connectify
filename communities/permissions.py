from rest_framework.permissions import BasePermission

class UserIsNotNew(BasePermission):
    #ensures that user accounts lte 30 days cannot create communities to prevent spam commmunities
    message = 'You must be a member for at least 30 days to create a community.'

    def has_permission(self, request, view):
            if request.method == 'GET':
                return True
            return request.user.is_authenticated and not request.user.user_joined_recently()