from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

from startup.models import Startup
from startup.api.serializers import StartupSerializer

@api_view(['GET',])
def api_detail_startup_view(request, slug):
    try:
        startup = get_object_or_404(Startup, pk=slug)
    except Startup.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = StartupSerializer(startup)
        return Response(serializer.data)

