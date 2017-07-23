from django.contrib.auth.models import User
from django.db import models


class Perfil(models.Model):
    usuario = models.OneToOneField(User)

    direccion = models.TextField(
        blank=False,
        null=False
    )

    telefono = models.CharField(
        max_length=9,
        blank=False,
        null=False
    )

    edad = models.PositiveIntegerField(
        blank=False,
        null=False
    )

    avatar = models.ImageField(
        upload_to='avatar',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.usuario.username
