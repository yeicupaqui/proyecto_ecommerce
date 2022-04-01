from django.db import models

class categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion =models.TextField(max_length=500)


    def __str__(self):
        return self.nombre

class marca(models.Model):
    nombre = models.CharField(max_length=120)

    def __str__(self):
        return self.nombre

class producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=500)
    status = models.BooleanField(default=True)
    precio = models.FloatField()
    stock = models.IntegerField()
    categoria = models.ForeignKey (categoria, on_delete=models.CASCADE)
    marca = models.ManyToManyField(marca,)

    def __str__(self):
        return self.nombre