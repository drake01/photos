from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import ImageSerializer, AlbumSerializer, UserSerializer
from .models import Image, Album
from .permissions import IsOwner, CheckLoggedIn
from django.contrib.auth.models import User

class ImageViewSet(viewsets.ModelViewSet):
    queryset =  Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner,]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user
        return Image.objects.filter(user=user)

class AlbumViewSet(viewsets.ModelViewSet):
    queryset =  Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner,]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user
        return Album.objects.filter(user=user)

class UserViewSet(viewsets.ModelViewSet):
    # Listview works without logging in to see user list,
    # object level permission: CheckLoggedIn allows editing only current user object
    queryset =  User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [CheckLoggedIn,]
