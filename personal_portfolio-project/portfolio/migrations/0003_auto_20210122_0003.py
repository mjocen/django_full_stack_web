# Generated by Django 3.1.5 on 2021-01-22 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_project_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(),
        ),
    ]
