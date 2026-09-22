from django.db import models

# Create your models here.

class BaseModel(models.Model):
    @classmethod
    def serialized_names(cls):
        return []
    
    class Meta:
        abstract = True

class Product(BaseModel):
    NAME_MAX_LENGTH = 63
    
    name = models.CharField(verbose_name='Название', max_length=NAME_MAX_LENGTH, db_index=True, editable=True)
    available_to_purchase  = models.BooleanField(verbose_name='Доступен для покупки', default=True, db_index=True, editable=True)
    description = models.TextField(verbose_name='Описание', max_length=255)
    price_in_rubles = models.DecimalField(verbose_name='Цена в рублях', max_digits=8, decimal_places=2, db_index=True)
    slug = models.CharField(max_length=NAME_MAX_LENGTH*2+1, editable=True, unique=True)
    
    @classmethod
    def serialized_names(cls):
        return ['name','available_to_purchase', 'description',  'price_in_rubles', 'slug']
    
    class Meta:
        verbose_name = 'Товар',
        verbose_name_plural = 'Товары'
    

