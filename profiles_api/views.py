from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status
from profiles_api import serializers

from rest_framework import viewsets
from profiles_api import models

from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions

from rest_framework import filters

# Create your views here.

class HelloApiView(APIView):
    '''Test api view'''

    serializer_class = serializers.HelloSerializer

    #can use any keyword for req or request the parameter passed is the request
    #from browser (maybe)
    def get(self, req, format = None):
        '''Returns a list of apiview features'''
        an_apiview=[
            'Uses http method as function(get, post, patch,put , delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over you rapplication logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message' : 'Hello', 'an_apiview' : an_apiview})


    def post(self, request):
        """create a hello mssg with name"""
        serializer_post = self.serializer_class(data = request.data)

        if serializer_post.is_valid():
            name = serializer_post.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message' : message})
        else:
            return Response(
                serializer_post.errors,
                status = status.HTTP_400_BAD_REQUEST
            )


    def put(self,req,pk = None):
        """Handle updating an object"""
        #pk = primary key id of object ot be updated is updating objects
        return Response({'method': 'Put'})


    def patch(self,request,pk=None):
        """Handle partial update of object"""
        return Response({'method':'patch'})


    def delete(self,reques,pk=None):
        """to delete an object"""
        return Response({'method':'delete'})


class HelloViewSet(viewsets.ViewSet):
    """Test Api Viewset"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """return  a hello mssg"""

        a_viewset = [
            'uses action (list, create, retrieve, update, partial_update)',
            'automatically maps to URLs using Routers',
            'Provides more functionality with less code',
        ]

        return Response({'message':'Hello','a_viewset':a_viewset})

    def create(self, request):
        """create a new hello mssg"""

        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message' : message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk = None):
        """handle getting an object by its ID"""

        return Response({'http_method' : 'GET'})

    def update(self,request,pk= None):
        '''handle updating an object'''
        return Response({'http_method': 'PUT'})

    def partial_update(self,request,pk= None):
        '''handle updating part of object'''
        return Response({'http_method': 'Patch'})

    def destroy(self,request,pk= None):
        '''handle removing an object'''
        return Response({'http_method': 'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """handle creating and updating profiles"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)
