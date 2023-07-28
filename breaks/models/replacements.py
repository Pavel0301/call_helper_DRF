
from django.contrib.auth import get_user_model
from django.db import models



User = get_user_model()


class GroupInfo(models.Model):
    group = models.OneToOneField(
        to='organisations.Group', on_delete=models.CASCADE, related_name='break_info', verbose_name='Группа',
        primary_key=True
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
        verbose_name = 'Парамметр обеденных перерывов'
        verbose_name_plural = 'Параметры обеденных перерывов'



    def __str__(self):
        return f'{self.group}'



class Replacement(models.Model):
    group = models.ForeignKey(
        to='breaks.GroupInfo', on_delete=models.CASCADE, related_name='replacements', verbose_name='Группа'
    )
    date = models.DateField(verbose_name='Дата смены')
    break_start = models.TimeField(verbose_name='Начало обеда')
    break_end = models.TimeField(verbose_name='Конец обеда')
    break_max_duration = models.IntegerField(verbose_name='Максимальная продолжительность обеда')



    class Meta:
        verbose_name = 'Смена'
        verbose_name_plural = 'Смены'
        ordering = ('-date',)

    def __str__(self):
        return f'Смена №{self.pk} для {self.group}'




class ReplacementEmployee(models.Model):
    employee = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name='replacements', verbose_name='Сотрудник смены'
    )
    replacement = models.ForeignKey(
        to='breaks.Replacement', on_delete=models.CASCADE, related_name='employees', verbose_name='Смена'
    )
    status = models.ForeignKey(
        to='breaks.ReplacementStatus', on_delete=models.RESTRICT,
        related_name='replacements_employees', verbose_name='Статус'
    )

    class Meta:
        verbose_name = 'Смена - Работник'
        verbose_name_plural = 'Смены - Работники'

    def __str__(self):
        return f'Смена {self.replacement} для {self.employee}'




