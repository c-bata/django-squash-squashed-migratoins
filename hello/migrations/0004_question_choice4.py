# Generated by Django 3.1 on 2020-03-29 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0003_question_choice3'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='choice4',
            field=models.CharField(default='', max_length=20),
        ),
    ]
