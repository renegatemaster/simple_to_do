# Generated by Django 3.2.3 on 2023-07-19 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=64, verbose_name='Заголовок')),
                ('body', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('deadline', models.DateTimeField(blank=True, null=True)),
                ('importance', models.CharField(blank=True, choices=[('!', 'Важно!'), ('!!', 'Очень важно!!'), ('!!!', 'Умри, но сделай!!!')], max_length=16, null=True, verbose_name='Степень важности')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
                'ordering': ['-id'],
            },
        ),
    ]