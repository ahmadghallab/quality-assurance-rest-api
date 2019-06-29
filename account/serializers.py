from rest_framework import serializers

from . import models

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        fields = ('id', 'email', 'username', 'date_joined', 'password')
        model = models.User

    def create(self, validated_data):
        user = models.User.objects.create_user(**validated_data)
        user.save()
        return user