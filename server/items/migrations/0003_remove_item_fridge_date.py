# Generated by Django 5.1.3 on 2024-11-17 03:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_remove_item_status_category_good_for'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='fridge_date',
        ),
    ]