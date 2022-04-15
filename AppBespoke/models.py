from django.db import models

# Create your models here.
class Bicicleta(models.Model):
    
    nombre = models.CharField(max_length=40)
    stock = models.IntegerField()
    pedido= models.BooleanField()
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Stock {self.stock} - Pedido {self.pedido}"
    
class Partes(models.Model):
    
    nombre = models.CharField(max_length=40)
    stock = models.IntegerField()
    pedido= models.BooleanField()
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Stock {self.stock} - Pedido {self.pedido}"
    
    
class Vidriera(models.Model):
    
    nombre= models.CharField(max_length=40)
    stock = models.IntegerField()
    pedido= models.BooleanField()
    
    # con esta indicación comenzamos a ver detalladamente en nuestra BD
    def __str__(self):
        return f"Nombre: {self.nombre} - Stock {self.stock} - Pedido {self.pedido}"
        
class Otro(models.Model):
    nombre= models.CharField(max_length=30)
    stock = models.IntegerField()
    pedido= models.BooleanField()
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Stock {self.stock} - Pedido {self.pedido}"