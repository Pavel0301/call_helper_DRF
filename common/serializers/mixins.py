from rest_framework import serializers


class ExtendedModelSerializer(serializers.ModelSerializer):



    class Meta:
        abstract = True
