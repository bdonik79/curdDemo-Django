# Generated by Django 3.0.7 on 2020-06-10 06:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fullname', models.CharField(max_length=100)),
                ('emp_code', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.Position')),
            ],
        ),
    ]