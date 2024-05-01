# Generated by Django 5.0.4 on 2024-04-30 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_user_phone_number_alter_user_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='permission',
            old_name='codename',
            new_name='code_name',
        ),
        migrations.RenameField(
            model_name='role',
            old_name='code',
            new_name='code_name',
        ),
        migrations.RemoveField(
            model_name='permission',
            name='role',
        ),
        migrations.RemoveField(
            model_name='role',
            name='user',
        ),
        migrations.AddField(
            model_name='role',
            name='permission',
            field=models.ManyToManyField(to='user.permission'),
        ),
    ]
