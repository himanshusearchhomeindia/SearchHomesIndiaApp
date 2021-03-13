# Generated by Django 3.1.6 on 2021-03-03 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SHIApp', '0012_propertylist_searchname'),
    ]

    operations = [
        migrations.AddField(
            model_name='propertylist',
            name='SubPropType',
            field=models.CharField(choices=[('Plot', 'Plot'), ('Villa', 'Villa'), ('Apartment', 'Apartment'), ('Rowhouse', 'Rowhouse'), ('Farmhouse', 'Farmhouse')], default='', max_length=60),
        ),
    ]
