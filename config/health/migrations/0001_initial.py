# Generated by Django 5.0.1 on 2024-01-19 18:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Health',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Рост')),
                ('weight', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Вес')),
                ('heart_rate', models.IntegerField(blank=True, null=True, verbose_name='Пульс')),
                ('user_profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.userprofile', verbose_name='Профиль пользователя')),
            ],
            options={
                'verbose_name': 'Здоровье пользователя',
                'verbose_name_plural': 'Здоровье пользователей',
            },
        ),
    ]