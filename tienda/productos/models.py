from django.db import models


class Producto(models.Model):
    nombre = models.CharField(
        max_length=100,
        blank=False,
        null=False
    )

    descripcion = models.TextField(
        blank=True,
        null=True
    )

    precio = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        default=0.0,
        blank=False,
        null=False
    )

    fecha_creacion = models.DateTimeField(
        auto_now_add=True
    )

    fecha_modificacion = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.nombre
