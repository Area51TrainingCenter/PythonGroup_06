from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(
        max_length=50,
        blank=False,
        null=False
    )

    def __str__(self):
        return self.nombre


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

    categorias = models.ManyToManyField(Categoria)

    talla = models.PositiveIntegerField(
        choices=(
            (1, 'XS'),
            (2, 'S'),
            (3, 'M'),
            (4, 'L'),
            (5, 'XL'),
        ),
        blank=True,
        null=True
    )

    stock = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False
    )

    def __str__(self):
        return self.nombre


class ImagenProducto(models.Model):
    producto = models.ForeignKey(Producto)
    imagen = models.ImageField(
        upload_to='productos',
        blank=False,
        null=False
    )

    def __str__(self):
        return self.producto.nombre

    class Meta:
        verbose_name = 'Imagen de producto'
        verbose_name_plural = 'Imágenes de producto'
