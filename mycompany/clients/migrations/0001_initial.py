# Generated by Django 4.1.1 on 2022-09-14 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('Mr', 'Mr'), ('Ms', 'Ms'), ('Mrs', 'Mrs')], max_length=3)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
                ('martial_status', models.CharField(choices=[('Single', 'Single'), ('Married', 'Married'), ('Other', 'Other')], max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('phone_no', models.IntegerField()),
                ('address_1', models.CharField(max_length=200)),
                ('address_2', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('zipcode', models.IntegerField()),
                ('years_present', models.CharField(choices=[('0-1 years', '0-1 years'), ('1-2 years', '1-2 years'), ('2-3 years', '2-3 years'), ('3-4 years', '3-4 years'), ('5+ years', '5+ years')], max_length=15)),
            ],
        ),
    ]
