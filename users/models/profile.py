from django.contrib.auth import get_user_model
from django.db import models


from users.models import users


class Profile(models.Model):
    user = models.OneToOneField(
        to='users.User', on_delete=models.CASCADE, related_name='profile', primary_key=True
    )
    telegram_id = models.CharField(max_length=20, blank=True, null=True, verbose_name='Telegram ID')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.user} ({self.pk})'
