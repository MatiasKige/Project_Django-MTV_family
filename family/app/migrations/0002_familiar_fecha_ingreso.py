# Generated by Django 4.2.2 on 2023-06-14 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='familiar',
            name='fecha_ingreso',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
