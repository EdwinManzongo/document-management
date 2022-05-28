from django.contrib.auth.models import User, Group
from rest_framework import serializers
from home.models import Authenticate
from rest_framework.validators import UniqueTogetherValidator

class UserAccountsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Authenticate
        fields = ['id','username','firstname','lastname','access_level']
