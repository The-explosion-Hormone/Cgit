import os

from django.http import JsonResponse
from django.shortcuts import redirect
from django.core.cache import cache

from common import keys
from common import stat
from dgit import cfg
from user import logics





#获取短信验证码
from user.models import User


def haha(request):
    print(22211111111)



def get_vcode(request):
    print(111111111111111)

    phonenum = request.GET.get('phonenum')


    #连发送加验证
    if logics.send_vcode(phonenum):
        return JsonResponse({'code':stat.OK,'data':None})


    else:
        return JsonResponse({'code':stat.VCODE_ERR,'data':None})


#进行 验证 登陆 注册
def check_vcode(request):

    #验证
    phonenum = request.POST.get('phonenum')
    vcode = request.POST.get('vcode')

    #过期验证逻辑
    cache_vcode = cache.get(keys.VCODE_KEY % phonenum)
    if vcode and cache_vcode and vcode == cache_vcode:
        #登陆 或 注册
        try:
            user = User.objects.get(phonenum=phonenum)
        except User.DoesNotExist:
            user = User.objects.create(
                phonenum = phonenum,
                nickname = phonenum,
            )
        request.session['uid'] = user.id#随便写，目的是让session发生改变，然后让用户的账户被session
        return JsonResponse({'code':stat.OK,'data':None})

    else:
        return JsonResponse({'code':stat.INVILD_VCODE, 'data':None})














