# Generated by Django 3.1.6 on 2021-02-18 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SHIApp', '0005_auto_20210218_1844'),
    ]

    operations = [
        migrations.AddField(
            model_name='propertylist',
            name='Master_Plan',
            field=models.ImageField(blank=True, default='', upload_to='static/Master_Plans'),
        ),
        migrations.AddField(
            model_name='propertylist',
            name='Video',
            field=models.FileField(blank=True, default='', upload_to='static/Videos'),
        ),
    ]