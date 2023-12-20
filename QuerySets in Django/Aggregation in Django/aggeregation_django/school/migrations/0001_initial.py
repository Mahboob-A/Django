# Generated by Django 4.2.2 on 2023-09-05 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('roll', models.IntegerField()),
                ('grade', models.CharField(max_length=5)),
                ('city', models.CharField(max_length=30)),
                ('marks', models.DecimalField(decimal_places=2, max_digits=5)),
                ('admission_date', models.DateTimeField()),
                ('pass_date', models.DateField()),
            ],
        ),
    ]