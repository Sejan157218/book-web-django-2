# Generated by Django 3.2 on 2022-08-25 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookApp', '0014_auto_20220825_2209'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.EmailField(default=None, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('Order Canceled', 'Order Canceled'), ('Order Completed', 'Order Completed'), ('On the way', 'On the way'), ('Order Received', 'Order Received'), ('Order Processing', 'Order Processing')], default='Order Received', max_length=100),
        ),
    ]
