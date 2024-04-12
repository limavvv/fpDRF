from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.permissions import *
from movie.permissios import *

class UserListAPIView(generics.ListAPIView):
    queryset = MyUser.objects.all()
    serializer_class = UserListSerializers
    permission_classes = [AllowAny]

class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MyUser.objects.all()
    serializer_class = UserDetailSerializers
    permission_classes = [IsAdminOrReadOnly]

class UserCreateAPIView(generics.CreateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = UserCreateUpdateSerializers
    permission_classes = [AllowAny]

class UserUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = UserCreateUpdateSerializers
    permission_classes = [IsOwnerOrReadOnly]


class UserDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MyUser.objects.all()
    serializer_class = UserCreateUpdateSerializers
    permission_classes = [IsOwnerOrReadOnly]    


class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]  # Требуется аутентификация

    def get_object(self):
        return self.request.user

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
