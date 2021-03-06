# Generated by Django 2.1.4 on 2020-01-09 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('create_at', models.DateTimeField(verbose_name='发布时间')),
                ('avatar', models.ImageField(upload_to='avatar', verbose_name='头像')),
                ('weibo', models.URLField(blank=True, verbose_name='微博')),
                ('zhihu', models.URLField(blank=True, verbose_name='知乎')),
                ('twitter', models.URLField(blank=True, verbose_name='Twitter')),
                ('facebook', models.URLField(blank=True, verbose_name='Facebook')),
                ('github', models.URLField(blank=True, verbose_name='Github')),
                ('stackoverflow', models.URLField(blank=True, verbose_name='Stack Overflow')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='邮箱')),
            ],
            options={
                'verbose_name': '自我简介',
                'verbose_name_plural': '自我简介',
            },
        ),
        migrations.CreateModel(
            name='Ziyu',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=200, verbose_name='标题')),
                ('create_at', models.DateTimeField(verbose_name='发布时间')),
            ],
            options={
                'verbose_name': '自语',
                'verbose_name_plural': '自语',
            },
        ),
    ]
