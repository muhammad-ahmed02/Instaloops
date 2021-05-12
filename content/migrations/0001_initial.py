# Generated by Django 3.2.2 on 2021-05-12 12:14

import content.models
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
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Site/Banners/')),
                ('link', models.URLField(blank=True, null=True)),
                ('order_no', models.PositiveIntegerField(default=content.models.getIncreasingBannerOrder)),
            ],
        ),
        migrations.CreateModel(
            name='Consumer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(blank=True, null=True, upload_to='Consumer/pic/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Influencer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_budget', models.PositiveIntegerField(default=0)),
                ('max_budget', models.PositiveIntegerField()),
                ('pic', models.ImageField(blank=True, null=True, upload_to='Influencer/Pic/')),
                ('banner', models.ImageField(blank=True, null=True, upload_to='Influencer/Banner/')),
                ('bio', models.CharField(blank=True, max_length=64, null=True)),
                ('about', models.TextField()),
                ('rating', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Niche',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=56)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=128, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('is_public', models.BooleanField(default=True)),
                ('consumer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='content.consumer')),
                ('influencer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.influencer')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_created=True)),
                ('accepted_amount', models.FloatField()),
                ('is_accepted', models.BooleanField(default=False)),
                ('has_responded', models.BooleanField(default=False)),
                ('consumer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.consumer')),
                ('influencer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.influencer')),
            ],
        ),
        migrations.AddField(
            model_name='influencer',
            name='niche',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.niche'),
        ),
        migrations.AddField(
            model_name='influencer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
