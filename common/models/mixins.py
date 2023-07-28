from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from config import settings

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


class DateMixin(models.Model):
    created_at = models.DateTimeField(verbose_name='Created at', blank=False, null=True)
    updated_at = models.DateTimeField(verbose_name='Updated at', blank=False, null=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.pk and not self.created_at:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(DateMixin, self).save(*args, **kwargs)



class InfoMixin(DateMixin):
    created_by = models.ForeignKey(
        to=User, on_delete=models.SET_NULL, related_name='created_%(app_label)s_%(class)s',
        verbose_name='Created by', null=True)
    updated_by = models.ForeignKey(
        to=User, on_delete=models.SET_NULL, related_name='updated_%(app_label)s_%(class)s',
        verbose_name='Updated by', null=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        from crum import get_current_user

        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.created_by = user
        self.updated_by = user
        super().save(*args, **kwargs)