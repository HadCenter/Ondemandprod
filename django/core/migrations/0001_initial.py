# Generated by Django 2.1.5 on 2022-09-12 11:05

import core.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountsAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('email', models.CharField(max_length=254, unique=True)),
                ('username', models.CharField(max_length=255)),
                ('is_active', models.IntegerField()),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('role', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'accounts_account',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AnomaliesEdiFileAnnuaire',
            fields=[
                ('id_anomalie', models.AutoField(primary_key=True, serialize=False)),
                ('label', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'anomalies_edi_file_annuaire',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InterventionAdmin',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('execution_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'intervention_admin',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_client', models.CharField(blank=True, max_length=200, null=True)),
                ('nom_client', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('archived', models.BooleanField(default=False)),
                ('id_salesforce', models.CharField(blank=True, max_length=200, null=True)),
                ('token', models.CharField(blank=True, max_length=250, null=True)),
                ('token_for_flux', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EDIfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=core.models.upload_to)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default='En attente', max_length=200)),
                ('wrong_commands', models.CharField(default='_', max_length=200)),
                ('validated_orders', models.CharField(default='_', max_length=200)),
                ('archived', models.BooleanField(default=False)),
                ('cliqued', models.BooleanField(default=False)),
                ('sendedToUrbantz', models.BooleanField(default=False)),
                ('number_correct_commands', models.IntegerField(default=0)),
                ('number_wrong_commands', models.IntegerField(default=0)),
                ('client', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='files', to='core.Client')),
            ],
        ),
        migrations.CreateModel(
            name='HistoryAnomaliesEdiFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('execution_time', models.DateTimeField(auto_now=True)),
                ('number_of_anomalies', models.IntegerField(blank=True, null=True)),
                ('anomalie', models.ForeignKey(blank=True, db_column='id_anomalie', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.AnomaliesEdiFileAnnuaire')),
                ('edi_file', models.ForeignKey(db_column='edi_file', on_delete=django.db.models.deletion.CASCADE, to='core.EDIfile')),
            ],
            options={
                'db_table': 'history_anomalies_edi_files',
            },
        ),
        migrations.CreateModel(
            name='LogisticFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logisticFile', models.FileField(upload_to='')),
                ('logisticFileType', models.CharField(blank=True, max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default='En attente', max_length=200)),
                ('number_annomalies', models.IntegerField(default=0)),
                ('clientName', models.CharField(max_length=200)),
                ('archived', models.BooleanField(default=False)),
                ('ButtonCorrecteActiveted', models.BooleanField(default=False)),
                ('ButtonValidateActivated', models.BooleanField(default=True)),
                ('ButtonInvalidateActivated', models.BooleanField(default=False)),
            ],
        ),
    ]
