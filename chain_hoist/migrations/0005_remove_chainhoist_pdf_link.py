# Generated by Django 4.0.5 on 2022-07-30 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chain_hoist', '0004_chainhoist_pdf_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chainhoist',
            name='pdf_link',
        ),
    ]