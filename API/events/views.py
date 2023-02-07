from django.shortcuts import render

from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



@api_view(['GET'])
def events_list(request):
    events_all = Events.objects.all()
    serializer = eventsSerializer(events_all,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def events_detail(request,pk):
    events_s = get_object_or_404(Events,pk=pk)
    serializer = eventsSerializer(events_s)
    return Response(serializer.data)

@api_view(['POST'])
def events_post(request):
    serializer = eventsSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  


