
from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()

class Replacement(models.Model):
    group = models.ForeignKey(
        to='breaks.Group', on_delete=models.CASCADE, related_name='replacements', verbose_name='Группа'
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


class ReplacementStatus(models.Model):
    code = models.CharField(verbose_name='Код', max_length=16, primary_key=True)
    name = models.CharField(verbose_name='Название', max_length=32)
    sort = models.PositiveIntegerField(verbose_name='Сортировка', blank=True, null=True)
    is_active = models.BooleanField(verbose_name='Активность', default=True)


    class Meta:
        verbose_name = 'Статус смены'
        verbose_name_plural = 'Статус Смен'
        ordering = ('sort',)


    def __str__(self):
        return f'Смена {self.code} для {self.name}'



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

