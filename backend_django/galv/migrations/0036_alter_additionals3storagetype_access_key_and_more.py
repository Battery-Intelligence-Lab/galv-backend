# Generated by Django 5.0.3 on 2024-06-11 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galv', '0035_additionals3storagetype_region_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additionals3storagetype',
            name='access_key',
            field=models.TextField(blank=True, help_text='Access key for the S3 bucket', null=True),
        ),
        migrations.AlterField(
            model_name='additionals3storagetype',
            name='region_name',
            field=models.TextField(blank=True, default='eu-west-2', help_text='Region for the S3 bucket. Only one of custom domain or region should be set.'),
        ),
    ]