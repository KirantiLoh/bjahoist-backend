# Generated by Django 4.0.5 on 2022-06-24 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wire_rope_hoist', '0002_wireropehoist_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wireropehoist',
            name='slug',
            field=models.SlugField(blank=True, default='', null=True),
        ),
    ]
