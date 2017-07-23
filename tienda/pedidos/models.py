from django.contrib.auth.models import User
from django.db import models

from productos.models import Producto


class Pedido(models.Model):
    usuario = models.ForeignKey(User)

    estado = models.PositiveIntegerField(
        choices=(
            (1, 'Recibido'),
            (2, 'Cancelado'),
            (3, 'Pagado'),
            (4, 'Entregado')
        ),
        default=1,
        blank=False,
        null=False
    )

    tipo_pago = models.PositiveIntegerField(
        choices=(
            (1, 'Efectivo'),
            (2, 'Contra entrega'),
            (3, 'Tarjeta'),
            (4, 'Paypal'),
        ),
        blank=False,
        null=False
    )

    fecha = models.DateTimeField(auto_now_add=True)

    # fecha_entrega

    # cantidad


class CantidadProducto(models.Model):
    pedido = models.ForeignKey(Pedido)
    producto = models.ForeignKey(Producto)
    cantidad = models.PositiveIntegerField(
        default=1,
        blank=False,
        null=False
    )

