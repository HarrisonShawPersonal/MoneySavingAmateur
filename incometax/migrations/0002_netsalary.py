# Generated by Django 5.0.4 on 2024-04-16 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incometax', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NetSalary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('net_salary', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
            ],
        ),
    ]
