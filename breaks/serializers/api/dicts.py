from django.contrib.auth import get_user_model

from breaks.models import dicts
from common.serializers.mixins import ExtendedModelSerializer, DictMixinSerializer
from organisations.models.dicts import Position


User = get_user_model()
"""
class ReplacementStatusListSerializer(DictMixinSerializer):



    class Meta:
        model = dicts.ReplacementStatus
        fields = (
            'code',
            'name',
        )



class BreakStatusListSerializer(DictMixinSerializer):
    class Meta:
        model = dicts.BreakStatus
        fields = (
            'code',
            'name',
        )
"""