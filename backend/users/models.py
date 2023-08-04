from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    '''Custom user model.'''
    email = models.EmailField(
        _('email address'),
        unique=True,
    )
    password = models.CharField(
        max_length=255,
        help_text=_('Required.'),
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'username', 'first_name', 'last_name',
    ]

    class Meta:
        verbose_name = _('Пользователь')
        verbose_name_plural = _('Пользователи')
        ordering = ['date_joined']

    def __str__(self):
        return self.username

    def get_user_email(self):
        return self.email
