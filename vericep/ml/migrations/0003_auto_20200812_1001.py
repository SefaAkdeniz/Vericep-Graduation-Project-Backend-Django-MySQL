# Generated by Django 3.0.8 on 2020-08-12 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ml', '0002_auto_20200811_1117'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mlmodel',
            options={'verbose_name': 'Machine Learning Model', 'verbose_name_plural': 'Machine Learning Model'},
        ),
        migrations.CreateModel(
            name='ModelInput',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typed', models.CharField(choices=[('Str', 'String'), ('Int', 'İnteger'), ('Db', 'Double')], max_length=20)),
                ('description', models.TextField(verbose_name='Giriş Açıklaması')),
                ('model_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ml.MlModel', verbose_name='ML Modeli')),
            ],
        ),
    ]