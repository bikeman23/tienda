from django.shortcuts import render
from .serializer import *
from rest_framework import viewsets

class producto_viewset(viewsets.ModelViewSet):
	"""docstring for producto_viewset"""
	queryset =  Producto.objects.all()
	serializer_class = producto_serializer

class marca_viewset(viewsets.ModelViewSet):
	"""docstring for marca_viewset"""
	queryset=Marca.objects.all()
	serializer_class = marca_serializer

class categoria_viewset(viewsets.ModelViewSet):
	"""docstring for marca_viewset"""
	queryset=Categoria.objects.all()
	serializer_class = categoria_serializer
		
		
# Create your views here.
