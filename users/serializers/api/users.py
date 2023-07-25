from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from rest_framework.exceptions import ParseError

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





class ChangePasswordSerializer(serializers.Serializer):
    pass