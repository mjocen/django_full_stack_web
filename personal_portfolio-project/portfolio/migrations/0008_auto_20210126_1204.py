# Generated by Django 3.1.5 on 2021-01-26 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_auto_20210125_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, upload_to='portfolio/images/'),
        ),
    ]
