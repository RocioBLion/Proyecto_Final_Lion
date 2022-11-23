# Generated by Django 4.1.2 on 2022-11-23 05:01

import ckeditor.fields
import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('computer', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='computer',
            options={'ordering': ['-created_at']},
        ),
        migrations.AddField(
            model_name='computer',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='computer',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='computer'),
        ),
        migrations.AddField(
            model_name='computer',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='computer',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='computer',
            name='brand',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='computer',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='computer',
            name='model',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterUniqueTogether(
            name='computer',
            unique_together={('brand', 'model')},
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(validators=[django.core.validators.MinLengthValidator(10, 'The comment must be longer than 10 characters')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('computer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='computer.computer')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='computer',
            name='comments',
            field=models.ManyToManyField(related_name='comments_owned', through='computer.Comment', to=settings.AUTH_USER_MODEL),
        ),
    ]
