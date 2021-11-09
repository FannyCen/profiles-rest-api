from rest_framework.views import APIView
from rest_framework.views import Response
from  rest_framework import status
from profiles_api import serializers
# api/hellow-view
class HelloApiView(APIView):
    """Test API view"""
    serializer_class = serializers.HelloSerializer



    def get(self, request, format=None):
        """Returns a list of APIView features"""

        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


    def put(self, request, pk=None):
        return Response({'method': 'PUT'})


    def patch(self, request, pk=None):
        return Response({'method': 'PATCH'})
        """Handle partial update of object"""

    def delete(self, request, pk=None):
        return Response({'method': 'DELETE'})
        """Delete an object"""




















     # validation
     # # XXX:
     # db acess
     # entity(first_name) - db model one to one match profile table, first_name column
     # save to db profile table
