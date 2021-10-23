# Generated by Django 3.0.2 on 2020-01-09 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CertificateModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate', models.ImageField(upload_to='certificates')),
                ('filetype', models.CharField(max_length=50)),
                ('studentid', models.CharField(max_length=50)),
                ('universityid', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'certificates',
            },
        ),
        migrations.CreateModel(
            name='RegistrationModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('utype', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'registration',
            },
        ),
        migrations.CreateModel(
            name='RequestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentid', models.CharField(max_length=50)),
                ('verifierid', models.CharField(max_length=50)),
                ('userstatus', models.CharField(max_length=50)),
                ('requeststatus', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'requests',
            },
        ),
    ]
