# Generated by Django 4.1.7 on 2023-05-19 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0003_alter_product_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('starts', models.IntegerField()),
            ],
            options={
                'db_table': 'app1_product',
            },
        ),
    ]
