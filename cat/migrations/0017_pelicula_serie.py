# Generated by Django 2.2.4 on 2019-08-30 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cat', '0016_remove_pelicula_serie'),
    ]

    operations = [
        migrations.AddField(
            model_name='pelicula',
            name='serie',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cat.Serie'),
        ),
    ]
