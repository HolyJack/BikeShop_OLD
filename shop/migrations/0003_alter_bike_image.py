# Generated by Django 4.2.1 on 2023-06-26 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_bike_image_alter_bike_has_basket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bike',
            name='image',
            field=models.ImageField(default='/staticfiles/shop/img/dummy_300x300_ffffff_cccccc.png', upload_to='uploads/products/'),
        ),
    ]
