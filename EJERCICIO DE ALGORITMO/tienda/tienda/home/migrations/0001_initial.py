# Generated by Django 3.2.6 on 2021-08-21 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=500)),
                ('status', models.BooleanField(default=True)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=6)),
                ('stock', models.IntegerField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.categoria')),
                ('marca', models.ManyToManyField(blank=True, null=True, to='home.marca')),
            ],
        ),
    ]