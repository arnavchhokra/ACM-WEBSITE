from .models import *
from rest_framework.serializers import ModelSerializer


class eventsSerializer(ModelSerializer):
    class Meta:
        model = Events
        fields = "__all__"