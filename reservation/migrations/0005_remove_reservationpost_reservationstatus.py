# Generated by Django 3.1.1 on 2020-11-23 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("reservation", "0004_auto_20201123_1209"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="reservationpost",
            name="reservationstatus",
        ),
    ]