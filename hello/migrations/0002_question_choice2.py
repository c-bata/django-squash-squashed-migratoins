# Generated by Django 3.1 on 2020-03-29 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_squashed_0002_question_choice1'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='choice2',
            field=models.CharField(default='', max_length=20),
        ),
    ]
