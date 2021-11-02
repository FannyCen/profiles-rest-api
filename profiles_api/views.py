from rest_framework.views import APIView
from rest_framework.views import Response


class HelloApiView(APIView):
    """Test API view"""
    def get(self,request,format=None):
     """ Returns a list of APIView features"""
     an_apiview = [
         'Uses HTTP methods as function(get, post, patch, put, delete)',
         'Is similar to traditional Django View',
         'Gives you the most contral over your appointment',
         'Is mapped manually to URLs',
     ]

     return Response ({'message':'hello','an_apiview': an_apiview})
