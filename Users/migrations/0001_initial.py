# Generated by Django 2.2.2 on 2019-06-20 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('lastName', models.CharField(max_length=255, verbose_name='lastName')),
                ('cpf', models.CharField(blank=True, max_length=15, null=True, verbose_name='cpf')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email')),
                ('password', models.CharField(max_length=255, verbose_name='password')),
                ('birthdate', models.DateField(blank=True, null=True, verbose_name='birthdate')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='phone')),
                ('type', models.CharField(blank=True, max_length=20, null=True, verbose_name='type')),
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
                'db_table': 'users',
                'ordering': ['name'],
            },
        ),
    ]
