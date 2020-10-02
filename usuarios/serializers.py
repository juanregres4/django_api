from rest_framework import serializers
from .models import UserProfile, Productos, Carrito, Orden, detalle_Orden


class HelloSerializer(serializers.Serializer):

	name = serializers.CharField(max_length = 10)

class UserSerializer(serializers.ModelSerializer):

	class Meta:

		model = UserProfile

		fields = ['email', 'name', 'password']


class ProductosSerializer(serializers.ModelSerializer):

	class Meta:

		model = Productos

		fields = '__all__'

class CarritoSerializer(serializers.ModelSerializer):

	class Meta:

		model = Carrito

		fields = '__all__'

class OrdenSerializer(serializers.ModelSerializer):

	class Meta:

		model = Orden

		fields = '__all__'