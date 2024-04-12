from rest_framework import serializers
from .models import MyUser


class UserListSerializers(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('email', 'username', 'cover')


class UserDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = '__all__'


class UserCreateUpdateSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = MyUser
        fields = ('username', 'email', 'phone_number', 'cover', 'password')

    def create(self, validated_data):
        user = MyUser.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        instance = super().update(instance, validated_data)
        if password:
            instance.set_password(password)
            instance.save()
        return instance


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('id', 'cover', 'username', 'phone_number', 'email')
