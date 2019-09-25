from django.conf.urls import url
from user import api as user_api


urlpatterns = [

    url(r'^get_vcode/',user_api.get_vcode),
    url(r'^check_vcode/',user_api.check_vcode),

]