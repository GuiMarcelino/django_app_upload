# Generated by Django 3.2.5 on 2021-07-18 22:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='merchant',
            old_name='description',
            new_name='name',
        ),
    ]
