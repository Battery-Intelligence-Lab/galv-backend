# Generated by Django 5.0.2 on 2024-04-10 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galv', '0012_parquetpartition_storage_class_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parquetpartition',
            name='auth_key',
        ),
    ]