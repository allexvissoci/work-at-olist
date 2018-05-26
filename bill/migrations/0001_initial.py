# Generated by Django 2.0.5 on 2018-05-26 02:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('record', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('call_duration', models.DurationField()),
                ('call_price', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('call_end_record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='call_end_record', to='record.Record')),
                ('call_start_record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='call_start_record', to='record.Record')),
            ],
        ),
    ]
