# Generated by Django 5.0.2 on 2024-04-10 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galv', '0013_remove_parquetpartition_auth_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lab',
            name='s3_custom_domain',
            field=models.TextField(blank=True, help_text='Custom domain for the S3 bucket. Probably region-name.s3.amazonaws.com. Only one of custom domain or region should be set.', null=True),
        ),
        migrations.AlterField(
            model_name='lab',
            name='s3_region',
            field=models.TextField(blank=True, help_text='Region for the S3 bucket. Only one of custom domain or region should be set.', null=True),
        ),
    ]