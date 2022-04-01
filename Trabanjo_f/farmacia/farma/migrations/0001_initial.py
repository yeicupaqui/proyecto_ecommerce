# Generated by Django 4.0.2 on 2022-02-21 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField(unique=True)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField(unique=True)),
                ('nombre', models.CharField(max_length=40, unique=True)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=8)),
                ('especificaciones', models.TextField(blank=True, max_length=5000, null=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productos', to='farma.categoria')),
            ],
        ),
    ]
