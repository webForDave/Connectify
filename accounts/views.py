from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import CustomUserDetailsSerializer, CustomRegularUserDetailsSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def user_detials(request, username):

    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response({'users': 'user not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.user == user:
        serializer = CustomUserDetailsSerializer(user)
        return Response(serializer.data)
    
    else:
        serializer = CustomRegularUserDetailsSerializer(user)
        return Response(serializer.data)