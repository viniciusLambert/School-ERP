# Generated by Django 2.2.2 on 2019-06-20 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gerenciaTurmas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='disciplinas',
            name='cargaHoraria',
            field=models.IntegerField(blank=True, null=True, verbose_name='cargaHoraria'),
        ),
    ]
