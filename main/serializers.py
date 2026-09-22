from rest_framework import serializers
from .models import Product, BaseModel

def create_model_serializer(baseModel):
    fields_list = baseModel.serialized_names()
    
    class ModelSerializer(serializers.ModelSerializer):
        class Meta:
            model = baseModel
            fields = fields_list
    
    return ModelSerializer

ProductSerializer = create_model_serializer(Product)
    