# Generated by Django 5.0.3 on 2024-05-28 09:07

import django.db.models.deletion
import galv.models.utils
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('galv', '0028_localstoragequota'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lab',
            name='s3_access_key',
        ),
        migrations.RemoveField(
            model_name='lab',
            name='s3_bucket_name',
        ),
        migrations.RemoveField(
            model_name='lab',
            name='s3_custom_domain',
        ),
        migrations.RemoveField(
            model_name='lab',
            name='s3_location',
        ),
        migrations.RemoveField(
            model_name='lab',
            name='s3_secret_key',
        ),
        migrations.RemoveField(
            model_name='observedfile',
            name='storage_class_name',
        ),
        migrations.RemoveField(
            model_name='parquetpartition',
            name='storage_class_name',
        ),
        migrations.AddField(
            model_name='observedfile',
            name='_storage_content_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
        migrations.AddField(
            model_name='observedfile',
            name='_storage_object_id',
            field=models.UUIDField(null=True),
        ),
        migrations.AddField(
            model_name='parquetpartition',
            name='_storage_content_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
        migrations.AddField(
            model_name='parquetpartition',
            name='_storage_object_id',
            field=models.UUIDField(null=True),
        ),
        migrations.CreateModel(
            name='AdditionalS3StorageType',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('id', galv.models.utils.UUIDFieldLD(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.TextField(blank=True, null=True)),
                ('enabled', models.BooleanField(default=True, help_text='Whether this storage type is enabled for writing to')),
                ('quota', models.BigIntegerField(help_text='Maximum storage capacity in bytes')),
                ('priority', models.SmallIntegerField(default=0, help_text='Priority for storage allocation. Higher values are higher priority.')),
                ('bucket_name', models.TextField(blank=True, help_text='Name of the S3 bucket to store files in', null=True)),
                ('location', models.TextField(blank=True, help_text='Directory within the S3 bucket to store files in', null=True)),
                ('access_key', models.TextField(blank=True, help_text='Access key for the S3 bucket', null=True)),
                ('secret_key', models.TextField(blank=True, help_text='Secret key for the S3 bucket', null=True)),
                ('custom_domain', models.TextField(blank=True, help_text='Custom domain for the S3 bucket.', null=True)),
                ('lab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='storage_%(class)s', to='galv.lab')),
            ],
            options={
                'abstract': False,
                'unique_together': {('lab', 'priority')},
            },
        ),
        migrations.CreateModel(
            name='GalvStorageType',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('id', galv.models.utils.UUIDFieldLD(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.TextField(blank=True, null=True)),
                ('enabled', models.BooleanField(default=True, help_text='Whether this storage type is enabled for writing to')),
                ('quota', models.BigIntegerField(help_text='Maximum storage capacity in bytes')),
                ('priority', models.SmallIntegerField(default=0, help_text='Priority for storage allocation. Higher values are higher priority.')),
                ('lab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='storage_%(class)s', to='galv.lab')),
            ],
            options={
                'abstract': False,
                'unique_together': {('lab', 'priority')},
            },
        ),
        migrations.DeleteModel(
            name='LocalStorageQuota',
        ),
    ]
