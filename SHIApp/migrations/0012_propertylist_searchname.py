# Generated by Django 3.1.6 on 2021-02-22 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SHIApp', '0011_auto_20210221_1206'),
    ]

    operations = [
        migrations.AddField(
            model_name='propertylist',
            name='SearchName',
            field=models.CharField(default='', max_length=100),
        ),
    ]