from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email','password')
        extra_kwargs = {'password':{'write_only':True,'required':True}}
# создание юзера
    def create(self, validated_data):
        self.user = User.objects.create_user(**validated_data)
        return self.user
