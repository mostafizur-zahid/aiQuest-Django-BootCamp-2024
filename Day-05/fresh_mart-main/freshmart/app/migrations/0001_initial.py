# Generated by Django 4.2.3 on 2023-07-24 16:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("locality", models.CharField(max_length=200)),
                ("city", models.CharField(max_length=50)),
                ("zipcode", models.IntegerField()),
                (
                    "district",
                    models.CharField(
                        choices=[
                            ("Dhaka", "Dhaka"),
                            ("Chattogram", "Chattogram"),
                            ("Khulna", "Khulna"),
                            ("Rajshahi", "Rajshahi"),
                            ("Shylet", "Shylet"),
                            ("Rangpur", "Rangpur"),
                            ("Barishal", "Barishal"),
                            ("Maymansing", "Maymansing"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("selling_price", models.FloatField()),
                ("discounted_price", models.FloatField()),
                ("basic_description", models.TextField()),
                ("description", models.TextField()),
                ("additional_information", models.TextField()),
                ("food_brand", models.CharField(max_length=100)),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("VEG", "Vegetable"),
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
                ("stock", models.BooleanField()),
                ("product_1_image", models.ImageField(upload_to="productimg")),
                ("product_2_image", models.ImageField(upload_to="productimg")),
                ("product_3_image", models.ImageField(upload_to="productimg")),
                ("product_4_image", models.ImageField(upload_to="productimg")),
            ],
        ),
        migrations.CreateModel(
            name="OrderPlaced",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.PositiveIntegerField(default=1)),
                ("ordered_date", models.DateTimeField(auto_now_add=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Accepted", "Accepted"),
                            ("Packed", "Packed"),
                            ("On The Way", "On The Way"),
                            ("Delivered", "Delivered"),
                            ("Cancel", "Cancel"),
                        ],
                        default="Pending",
                        max_length=50,
                    ),
                ),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.customer"
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.product"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Cart",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.PositiveIntegerField(default=1)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.product"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]