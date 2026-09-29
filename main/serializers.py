from rest_framework import serializers
from .models import *

def create_model_serializer(baseModel: BaseModel):
    fields_list = baseModel.serialized_names()
    
    class ModelSerializer(serializers.ModelSerializer):
        class Meta:
            model = baseModel
            fields = fields_list
    
    return ModelSerializer

MovieSerializer = create_model_serializer(Movie)
    