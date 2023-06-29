from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class BaseDictModelMixin(models.Model):
    code = models.CharField(verbose_name='Код', max_length=16, primary_key=True)
    name = models.CharField(verbose_name='Название', max_length=32)
    sort = models.PositiveIntegerField(verbose_name='Сортировка', blank=True, null=True)
    is_active = models.BooleanField(verbose_name='Активность', default=True)


    class Meta:

        ordering = ('sort',)
        abstract = True

    def __str__(self):
        return f'{self.code}({self.name})'

