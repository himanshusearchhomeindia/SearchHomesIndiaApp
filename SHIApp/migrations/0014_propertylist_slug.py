# Generated by Django 3.1.6 on 2021-03-03 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SHIApp', '0013_propertylist_subproptype'),
    ]

    operations = [
        migrations.AddField(
            model_name='propertylist',
            name='slug',
            field=models.CharField(default='', max_length=550, null=True),
        ),
    ]
