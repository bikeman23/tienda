from django.urls import path 
from .views import *
urlpatterns = [
	path('quienes_somos/', quienes_somos_view, name='quienes_somos'),
	path('contactenos/', contacto_view, name='contacto'),
	path('agregar_productos/', agregar_productos_view, name = 'agregar_productos'),
	path('login/', login_view, name='login'),
	path('logout/', logout_view, name='logout'),
	path('index/', index_view, name='index'),
	path('lista_productos/', lista_productos_view, name = 'lista_productos'),
	path('nuestros_servicios/', nuestros_servicios_view, name = 'nuestros_servicios'),
	path('quienes_somos/', quienes_somos_view, name = 'quienes_somos'),
	path('ver_producto/', ver_producto_view, name = 'ver_producto'),
	path('register/', register_view, name = 'register'),
	path('thanks_for_register/', thanks_for_register_view, name = 'thanks_for_register'),
	path('servicio_web/', servicio_web_view, name='servicio_web')



	# path('lista_marca/', lista_marca_view, name='lista_marca'),
	# path('agregar_marca/', agregar_marca_view, name = 'agregar_marca'),
	# path('lista_categoria/', lista_categoria_view, name = 'lista_categoria'),
	# path('agregar_categoria/', agregar_categoria_view, name=agregar_categoria),
]  