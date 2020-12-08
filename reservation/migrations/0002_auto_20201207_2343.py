# Generated by Django 3.1.1 on 2020-12-08 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='notificationstatus',
            field=models.IntegerField(choices=[(1, 'ACCEPT'), (2, 'REJECT'), (3, 'PENDING'), (4, 'EXPIRED')], default=3),
        ),
        migrations.AlterField(
            model_name='reservationpost',
            name='reservationstatus',
            field=models.IntegerField(choices=[(1, 'accept'), (2, 'reject'), (3, 'pending'), (4, 'expired')], default=3),
        ),
    ]