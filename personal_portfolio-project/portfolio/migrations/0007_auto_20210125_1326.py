# Generated by Django 3.1.5 on 2021-01-25 13:26

from django.db import migrations
import markdownfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_auto_20210125_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='blurb',
            field=markdownfield.models.MarkdownField(default='Insert blurb here', max_length=250, rendered_field='blurb_rendered'),
        ),
    ]
