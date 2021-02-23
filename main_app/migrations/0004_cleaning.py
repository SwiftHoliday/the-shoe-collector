# Generated by Django 3.1.7 on 2021-02-23 02:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_shoe_sellers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cleaning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('cleaner', models.CharField(choices=[('R', 'Reshoevn8r'), ('SL', 'Sneaker Lab'), ('JM', 'Jason Markk')], default='R', max_length=2)),
                ('shoe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.shoe')),
            ],
        ),
    ]