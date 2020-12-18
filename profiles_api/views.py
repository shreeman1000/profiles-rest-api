from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class HelloApiView(APIView):
    '''Test api view'''

    def get(self, request, format = None):
        '''Returns a list of apiview features'''
        an_apiview=[
            'Uses http method as function(get, post, patch,put , delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over you rapplication logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message' : 'Hello', 'an_apiview' : an_apiview})
