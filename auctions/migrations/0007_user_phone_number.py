# Generated by Django 4.0.3 on 2022-10-05 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_remove_user_phone_number_remove_winner_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]
