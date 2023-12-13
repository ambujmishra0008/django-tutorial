# Generated by Django 4.2.6 on 2023-12-13 14:13

from django.db import migrations, models
import djchoices.choices


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='status',
            field=models.CharField(choices=[('active', 'ACTIVE'), ('inactive', 'INACTIVE'), ('close', 'CLOSE')], max_length=64, null=True, validators=[djchoices.choices.ChoicesValidator({'active': 'ACTIVE', 'close': 'CLOSE', 'inactive': 'INACTIVE'})]),
        ),
        migrations.AlterField(
            model_name='student',
            name='resume',
            field=models.FileField(upload_to='resume'),
        ),
    ]
