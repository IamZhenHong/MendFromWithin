# Generated by Django 4.2.5 on 2024-02-03 18:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0013_order_order_summary"),
    ]

    operations = [
        migrations.AddField(
            model_name="cartitem",
            name="session_key",
            field=models.CharField(blank=True, max_length=100),
        ),
    ]