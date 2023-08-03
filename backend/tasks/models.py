from django.db import models
from django.utils.translation import gettext_lazy as _


class Task(models.Model):
    LEVELS = (
        ('!', 'Важно!'),
        ('!!', 'Очень важно!!'),
        ('!!!', 'Умри, но сделай!!!'),
    )

    name = models.CharField(
        max_length=64,
        db_index=True,
        verbose_name=_('Заголовок'),
    )
    body = models.TextField(
        blank=True,
        null=True,
        verbose_name=_('Описание'),
    )
    created = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    importance = models.CharField(
        max_length=16,
        choices=LEVELS,
        null=True,
        blank=True,
        verbose_name=_('Степень важности'),
    )

    class Meta:
        ordering = ['-importance']
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return f'Задача "{self.name}".'


class SubTask(models.Model):
    text = models.CharField(max_length=100)
    task = models.ForeignKey(
        Task,
        related_name='subtasks',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Подзадача'
        verbose_name_plural = 'Подзадачи'

    def __str__(self):
        return self.text[:15]
