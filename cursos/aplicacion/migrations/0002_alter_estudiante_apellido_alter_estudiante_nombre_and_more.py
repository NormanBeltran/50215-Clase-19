# Generated by Django 4.2.5 on 2024-02-27 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='apellido',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='nombre',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='apellido',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='nombre',
            field=models.CharField(max_length=60),
        ),
    ]
