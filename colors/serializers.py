from rest_framework import serializers
from colors.models import Color


class ColorSerializer(serializers.ModelSerializer):

    name = serializers.CharField(max_length=30)

    class Meta:
        model = Color
        fields = '__all__'

    def validate_name(self, value):
        return value.upper()
