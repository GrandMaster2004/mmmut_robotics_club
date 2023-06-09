# Generated by Django 3.2.18 on 2023-05-12 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_college', '0008_circuitary_work_web_work'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_title', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=1000)),
                ('event_format', models.CharField(max_length=500)),
                ('event_schedule', models.CharField(max_length=500)),
                ('image_Event', models.ImageField(upload_to='Event_img')),
            ],
        ),
        migrations.AddField(
            model_name='circuitary_work',
            name='video_link',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='web_work',
            name='video_link',
            field=models.CharField(default=2, max_length=500),
            preserve_default=False,
        ),
    ]
