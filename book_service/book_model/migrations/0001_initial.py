# Generated by Django 4.1.3 on 2023-03-27 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barcode', models.CharField(max_length=200)),
                ('book_category', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=100)),
                ('availability', models.CharField(max_length=15)),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=9)),
                ('quantity', models.IntegerField()),
                ('author', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('publisher', models.CharField(max_length=200)),
                ('publication_date', models.DateField()),
            ],
        ),
    ]