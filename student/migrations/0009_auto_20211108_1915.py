# Generated by Django 3.0.3 on 2021-11-08 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0008_delete_json'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='', max_length=200)),
                ('Year', models.IntegerField(default=0)),
                ('Pdf', models.FileField(upload_to='exercise/previous_papers/Jee')),
            ],
        ),
        migrations.CreateModel(
            name='Neet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='', max_length=200)),
                ('Year', models.IntegerField(default=0)),
                ('Pdf', models.FileField(upload_to='exercise/previous_papers/Neet')),
            ],
        ),
        migrations.RemoveField(
            model_name='question',
            name='paper',
        ),
        migrations.DeleteModel(
            name='Previous_paper',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
