# Generated by Django 4.1.2 on 2022-12-23 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel_destinations', '0003_traveldestinations_destination_subheading'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TravelDestinations',
            new_name='Destinations',
        ),
        migrations.AlterModelOptions(
            name='destinations',
            options={'ordering': ['-created_on']},
        ),
    ]