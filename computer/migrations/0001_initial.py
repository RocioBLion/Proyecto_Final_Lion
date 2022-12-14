# Generated by Django 4.1.3 on 2022-11-17 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=20)),
                ('model', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=40)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(null=True, upload_to='products')),
            ],
        ),
    ]
# Generated by Django 4.1.3 on 2022-11-15 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=20)),
                ('model', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=40)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
