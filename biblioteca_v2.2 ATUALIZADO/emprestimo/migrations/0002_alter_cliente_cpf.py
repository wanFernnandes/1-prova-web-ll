# Generated by Django 5.1.1 on 2024-10-18 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emprestimo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cpf',
            field=models.CharField(max_length=11, unique=True),
        ),
    ]
