# Generated by Django 4.0.1 on 2022-02-07 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pendaftaran', '0002_alter_user_nim'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='prodi',
            field=models.CharField(choices=[('Sistem Informasi', 'Sistem Informasi'), ('Teknik Informatika', 'Teknik Informatika'), ('Matematika', 'Matematika'), ('Manaajemen', 'Manajemen'), ('Ekonomi Pembangunan', 'Ekonomi Pembangunan'), ('Pendidikan Guru Sekolah Dasar', 'Pendidikan Guru Sekolah Dasar')], default='Sistem Informasi', max_length=35),
        ),
    ]
