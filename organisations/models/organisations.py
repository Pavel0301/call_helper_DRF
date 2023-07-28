

from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

from common.models.mixins import InfoMixin, DateMixin
from organisations.models.dicts import Position

User = get_user_model()

class Organisation(InfoMixin):
    name = models.CharField(verbose_name='Название', max_length=250)
    director = models.ForeignKey(
        to=User, on_delete=models.RESTRICT, related_name='organisations_directors', verbose_name='Директор'
    )
    employee = models.ManyToManyField(
        to=User, related_name='organisations_employees', verbose_name='Сотрудники', blank=True, through='Employee'
    )

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'
        ordering = ('name',)


    def __str__(self):
        return f'{self.name}({self.pk})'



class Employee(models.Model):
    organisation = models.ForeignKey(
        to=Organisation, on_delete=models.CASCADE, related_name='employees_info'
    )
    user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name='organisations_info'
    )
    position = models.ForeignKey(
        to=Position, on_delete=models.RESTRICT, related_name='employees'
    )
    date_joined = models.DateField('Date joined', default=timezone.now)

    class Meta:
        verbose_name = 'Сотрудник организации'
        verbose_name_plural = 'Сотрудники организации'
        ordering = ('-date_joined',)
        unique_together = [['organisation', 'user'],]    # без повторений прий выборе

    def __str__(self):
        return f'Employee {self.user}'

