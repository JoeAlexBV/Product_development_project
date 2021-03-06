# Generated by Django 2.1.2 on 2018-10-18 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('field_type', models.CharField(choices=[('Text', 'Text'), ('Number', 'Number'), ('Date', 'Date'), ('Enum', 'Enum')], max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Risk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('risk_type', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='field',
            name='risk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fieldz', to='api.Risk'),
        ),
    ]
