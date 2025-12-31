# core Django.
from django.contrib.auth import get_user_model

# third party.
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# accounts app.
from .serializers import (
    OwnerDetailsSerializer, 
    RandomUserDetailsSerializer, 
    UpdateUserSerializer,
)

User = get_user_model()

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def user_details(request, username):
    
    try:
        user = User.objects.get(username__iexact=username)
    except User.DoesNotExist:
        return Response({'users': 'user not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # checks whether the user making the request is the owner of the profile.
        if request.user == user:
            serializer = OwnerDetailsSerializer(user)
            return Response(serializer.data)
        
        else:
            serializer = RandomUserDetailsSerializer(user)
            return Response(serializer.data)
    
    # Runs before a PUT or DELETE request to determine the permission of the user.
    if request.user != user:
        return Response(
            {'users': 'You do not have permission to perform this action'}, 
            status=status.HTTP_403_FORBIDDEN
        )
        
    if request.method == 'PUT':

        serializer = UpdateUserSerializer(user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)