# Generated by Django 5.1.1 on 2024-10-20 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0006_rename_firstname_sign_firstname_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Login",
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
                ("username", models.CharField(max_length=122)),
                ("password", models.CharField(max_length=122)),
            ],
        ),
    ]
