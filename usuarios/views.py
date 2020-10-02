from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from usuarios import serializers
from .serializers import UserSerializer, ProductosSerializer, CarritoSerializer, OrdenSerializer
from .models import UserProfile, Productos, Carrito, Orden
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404


class UsersApiView(APIView):

	serializer_class = serializers.UserSerializer

	def get(self, request, format = None):

		users = UserProfile.objects.all()

		serial = UserSerializer(users, many = True)

		return Response(serial.data)


	def post(self, request):

		serializer = UserSerializer(data = request.data)

		if serializer.is_valid():

			serializer.save()

			return Response(serializer.data, status = status.HTTP_201_CREATED)

		else:

			return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class UserManageApi(APIView):

	serializer_class = serializers.UserSerializer

	def delete(self, request, pk, format = None):

		user = UserProfile.objects.get(id = pk)

		user.delete()

		return Response({'Status': 'OK'})

class ProductosList(APIView):

	serializer_class = ProductosSerializer

	def get(self, request):

		serializer = ProductosSerializer(Productos.objects.all(), many = True)

		return Response(serializer.data)

	def post(self, request):

		serializer = ProductosSerializer(data = request.data)

		if serializer.is_valid():

			serializer.save()

			return Response(serializer.data, status = status.HTTP_201_CREATED)

		else:

			return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class ProductosManage(APIView):

	serializer_class = ProductosSerializer

	def delete(self, request, pk, format = None):

		try:

			producto = Productos.objects.get(id = pk)

			producto.delete()

			return Response({'Status': 'El producto se ha eliminado con éxito.'})

		except ObjectDoesNotExist:

			return Response({'Status': 'El producto no se ha encontrado.'}, status = status.HTTP_400_BAD_REQUEST)

	def put(self, request, pk, format = None):

		try:

			serializer = ProductosSerializer(Productos.objects.get(id = pk), data = request.data)

			if serializer.is_valid():

				serializer.save()

				return Response(serializer.data)

			else:

				return Response(
				serializer.errors,
				status = status.HTTP_400_BAD_REQUEST
				)

		except ObjectDoesNotExist:

			return Response({'Status': 'El producto no se ha encontrado.'}, status = status.HTTP_400_BAD_REQUEST)

class CarritoListAPI(APIView):

	serializer_class = serializers.CarritoSerializer

	def get(self, request, format = None):

		serializer = CarritoSerializer(Carrito.objects.all(), many = True)

		return Response(serializer.data)

	def post(self, request, format = None):

		serializer = CarritoSerializer(data = request.data)

		if serializer.is_valid():

			serializer.save()

			return Response(serializer.data)

		else:

			return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class OrdenListAPI(APIView):

	serializer_class = OrdenSerializer

	def get(self, request, format = None):

		serializer = OrdenSerializer(Orden.objects.all(), many = True)

		return Response(serializer.data, status = status.HTTP_200_OK)

	def post(self, request, format = None):

		serializer = OrdenSerializer(data = request.data)

		if serializer.is_valid():

			serializer.save()

			return Response({'Status': 'La orden ha sido creada.'}, status = status.HTTP_201_CREATED)

		else:

			return Response({'Status': 'La información es invalida'}, status = status.HTTP_400_BAD_REQUEST)


class OrdenManageAPI(APIView):

	serializer_class = OrdenSerializer

	def put(self, request, pk, format = None):

		try:

			serializer = OrdenSerializer(Orden.objects.get(id = pk), data = request.data)

			if serializer.is_valid():

				serializer.save()

				return Response({'Status': 'La orden se ha actualizado.'})

		except ObjectDoesNotExist:

			return Response({'Status': 'La orden no se ha encontrado.'})

	def delete(self, request, pk, format = None):

		try:

			orden_o = Orden.objects.get(id = pk)

			orden_o.delete()

			return Response({'Status': 'Se ha eliminado la orden con éxito.'})

		except ObjectDoesNotExist:

			return Response({'Status': 'La orden no se ha encontrado.'})









class CarritoManageAPI(APIView):

	serializer_class = CarritoSerializer

	def delete(self, request, pk, format = None):

		try:

			producto = Carrito.objects.get(id = pk)

			producto.delete()

			return Response({'Status': 'El producto ha sido eliminado del carrito.'})

		except ObjectDoesNotExist:

			return Response({'Status': 'El producto no está en el carrito.'})

	def put(self, request, pk,  format = None):

		serializer = CarritoSerializer(Carrito.objects.get(id = pk), data = request.data)

		if serializer.is_valid():

			serializer.save()

			return Response({'Status': 'El carrito se ha actualizado con éxito.'})

		else:

			return Response({'Status': 'La información es invalida.'})







class HelloApiView(APIView):

	serializer_class = serializers.HelloSerializer

	def get(self, request, format = None):

		an_apiview = {

			'Hola mundo': 'xd'

		}

		return Response({'message': 'Hello', 'an_apiview': an_apiview})

	def post(self, request):

		serializer = self.serializer_class(data = request.data)

		if serializer.is_valid():

			name = serializer.validated_data.get('name')
			message = 'Hello ' + name
			return Response({'message': message})

		else:

			return Response(
				serializer.errors,
				status = status.HTTP_400_BAD_REQUEST
				)