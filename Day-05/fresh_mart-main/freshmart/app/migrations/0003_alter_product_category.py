# Generated by Django 4.2.4 on 2023-08-02 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_alter_product_stock"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.CharField(
                choices=[
                    ("VEG", "Vegetable"),
                    ("BRD", "Bread"),
                    ("FR", "Fruits"),
                    ("JU", "Juice"),
                    ("TC", "Teacoffee"),
                    ("JAM", "Jam"),
                    ("SF", "SeaFood"),
                    ("FMT", "FreshMeats"),
                ],
                max_length=3,
            ),
        ),
    ]
