# Generated by Django 3.1.6 on 2021-02-17 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SHIApp', '0002_auto_20210217_1619'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='propertylist',
            name='Area_in_sqft',
        ),
        migrations.AlterField(
            model_name='propertylist',
            name='Avaliable_For',
            field=models.CharField(default='Sale', max_length=50),
        ),
        migrations.AlterField(
            model_name='propertylist',
            name='BHK',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='propertylist',
            name='Location',
            field=models.CharField(choices=[('Bangalore', 'Bangalore'), ('Mumbai', 'Mumbai'), ('Delhi', 'Delhi'), ('Punjab', 'Punjab')], max_length=50),
        ),
        migrations.AlterField(
            model_name='propertylist',
            name='PropertyName',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='propertylist',
            name='PropertyStatus',
            field=models.CharField(choices=[('Ongoing', 'Ongoing'), ('Completed', 'Completed'), ('Ready to move', 'Ready to move')], max_length=50),
        ),
        migrations.AlterField(
            model_name='propertylist',
            name='Property_Description',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='propertylist',
            name='Property_Price',
            field=models.CharField(max_length=50),
        ),
    ]
