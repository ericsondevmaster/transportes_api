from rest_framework import serializers
from brands.models import Brand


class BrandSerializer(serializers.ModelSerializer):

    name = serializers.CharField(max_length=20)

    class Meta:
        model = Brand
        fields = '__all__'

    def validate_name(self, value):
        return value.upper()
