# Generated by Django 3.2.5 on 2022-07-20 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_api', '0002_alter_employee_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='email',
            field=models.EmailField(default='email@email.com', max_length=50, unique=True),
        ),
    ]
