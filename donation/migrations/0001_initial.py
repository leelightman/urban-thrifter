# Generated by Django 3.1.1 on 2020-11-18 15:15

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import places.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ResourcePost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('quantity', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('dropoff_time_1', models.DateTimeField(default=django.utils.timezone.now)),
                ('dropoff_time_2', models.DateTimeField(blank=True, null=True)),
                ('dropoff_time_3', models.DateTimeField(blank=True, null=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('dropoff_location', places.fields.PlacesField(blank=True, max_length=255, null=True)),
                ('resource_category', models.CharField(choices=[('FOOD', 'Food'), ('MDCL', 'Medical/ PPE'), ('CLTH', 'Clothing/ Covers'), ('ELEC', 'Electronics'), ('OTHR', 'Others')], max_length=100)),
                ('image', models.ImageField(blank=True, default='donation-pics/default.jpg', upload_to='donation-pics')),
                ('status', models.CharField(choices=[('AVAILABLE', 'Available'), ('RESERVED', 'Reserved'), ('PENDING', 'Pending'), ('CLOSED', 'Closed')], default='Available', max_length=100)),
                ('donor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
