# Generated by Django 4.1.2 on 2022-11-23 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accessorie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='accessorie',
            name='image',
            field=models.ImageField(null=True, upload_to='products'),
        ),
        migrations.AlterField(
            model_name='accessorie',
            name='description',
            field=models.TextField(),
        ),
    ]
