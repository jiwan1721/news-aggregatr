# Generated by Django 4.0.4 on 2022-05-09 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsAggre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_headline', models.CharField(max_length=300)),
                ('href_link', models.URLField(max_length=300)),
                ('image_link', models.URLField(max_length=300)),
                ('news_category', models.CharField(choices=[('P', 'Politics'), ('S', 'Sports'), ('H', 'Health')], max_length=1)),
            ],
        ),
    ]
