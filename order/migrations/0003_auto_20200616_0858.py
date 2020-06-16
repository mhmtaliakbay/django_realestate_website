# Generated by Django 3.0.4 on 2020-06-16 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_order_orderproperty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderproperty',
            name='status',
            field=models.CharField(choices=[('Canceled', 'Canceled'), ('Accepted', 'Accepted'), ('New', 'New')], default='New', max_length=10),
        ),
    ]
