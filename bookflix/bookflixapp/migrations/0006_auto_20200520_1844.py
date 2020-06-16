# Generated by Django 3.0.6 on 2020-05-20 21:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookflixapp', '0005_auto_20200520_1756'),
    ]

    operations = [
        migrations.CreateModel(
            name='PerfilCust',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bookflixapp.Usuario')),
            ],
        ),
        migrations.DeleteModel(
            name='Perfil',
        ),
    ]
