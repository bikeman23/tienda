from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.core import serializers


from .forms import *
from .models import *



# Create your views here.

def quienes_somos_view(request):
	nombre = [12,3,45,67,89,436,51]
	#return render(request, 'quienes_somos.html', {'n':nombre})
	return render(request, 'quienes_somos.html', locals())

def contacto_view(request):
	email=""
	subject=""
	text=""
	info_enviado = False
	if request.method=='POST':
		formulario = contacto_form(request.POST)
		if formulario.is_valid():
			email  	= formulario.cleaned_data['correo']
			subject = formulario.cleaned_data['asunto']
			text 	= formulario.cleaned_data['texto']
			info_enviado = True
			return render(request, 'contacto.html', locals())
		else:
			msg = 'la informacion no es correcta'	
	else: # si es un metodo GET		
		formulario = contacto_form()
	return render(request, 'contacto.html', locals())

def index_view(request):
	return render(request,'index.html')

def nuestros_servicios_view(request):
	return render(request,'nuestros_servicios.html')

def lista_productos_view(request):
	lista = Producto.objects.filter(status=True)
	return render(request, 'lista_productos.html', locals())

def agregar_productos_view(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			formulario = agregar_productos_form(request.POST, request.FILES)
			if formulario.is_valid():
				formulario.save()
				return redirect('/lista_productos/') #Importar Redirect
			else:
				msj = "Hay datos por verificar"
		else:
			formulario=agregar_productos_form()

		return render(request, 'agregar_productos.html', locals())
	else:
		return (request, 'lista_productos.html',locals())

def ver_producto_view(request, id_prod): #le paso el mismo nombre del parametro que esta en la url
	try:
		obj=Producto.objects.get(id=id_prod) #obtenga un objeto de producto segun su id y guardelo en la variable

	except:
		print("error en la consulta EL PRODUCTO NO EXISTE")
		msj="error en la consulta EL PRODUCTO NO EXISTE"
	return render(request,'ver_producto.html',locals())

def editar_producto_view(request, id_prod): #le paso el mismo nombre del parametro que esta en la url
		#no hay necesidad de crear html
	#hago la consulta
	obj=Producto.objects.get(id=id_prod) # ya me deberia cargar la info
	if request.method=='POST':   #paso la info que viene desde el POST
		formulario=agregar_producto_form(request.POST, request.FILES, instance=obj)
		if formulario.is_valid():
			#formulario.save(commit =False) #solo guarda en RAM 
			formulario.save()
			return redirect('/lista_productos')
	else:	
		formulario=agregar_producto_form(instance=obj)

	formulario=agregar_producto_form(instance=obj) #me trae el mismo formulario
	return render(request,'agregar_producto.html',locals())


def eliminar_producto_view(request, id_prod):
	obj=Producto.objects.get(id=id_prod)
	obj.delete()
	return redirect('/lista_productos')

def desactivar_producto_view(request, id_prod):
	obj=Producto.objects.get(id=id_prod)
	obj.status=False
	obj.save()
	return redirect('/lista_productos')

def login_view(request):
	if request.method=='POST':
		formulario = login_form (request.POST)
		if formulario.is_valid():
			user = formulario.cleaned_data['usuario']
			cla = formulario.cleaned_data['clave']

			usuario = authenticate(username=user, password=cla)
			if usuario is not None and usuario.is_active:
				login(request, usuario)
				return redirect('/lista_productos/')
			else:
				msj="usuario o clave incorrectos"


	formulario=login_form()

	return render(request, 'login.html', locals())

def logout_view(request):
	logout(request)
	return redirect('/login/')

def register_view(request):
	formulario=register_form()

	if request.method == 'POST':
		formulario=register_form(request.POST)
		if formulario.is_valid():

			usuario = formulario.cleaned_data['username']
			correo = formulario.cleaned_data['email']
			password_1 = formulario.cleaned_data['password_1']
			password_2 = formulario.cleaned_data['password_2']
			u= User.objects.create_user(username=usuario, email=correo, password=password_1)
			u.save()
			return render(request, 'thansk_for_register.html', locals())
		else:
			return render(request, 'register.html', locals())

	return render(request, 'register.html', locals())

def thanks_for_register_view(request):
	return render (request, 'register.html', locals())

def servicio_web_view(request):
	data= serializers.serialize('xml', Producto.objects.all())
	return HttpResponse(data, content_type ='application/xml')





