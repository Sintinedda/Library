# Generated by Django 5.1.2 on 2024-10-29 16:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('parution', models.DateField()),
                ('available', models.BooleanField(default=True)),
                ('category', models.CharField(choices=[('Livre', 'Livre'), ('Cd', 'Cd'), ('Dvd', 'Dvd'), ('Tabletop', 'Tabletop')], max_length=100)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Cd',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='gestion.item')),
                ('interpreter', models.CharField(max_length=100)),
            ],
            bases=('gestion.item',),
        ),
        migrations.CreateModel(
            name='Dvd',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='gestion.item')),
                ('realisator', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=100)),
            ],
            bases=('gestion.item',),
        ),
        migrations.CreateModel(
            name='Livre',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='gestion.item')),
                ('author', models.CharField(max_length=100)),
            ],
            bases=('gestion.item',),
        ),
        migrations.CreateModel(
            name='Tabletop',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='gestion.item')),
                ('creator', models.CharField(max_length=100)),
            ],
            bases=('gestion.item',),
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('blocked', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['lastname', 'firstname'],
                'unique_together': {('firstname', 'lastname')},
            },
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.item')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.member')),
            ],
            options={
                'unique_together': {('member', 'item', 'date')},
            },
        ),
    ]
