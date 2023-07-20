from rest_framework import serializers
from .models import Album
from users.serializers import UserSerializer


class AlbumSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Album
        fields = ["id", "name", "year", "user"]
        read_only_fields = ["user", "id"]

    def get_user(self, obj):
        user = obj.user
        serializer = UserSerializer(user)
        return serializer.data

    def create(self, validated_data):
        album = Album.objects.create(**validated_data)
        return album
