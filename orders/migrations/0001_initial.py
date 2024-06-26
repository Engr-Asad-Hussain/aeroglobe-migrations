# Generated by Django 5.0.6 on 2024-06-09 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Orders",
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
                ("destination", models.TextField(max_length=150)),
                ("destination_iata", models.TextField(max_length=15)),
                ("origin", models.TextField(max_length=150)),
                ("origin_iata", models.TextField(max_length=15)),
                ("type", models.TextField(max_length=30)),
                ("departure", models.DateField()),
                ("arrival", models.DateField()),
            ],
        ),
    ]
