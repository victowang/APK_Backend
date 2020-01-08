from rest_framework import serializers

class AppSerializer(serializers.Serializer):
    application = serializers.CharField(max_length=200)
    package_name = serializers.CharField(max_length=200)
    package_version_code = serializers.CharField(max_length=200)