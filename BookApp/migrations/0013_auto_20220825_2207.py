# Generated by Django 3.2 on 2022-08-25 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BookApp', '0012_auto_20220825_2156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='book',
        ),
        migrations.RemoveField(
            model_name='order',
            name='date',
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_status',
        ),
    ]
