# Generated by Django 5.1.3 on 2024-11-23 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Camiseta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('quantidade', models.PositiveIntegerField()),
                ('preco', models.DecimalField(decimal_places=2, max_digits=6)),
                ('img', models.URLField()),
                ('descricao', models.TextField(blank=True)),
            ],
        ),
    ]
