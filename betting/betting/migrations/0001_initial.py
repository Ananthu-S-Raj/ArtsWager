# Generated by Django 3.2.7 on 2024-04-15 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='betting_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=150)),
                ('u_name', models.CharField(max_length=150)),
                ('u_email', models.CharField(max_length=150)),
                ('item', models.CharField(max_length=150)),
                ('district', models.CharField(max_length=150)),
                ('position', models.CharField(max_length=150)),
                ('prize', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='event_creators',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('phone_number', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=150)),
                ('venue', models.CharField(max_length=150)),
                ('date', models.CharField(max_length=150)),
                ('time', models.CharField(max_length=150)),
                ('gender', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='feedbacks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_id', models.CharField(max_length=255)),
                ('u_name', models.CharField(max_length=255)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='participant_register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('phone_number', models.CharField(max_length=120)),
                ('gender', models.CharField(max_length=120)),
                ('age', models.CharField(max_length=150)),
                ('category', models.CharField(max_length=150)),
                ('status', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=150)),
                ('chest_number', models.CharField(max_length=3, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='registered_events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chest_number', models.CharField(max_length=150)),
                ('p_id', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=120)),
                ('item', models.CharField(max_length=120)),
                ('venue', models.CharField(max_length=120)),
                ('time', models.CharField(max_length=120)),
                ('result', models.CharField(max_length=120)),
                ('status', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('item', models.CharField(max_length=120)),
                ('result', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='user_register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('phone_number', models.CharField(max_length=120)),
                ('password', models.CharField(max_length=120)),
            ],
        ),
    ]
