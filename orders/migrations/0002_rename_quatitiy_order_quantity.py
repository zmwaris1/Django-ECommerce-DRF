# Generated by Django 4.1.5 on 2023-01-28 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='quatitiy',
            new_name='quantity',
        ),
    ]
