# Generated by Django 4.0.5 on 2022-07-28 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wire_rope_hoist', '0003_alter_wireropehoist_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='wireropehoist',
            name='pdf_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
