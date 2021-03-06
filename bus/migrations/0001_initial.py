# Generated by Django 3.2 on 2021-05-21 06:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('busNum', models.IntegerField()),
                ('busAgencyName', models.CharField(max_length=64)),
                ('busType', models.CharField(max_length=16)),
                ('seats', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BusStop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StopName', models.CharField(max_length=64)),
                ('StopLocation', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='NameForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=161)),
                ('custfName', models.CharField(max_length=64)),
                ('custlName', models.CharField(max_length=64)),
                ('custEmail', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('duration', models.IntegerField()),
                ('cost', models.IntegerField()),
                ('busInfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bus.bus')),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrivalsSchedule', to='bus.busstop')),
                ('origin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departuresSchedule', to='bus.busstop')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passenger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bus.passenger')),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bus.schedule')),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrivalsRoutes', to='bus.busstop')),
                ('origin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departuresRoutes', to='bus.busstop')),
            ],
        ),
        migrations.AddField(
            model_name='passenger',
            name='buses',
            field=models.ManyToManyField(blank=True, related_name='passengers', to='bus.Schedule'),
        ),
    ]
