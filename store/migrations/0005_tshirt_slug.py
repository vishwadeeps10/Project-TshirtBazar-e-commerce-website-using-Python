# Generated by Django 3.1.2 on 2020-10-31 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20201031_1133'),
    ]

    operations = [
        migrations.AddField(
            model_name='tshirt',
            name='slug',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]
