# Generated by Django 3.2 on 2022-08-25 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookApp', '0006_remove_cartproduct_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartproduct',
            name='user',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
