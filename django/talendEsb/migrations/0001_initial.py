# Generated by Django 2.1.5 on 2022-09-12 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InterventionFacturationTransport',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('execution_time', models.DateTimeField(auto_now=True)),
                ('typeTransaction', models.CharField(max_length=12)),
            ],
            options={
                'db_table': 'intervention_Facturation_transport',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PlansFacturation',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('plan', models.CharField(max_length=45)),
                ('status', models.CharField(max_length=45)),
                ('month', models.IntegerField()),
                ('year', models.IntegerField()),
                ('numFacture', models.IntegerField()),
                ('derniere_execution', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'plans_facturation',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TransactionsLivraison',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('statut', models.CharField(blank=True, max_length=45, null=True)),
                ('fichier_livraison_sftp', models.CharField(blank=True, max_length=100, null=True)),
                ('fichier_exception_sftp', models.CharField(blank=True, max_length=100, null=True)),
                ('fichier_metadata_sftp', models.CharField(blank=True, max_length=100, null=True)),
                ('fichier_mad_sftp', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'transactions_livraison',
                'managed': False,
            },
        ),
    ]
