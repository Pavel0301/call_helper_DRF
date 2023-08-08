import pdb

from crum import get_current_user
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ParseError

from common.serializers.mixins import ExtendedModelSerializer
from organisations.models.organisations import Organisation
from organisations.serializers.nested.users import UserShortSerializer

User = get_user_model()

class OrganisationSearchSerializer(ExtendedModelSerializer):
    director = UserShortSerializer()
    class Meta:
        model = Organisation
        fields = (
            'id',
            'name',
            'director',
        )



class OrganisationListSerializer(ExtendedModelSerializer):
    director = UserShortSerializer()

    class Meta:
        model = Organisation
        fields = '__all__'


class OrganisationRetrieveSerializer(ExtendedModelSerializer):
    director = UserShortSerializer()

    class Meta:
        model = Organisation
        fields = '__all__'


class OrganisationCreateSerializer(ExtendedModelSerializer):

    class Meta:
        model = Organisation
        fields = (
            'id',
            'name',
        )


class OrganisationUpdateSerializer(ExtendedModelSerializer):


    class Meta:
        model = Organisation
        fields = (
            'id',
            'name',
        )



