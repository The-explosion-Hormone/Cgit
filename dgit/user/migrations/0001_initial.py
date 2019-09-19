# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-09-19 20:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phonenum', models.CharField(max_length=15, unique=True, verbose_name='手机号')),
                ('nickname', models.CharField(max_length=20, verbose_name='昵称')),
                ('sex', models.CharField(choices=[('male', '男性'), ('female', '女性')], max_length=8, verbose_name='性别')),
                ('birthday', models.DateField(default='1990-1-1', verbose_name='出生日')),
                ('avatar', models.CharField(max_length=256, verbose_name='个人头像')),
                ('location', models.CharField(choices=[('泰安', '泰安'), ('济南', '济南'), ('青岛', '青岛'), ('淄博', '淄博')], max_length=20, verbose_name='常居地')),
            ],
        ),
    ]