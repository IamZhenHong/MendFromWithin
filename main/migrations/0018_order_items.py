# Generated by Django 4.2.5 on 2024-02-04 03:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0017_alter_order_user_delete_customuser"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="items",
            field=models.ManyToManyField(through="main.CartItem", to="main.item"),
        ),
    ]
