# Generated by Django 5.0.2 on 2024-04-11 16:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_responder'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(choices=[('Новичок', 'Игра с новичком'), ('Профи', 'Игра с профи'), ('Любительская игра', 'Любительская игра'), ('Турнир', 'Турнир')], default='Новичок', max_length=20, verbose_name='Тип игры'),
        ),
        migrations.CreateModel(
            name='ExpectedGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]