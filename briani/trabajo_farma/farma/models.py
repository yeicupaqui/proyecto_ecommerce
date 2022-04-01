from django.db import models

# Create your models here.



class Categoria (models.Model):
	codigo 				= models.IntegerField(unique=True)
	nombre 				= models.CharField(max_length=50)

	def __str__(self):
		return self.nombre 

class Producto (models.Model):
	codigo 				= models.IntegerField(unique=True)
	nombre 				= models.CharField(max_length=40, unique=True)
	precio 				= models.DecimalField(max_digits = 8, decimal_places = 2)
	especificaciones 	= models.TextField(max_length = 5000, null= True, blank = True)
	categoria 			= models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="productos")
