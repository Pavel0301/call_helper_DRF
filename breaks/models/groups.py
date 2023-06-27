from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Group(models.Model):
    organisation = models.ForeignKey(
        to='breaks.Organisation', on_delete=models.CASCADE, related_name='groups', verbose_name='Организация'
    )
    name = models.CharField('Название', max_length=250)
    manager = models.ForeignKey(
        to=User, on_delete=models.RESTRICT, related_name='group_manager', verbose_name='Менеджер'
    )
    employee = models.ManyToManyField(
        to=User, related_name='group_employees', verbose_name='Сотрудники', blank=True
    )
    min_active = models.PositiveSmallIntegerField(
        verbose_name='Минимальное количество активных сотрудников', blank=True, null=True,
    )
    break_start = models.TimeField(verbose_name='Начало обеда', blank=True, null=True)
    break_end = models.TimeField(verbose_name='Конец обеда', blank=True, null=True)
    break_max_duration = models.PositiveSmallIntegerField(
        verbose_name='Максимальная длительность обеда', blank=True, null=True
    )

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
        ordering = ('name',)


    def __str__(self):
        return f'{self.name}({self.pk})'