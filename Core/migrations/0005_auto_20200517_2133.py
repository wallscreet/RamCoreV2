# Generated by Django 3.0.6 on 2020-05-18 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0004_auto_20200517_1358'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='updatedate',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Posted')], default=1),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(default='non', max_length=255),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Posted')], default=0),
        ),
    ]
