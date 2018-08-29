from rest_framework import serializers
from home.models import *

class producto_serializer(serializers.HyperlinkedModelSerializer):
	"""docstring for producto_serializer"""
	class Meta:
		model = Producto 
		fields = ('url', 'nombre', 'status', 'foto', 'precio', 'stock', 'marca', 'categoria',)


class marca_serializer(serializers.HyperlinkedModelSerializer):
	"""docstring for producto_serializer"""
	class Meta:
		model = Marca 
		fields = ('url', 'id', 'nombre',)

class categoria_serializer(serializers.HyperlinkedModelSerializer):
	"""docstring for producto_serializer"""
	class Meta:
		model = Categoria 
		fields = ('url', 'nombre',)
