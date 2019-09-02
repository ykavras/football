# Generated by Django 2.2.4 on 2019-09-02 10:18

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import football.utils.file_rename


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReferenceCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, unique=True, verbose_name='Kod')),
                ('is_used', models.BooleanField(verbose_name='Kullanılma Durumu')),
            ],
            options={
                'verbose_name': 'Referans Kodu',
                'verbose_name_plural': 'Referans Kodları',
            },
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Adı')),
                ('last_name', models.CharField(max_length=20, verbose_name='Soyadı')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='E-mail')),
                ('phone', models.CharField(max_length=15, unique=True, validators=[django.core.validators.RegexValidator(message='Telefon numarası "+999999999" formatında olmalı.', regex='^\\+?1?\\d{9,15}$')], verbose_name='Telefon Numarası')),
                ('address', models.CharField(max_length=1000, verbose_name='Adres')),
                ('id_photo', models.ImageField(upload_to=football.utils.file_rename.PathAndRename('application/id_photos/'), verbose_name='Kimlik Fotoğrafı')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('reference_code', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='application', to='apply.ReferenceCode', verbose_name='Referans Kodu')),
            ],
            options={
                'verbose_name': 'Başvuru',
                'verbose_name_plural': 'Başvurular',
            },
        ),
    ]