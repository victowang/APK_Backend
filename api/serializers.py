from rest_framework import serializers
from api.models import App


class AppSerializer(serializers.Serializer):
    application = serializers.CharField(max_length=200)
    package_name = serializers.CharField(max_length=200)
    package_version_code = serializers.CharField(max_length=200)

    class Meta:
        model = App
        fields = ('application', 'package_name', 'package_version_code')