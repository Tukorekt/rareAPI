from django.db import models

class BaseModel(models.Model):
    @classmethod
    def serialized_names(cls):
        return []
    
    @classmethod
    def lookup_field(cls):
        return None
    
    class Meta:
        abstract = True
        
class Movie(BaseModel):
    id = models.BigIntegerField(verbose_name='id')
    name = models.TextField(verbose_name='name')
    
    @classmethod
    def serialized_names(cls):
        return ['id','name']
    
    @classmethod
    def lookup_field(cls):
        return 'id'
    
    class Meta:
        abstract = False
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'
    

