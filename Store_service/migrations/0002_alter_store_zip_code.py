# Generated by Django 5.1 on 2024-08-29 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store_service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='zip_code',
            field=models.IntegerField(blank=True),
        ),
    ]
