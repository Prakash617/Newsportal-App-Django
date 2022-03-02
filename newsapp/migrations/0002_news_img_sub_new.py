# Generated by Django 4.0.3 on 2022-03-02 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='img',
            field=models.ImageField(default='space', upload_to='news_img'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Sub_New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_title', models.CharField(max_length=200)),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newsapp.news')),
            ],
        ),
    ]