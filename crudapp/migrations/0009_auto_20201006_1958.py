# Generated by Django 3.1.1 on 2020-10-06 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0008_auto_20201006_1934'),
    ]

    operations = [
        
        migrations.AlterField(
            model_name='contact',
            name='display_pictur',
            field=models.ImageField(blank=True, default='crudapp/templates/media/static/telechargement.jpg', upload_to='crudapp/templates/media/static/'),
        ),
    ]