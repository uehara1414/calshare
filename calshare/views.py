from django.conf.urls import url

from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def hello_world(request):
    """## Some documentations"""
    return Response({'result': "Hello World"})


urlpatterns = [
    url(r'', hello_world)
]
