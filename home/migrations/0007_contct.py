# Generated by Django 3.2.9 on 2022-05-28 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0006_delete_contct'),
    ]

    operations = [
        migrations.CreateModel(
            name='contct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=100)),
            ],
        ),
    ]
