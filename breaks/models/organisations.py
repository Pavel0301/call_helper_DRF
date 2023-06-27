import os

from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()
class Organisation(models.Model):
    name = models.CharField(verbose_name='Название', max_length=250)
    director = models.ForeignKey(
        to=User, on_delete=models.RESTRICT, related_name='organisation', verbose_name='Директор'
    )
    employee = models.ManyToManyField(
        to=User, related_name='organisation_employees', verbose_name='Сотрудники', blank=True
    )

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'
        ordering = ('name',)

    def __str__(self):
        return f'{self.name}({self.pk})'



