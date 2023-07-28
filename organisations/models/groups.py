from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

from common.models.mixins import InfoMixin

User = get_user_model()


class Group(InfoMixin):
    organisation = models.ForeignKey(
        to='Organisation', on_delete=models.CASCADE, related_name='groups', verbose_name='Организация'
    )
    name = models.CharField('Название', max_length=250)
    manager = models.ForeignKey(
        to=User, on_delete=models.RESTRICT, related_name='groups_manager', verbose_name='Менеджер'
    )
    members = models.ManyToManyField(
        to=User, related_name='groups_members', verbose_name='Участники', blank=True, through='Member'
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





class Member(models.Model):
    group = models.ForeignKey(
        to=Group, on_delete=models.CASCADE, related_name='members_info'
    )
    user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name='group_info'
    )

    date_joined = models.DateField('Date joined', default=timezone.now)

    class Meta:
        verbose_name = 'Участник группы'
        verbose_name_plural = 'Участники группы'
        ordering = ('-date_joined',)
        unique_together = [['group', 'user']]    # без повторений прий выборе

    def __str__(self):
        return f'Employee {self.user}'
