#逻辑语句放在这个文件里边，能够保证逻辑复用

import requests
import random

from django.core.cache import cache

from common import keys
from dgit import cfg




#产生验证码
def gen_randcode(length):

    chars = [str(random.randint(0,9) for i in range(length))]
    return ''.join(chars) # 把产生的1位随机数以 只对内存操作一次的方式 加入到空列表中




#对指定手机号进行发送
def send_vcode(phone):
    vcode = gen_randcode(6)

    #验证码要有有效期
    cache.set(keys.VCODE_KEY % phone,vcode,300)#保证key value 的一一对应，对key进行标注

    print('验证码是',vcode)

    sms_args = cfg.YZX_PARAMS.copy() # 以浅拷贝的原型模式 来防止对cfg这个文件里边的全局变量进行改动
    sms_args['mobile'] = phone #where来的？
    sms_args['param']  = vcode
    response = requests.post(cfg.YZX_API, json=sms_args)


    #发完还要进行检查
    if response.status_code == 200:
        result = response.json()
        if result['code'] == '000000': # 云之迅规定000000是right
            return True

    return False


