# Generated by Django 3.0.4 on 2020-03-27 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0005_deck_add_image_and_remove_field'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deck',
            old_name='deck_name',
            new_name='type',
        ),
    ]
