# Generated by Django 2.2.4 on 2020-11-12 05:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_reg_app', '0003_auto_20201109_2143'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='hashpw',
            new_name='password',
        ),
    ]
