from django.db import models

from common.models.mixins import BaseDictModelMixin


class ReplacementStatus(BaseDictModelMixin):

    class Meta:
        verbose_name = 'Статус смены'
        verbose_name_plural = 'Статус Смен'




class BreakStatus(BaseDictModelMixin):


    class Meta:
        verbose_name = 'Статус обеда'
        verbose_name_plural = 'Статус обеда'

