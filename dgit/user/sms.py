import requests

# 整体移到cfg里边
# YZX_API = 'https://open.ucpaas.com/ol/sms/sendsms'
#
# YZX_PARAMS ={
#
#  "sid":"83d1fd14a53d845f7178a42fe4eb3c8a",
#
#  "token":"991ba8c5ba70f504d9d001c45a7b97a3",
#
#  "appid":"17b97b7e74864681be513196d1a319fc",
#
#  "templateid":"503342",
#
#  "param":"123456",
#
#  "mobile":"15588537906",
#
#
# }

def send(phone,code):

    YZX_PARAMS['param'] = code  #code 就是云之迅给你的验证码
    YZX_PARAMS['mobile'] = phone
    response = requests.post(YZX_API, json = YZX_PARAMS)

    return response

# resp = send('15588537906','668899')
#
# print(resp.status_code)
#
# print(resp.text)

# 显示帐号未认证 ,得用身份证