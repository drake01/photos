from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Image, Album
import datetime

class AlbumSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')
    name = serializers.CharField(required=False)
    class Meta:
        model = Album
        fields = ['id', 'name', 'user']

    #def to_representation(self, obj):
    #    obj = super().to_representation(self, obj)

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return super().update(instance, validated_data)

class ImageSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')
    url = serializers.CharField(required=False)

    class Meta:
        model = Image
        fields = ['id', 'url', 'title', 'created', 'user', 'albums']

    def create(self, validated_data):
        # print(self.context)
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.url = validated_data.get('url', instance.url)
        instance.save()
        return super().update(instance, validated_data)

    def to_internal_value(self, data):
        albums =  data.get('albums', [])
        if albums:
            # When albums is sent from client, allow only adding albums belonging to the logged in user.
            # Using httpie client:
            # http -a abc:abc PUT http://127.0.0.1:8000/api/v1/image/5/ albums:='[1,3,4]' title='new image'
            # if albums 1,2 belong to current user, above request will set albums = [1]
            # We didn't do it by overriding validate_albums() as we have list
            # in validate_ methods We won't be able to do  .filter(user=current_user)
            # We 'd have to iterate list of objects.
            data['albums'] = Album.objects.filter(id__in=albums).filter(user=self.context['request'].user)
        return data

class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ['id', 'username', 'email', 'password']

        def create(self, validated_data):
            user = super(UserSerializer, self).create(validated_data)
            user.set_password(validated_data['password'])
            user.save()
            return user

        def update(self, instance, validated_data):
            use = super(UserSerializer, self).update(validated_data)
            instance.set_password(validated_data['password'])
            instance.save()
            return user

