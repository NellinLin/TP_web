# Generated by Django 2.1.7 on 2019-05-28 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0008_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='static/image/avatar.png', upload_to=''),
        ),
    ]