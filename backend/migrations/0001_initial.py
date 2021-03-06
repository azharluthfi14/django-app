# Generated by Django 3.1.1 on 2020-09-25 06:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PredResults',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fixed_acidity', models.FloatField()),
                ('volatile_acidity', models.FloatField()),
                ('citric_acid', models.FloatField()),
                ('residual_sugar', models.FloatField()),
                ('chlorides', models.FloatField()),
                ('free_sulfur_dioxide', models.FloatField()),
                ('total_sulfur_dioxide', models.FloatField()),
                ('density', models.FloatField()),
                ('pH', models.FloatField()),
                ('sulphates', models.FloatField()),
                ('alcohol', models.FloatField()),
                ('classification', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pict_user')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
