# Generated by Django 3.0.7 on 2020-07-29 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20200729_1750'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('total_price', models.IntegerField()),
                ('total_items', models.IntegerField()),
                ('img', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
