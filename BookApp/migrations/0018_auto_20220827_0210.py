# Generated by Django 3.2 on 2022-08-26 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookApp', '0017_rename_quantity_order_totalquantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('Order Canceled', 'Order Canceled'), ('Order Received', 'Order Received'), ('Order Completed', 'Order Completed'), ('Order Processing', 'Order Processing'), ('On the way', 'On the way')], default='Order Received', max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='order',
            name='totalQuantity',
            field=models.PositiveBigIntegerField(default=None),
        ),
    ]
