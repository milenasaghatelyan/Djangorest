from rest_framework.serializers import ModelSerializer
from .models import *

class CarSerializer(ModelSerializer):
    class Meta:
        model = Cars
        fields = '__all__'

