# Generated by Django 5.1.1 on 2024-11-11 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gerencialivro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='quantidade',
            field=models.IntegerField(default=0),
        ),
    ]
