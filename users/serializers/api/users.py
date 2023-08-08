from django.contrib.auth import get_user_model
from django.db import transaction
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from rest_framework.exceptions import ParseError

from users.serializers.nested.profile import ProfileShortSerializer, ProfileUpdateSerializer

#from users.models.profile import Profile

User = get_user_model()

class RegistrationSerializer(serializers.ModelSerializer):

    email = serializers.EmailField()
    password = serializers.CharField(allow_blank=False, allow_null=False, required=False, write_only=True)
    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'password',
        )

    def validate_email(self, value):
        email = value.lower()
        if User.objects.filter(email=email).exists():
            raise ParseError(
                'Пользователь с такой почтой уже зарегестрирован.'
            )
        return email

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data) # пароль будет зашифрован
        return user




class ChangePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'old_password',
            'new_password'
        )

    def validate(self, attrs):
        user = self.instance
        old_password = attrs.pop('old_password')
        if not user.check_password(old_password):
            raise ParseError(
                'Проверьте правильность текущего пароля'
            )
        return attrs

    def validate_new_password(self, value):
        validate_password(value)
        return value


    def update(self, instance, validated_data):
        password = validated_data.pop('new_password')
        instance.set_password(password)
        instance.save()
        return instance


class MeSerializer(serializers.ModelSerializer):

    profile = ProfileShortSerializer()

    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'username',
            'profile',
            'date_joined',
        )


class MeUpdateSerializer(serializers.ModelSerializer):

    profile = ProfileUpdateSerializer()

    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'username',
            'profile',
        )



    def update(self, instance, validated_data):
        # проверка наличия профиля
        profile_data = validated_data.pop('profile') if 'profile' in validated_data else None

        with transaction.atomic():
            instance = super().update(instance, validated_data)

            if profile_data:
                self._update_profile(instance, profile_data)
        return instance

    def _update_profile(self, instance, profile_data):
        profile = instance.profile
        profile_serializer = ProfileUpdateSerializer(
            instance=profile, data=profile_data, partial=True # partial - частичное изменение, не нужно засылать все поля
        )

        profile_serializer.is_valid(raise_exception=True)
        profile_serializer.save()

        return instance




class UserSearchListSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'full_name',
        )