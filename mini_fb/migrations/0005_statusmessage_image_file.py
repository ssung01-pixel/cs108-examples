# Generated by Django 2.2.7 on 2021-03-29 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mini_fb', '0004_auto_20210324_2225'),
    ]

    operations = [
        migrations.AddField(
            model_name='statusmessage',
            name='image_file',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
