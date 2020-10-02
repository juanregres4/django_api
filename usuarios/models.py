from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserProfileManager(BaseUserManager):

	def create_user(self, email, name, password = None):

		if not email:

			raise ValueError('Debe ingresar un email')

		email = self.normalize_email(email)

		user = self.model(email = email, name = name)

		user.set_password(password)

		user.save(using = self._db)

		return user

	def create_superuser(self, email, name, password = None):

		if not email:

			raise ValueError('Debe ingresar un email')

		email = self.normalize_email(email)

		user = self.create_user(email = email, name = name)

		user.is_superuser = True
		user.is_staff = True
		user.set_password(password)
		user.save(using = self._db)
		return user

class UserProfile(AbstractBaseUser, PermissionsMixin):

	""" Modelo Base de Datos para Usuarios en el Sistema """

	email = models.EmailField(max_length = 255, unique = True)
	name = models.CharField(max_length = 255)
	is_active = models.BooleanField(default = True)
	is_staff = models.BooleanField(default = False)

	objects = UserProfileManager()

	USERNAME_FIELD = 'email'

	REQUIRED_FIELDS = ['name']

	def get_full_name(self):

		return self.name

	def get_short_name(self):

		return self.name

	def __str__(self):

		return self.email

class Productos(models.Model):

	nombre = models.CharField(max_length = 50)
	descripcion = models.CharField(max_length = 100)
	costo = models.IntegerField()
	precio_venta = models.IntegerField()


	def __str__(self):

		return self.nombre

class Carrito(models.Model):

	cantidad = models.IntegerField()
	id_productos = models.ForeignKey(Productos, on_delete = models.CASCADE)
	id_usuarios = models.ForeignKey(UserProfile, on_delete = models.CASCADE)

class Orden(models.Model):

	fecha = models.DateField()

	id_usuario = models.ForeignKey(UserProfile, on_delete = models.CASCADE)

	total = models.IntegerField()

class detalle_Orden(models.Model):

	id_orden = models.ForeignKey(Orden, on_delete = models.CASCADE)

	id_producto = models.ForeignKey(Productos, on_delete = models.CASCADE)

	cantidad = models.IntegerField()

	sub_total = models.IntegerField()