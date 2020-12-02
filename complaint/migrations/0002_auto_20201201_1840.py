# Generated by Django 3.1.1 on 2020-12-01 23:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("reservation", "0006_reservationpost_reservationstatus"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("complaint", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="complaint",
            name="issuer",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="issuer_id",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="complaint",
            name="receiver",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="receiver_id",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="complaint",
            name="reservation_post",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="reservation.reservationpost",
            ),
        ),
        migrations.AddField(
            model_name="complaint",
            name="status",
            field=models.CharField(
                choices=[
                    ("PENDING", "Pending"),
                    ("VALID", "Valid"),
                    ("INVALID", "Invlaid"),
                ],
                default="PENDING",
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="complaint",
            name="message",
            field=models.TextField(),
        ),
    ]