from rest_framework import serializers
from .models import *
from .serializers import *

def create_model_viewset(baseModel: BaseModel, 
                         serializer: serializers.ModelSerializer, 
                         lookup_field_v:str):
    class ModelViewset(serializers.ModelSerializer):
        queryset = baseModel.objects.all()
        serializer_class = serializer
        lookup_field = lookup_field_v
        
    
    return ModelViewset

MovieViewSet = create_model_viewset(Movie, MovieSerializer, 'slug')
    
    
        
        
        
    
