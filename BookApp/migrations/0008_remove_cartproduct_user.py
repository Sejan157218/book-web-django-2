# Generated by Django 3.2 on 2022-08-25 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BookApp', '0007_cartproduct_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartproduct',
            name='user',
        ),
    ]