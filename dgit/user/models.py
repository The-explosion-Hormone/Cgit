

from django.db import models


class User(models.Model):

    SEX = (
        ('male','男性'),
        ('female','女性'),
    )

    LOCATION = (

        ('泰安','泰安'),
        ('济南','济南'),
        ('青岛','青岛'),
        ('淄博','淄博'),

    )

    phonenum = models.CharField(max_length=15, unique=True, verbose_name="手机号")
    nickname = models.CharField(max_length=20, verbose_name = "昵称")
    sex = models.CharField(max_length=8,choices=SEX, verbose_name="性别")
    birthday = models.DateField(default="1990-1-1", verbose_name="出生日")
    avatar = models.CharField(max_length=256, verbose_name="个人头像")
    location = models.CharField(max_length=20, choices= LOCATION , verbose_name="常居地")

