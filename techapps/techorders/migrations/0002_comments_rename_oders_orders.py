# Generated by Django 4.1.7 on 2023-03-02 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techorders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='senders name')),
                ('email', models.EmailField(max_length=254, verbose_name='senders email')),
                ('comments', models.TextField(max_length=500)),
                ('date', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'comment section',
                'verbose_name_plural': 'comments section',
                'ordering': ['date'],
            },
        ),
        migrations.RenameModel(
            old_name='Oders',
            new_name='Orders',
        ),
    ]
