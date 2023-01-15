# Generated by Django 4.1 on 2023-01-15 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_view', '0005_alter_library_book_avail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='library',
            name='book_avail',
            field=models.CharField(choices=[('in stock', 'available'), ('out of stock', 'unavailable')], default='out of stock', max_length=20),
        ),
    ]
