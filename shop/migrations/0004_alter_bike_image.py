# Generated by Django 4.2.1 on 2023-06-27 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_bike_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bike',
            name='image',
            field=models.ImageField(default='/staticfiles/shop/img/dummy_240x300_ffffff_cccccc.png', upload_to='uploads/products/'),
        ),
    ]
