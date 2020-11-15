
from django.db import models
from django.utils import timezone


class Producto(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    artistaProducto = models.CharField(max_length=50)
    albumProducto = models.CharField(max_length=50)
    imagenProducto = models.TextField(max_length=30)
    precioProducto = models.CharField(max_length=15)
    codigoProducto = models.TextField(max_length=50)
    stockProducto = models.IntegerField(default=0)

    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.albumProducto
