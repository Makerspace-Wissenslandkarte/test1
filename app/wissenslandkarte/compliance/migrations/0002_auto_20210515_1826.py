# Generated by Django 3.2.2 on 2021-05-15 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compliance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imprint',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='privacypolicy',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
