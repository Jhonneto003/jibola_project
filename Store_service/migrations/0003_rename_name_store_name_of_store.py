# Generated by Django 5.1 on 2024-09-01 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Store_service', '0002_alter_store_zip_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='store',
            old_name='name',
            new_name='name_of_store',
        ),
    ]
