# Generated by Django 5.1.1 on 2024-11-11 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('email', models.CharField(max_length=100)),
                ('senha', models.CharField(default='1234', max_length=100)),
            ],
        ),
    ]