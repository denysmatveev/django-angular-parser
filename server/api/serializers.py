from rest_framework import serializers
from api.models import DataList


class DataListSerializer(serializers.ModelSerializer):

    class Meta:
        model = DataList
        fields = ('title', 'date_2019', 'date_2018', 'date_2017', 'date_2016')
