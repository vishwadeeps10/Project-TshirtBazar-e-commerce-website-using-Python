# Generated by Django 3.1.2 on 2020-11-01 05:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0007_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_status', models.CharField(choices=[('PENDING', 'Pending'), ('PLACED', 'Placed'), ('CANCELED', 'Canceled'), ('COMPLETED', 'Completed ')], max_length=15)),
                ('payment_method', models.CharField(choices=[('COD', 'Cod'), ('ONLINE', 'Online')], max_length=15)),
                ('shipping_address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=10)),
                ('total', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('payment_status', models.CharField(default='FAILED', max_length=15)),
                ('payment_id', models.CharField(max_length=60)),
                ('payment_request_id', models.CharField(max_length=60, unique=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.orders')),
            ],
        ),
        migrations.CreateModel(
            name='Order_items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.orders')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.sizevariant')),
                ('tshirt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.tshirt')),
            ],
        ),
    ]