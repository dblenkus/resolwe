# Generated by Django 2.2.6 on 2019-11-11 14:03

from django.db import migrations


def delete_obsolete_perms(apps, schema_editor):
    """Delete obsolete permissions from the database."""
    Permission = apps.get_model('auth', 'Permission')
    Permission.objects.filter(
        codename__in=[
            'add_collection',
            'add_entity',
            'download_collection',
            'download_entity',
            'download_data'
        ]
    ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('flow', '0041_remove_download_perm'),
    ]

    operations = [
        migrations.RunPython(delete_obsolete_perms)
    ]
