from django.db import models
from django.urls import reverse_lazy


class Task(models.Model):
    LEVELS = (
        ('!', 'Важно!'),
        ('!!', 'Очень важно!!'),
        ('!!!', 'Умри, но сделай!!!'),
    )

    name = models.CharField(
        max_length=64,
        db_index=True,
        verbose_name='Заголовок'
    )
    body = models.TextField(
        blank=True,
        null=True,
        verbose_name='Описание'
    )
    created = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    importance = models.CharField(
        max_length=16,
        choices=LEVELS,
        null=True,
        blank=True,
        verbose_name='Степень важности'
    )

    class Meta:
        ordering = ['-id']
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return f'Задача "{self.name}".'
