# Generated by Django 4.1.7 on 2023-05-19 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0004_product1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='starts',
            new_name='rating',
        ),
        migrations.RenameField(
            model_name='product1',
            old_name='starts',
            new_name='rating',
        ),
    ]
