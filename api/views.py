from django.shortcuts import render
from api.serializers import UserAccountsSerializer

# Create your views here.
# from django.contrib.auth.models import User, Group
from rest_framework import viewsets , mixins, viewsets ,generics
from rest_framework import permissions
from home.models import Authenticate


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token


class AccountViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Authenticate.objects.all()
    serializer_class = UserAccountsSerializer
    permission_classes = []

class DetailedAccountViewSet(viewsets.ModelViewSet):
  
    serializer_class = UserAccountsSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        pickup_id = self.kwargs['pk']
        return Authenticate.objects.filter(pk=pickup_id)
