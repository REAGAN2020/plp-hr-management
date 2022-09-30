# Generated by Django 3.2.6 on 2022-08-06 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='leavetype',
            field=models.CharField(choices=[('sick', 'Sick Leave'), ('casual', 'Casual Leave'), ('emergency', 'Emergency Leave'), ('study', 'Study Leave'), ('maternity', 'Maternity Leave'), ('bereavement', 'Bereavement Leave'), ('quarantine', 'Self Quarantine'), ('compensatory', 'Compensatory Leave'), ('sabbatical', 'Sabbatical Leave')], default='sick', max_length=25, null=True),
        ),
    ]
