# Generated by Django 2.1.7 on 2019-02-17 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_date', models.DateField(auto_now_add=True)),
                ('name', models.CharField(max_length=50)),
                ('picture', models.ImageField(upload_to='static/images/profile_pictures/')),
                ('year', models.CharField(choices=[('1', '1st Year'), ('2', '2nd Year'), ('3', '3rd Year'), ('4', '4th Year'), ('Grad', 'Graduate Student'), ('Alumni', 'Alumni')], max_length=50)),
                ('bio', models.TextField(max_length=500)),
            ],
        ),
    ]
