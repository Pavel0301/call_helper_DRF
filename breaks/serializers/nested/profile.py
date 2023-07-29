from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from rest_framework.exceptions import ParseError

from users.models.profile import Profile


class ProfileShortSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = (
           'telegram_id',
        )



class ProfileUpdateSerializer(serializers.ModelSerializer):


    class Meta:
        model = Profile
        fields = (
            'telegram_id',
        )
"""
for key, value in profile_data.items():
    if hasattr(profile, key):
        setattr(profile, key, value)
profile.save()
"""