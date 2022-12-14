# Generated by Django 3.2 on 2022-08-26 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookApp', '0020_alter_order_order_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='quantity',
        ),
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('Order Canceled', 'Order Canceled'), ('Order Completed', 'Order Completed'), ('Order Received', 'Order Received'), ('Order Processing', 'Order Processing'), ('On the way', 'On the way')], default='Order Received', max_length=100),
        ),
    ]
