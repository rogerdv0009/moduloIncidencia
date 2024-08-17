from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

rol_user = [
    (1, 'Técnico'),
    (2, 'Especialista'),
    (3, 'Administrador')
]

class User(AbstractUser):
    avatar = models.ImageField(upload_to="avatar/%y/%m/%d", null=True, blank=True)
    rol = models.IntegerField(
        verbose_name='Rol',
        null= False, blank=False,
        choices= rol_user, default=1)