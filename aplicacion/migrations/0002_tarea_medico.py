# Generated by Django 4.2.3 on 2023-07-21 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarea',
            name='medico',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
    ]