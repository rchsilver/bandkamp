from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data: dict) -> User:
        return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.set_password(instance.password)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "password",
            "full_name",
            "artistic_name",
            "email"
        ]
        extra_kwargs = {
            "id": {"read_only": True},
            "username": {
                "validators": [
                    UniqueValidator(
                        queryset=User.objects.all(),
                        message="A user with that username already exists."
                    )
                ]},
            "password": {"write_only": True},
            "email": {
                "validators": [
                    UniqueValidator(queryset=User.objects.all())
                ]},
        }
