import json

from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from users.models import UserInfo, UserToken


def md5(user):
    import hashlib
    import time

    # 当前时间，相当于生成一个随机的字符串
    ctime = str(time.time())

    # token加密
    m = hashlib.md5(bytes(user, encoding='utf-8'))
    m.update(bytes(ctime, encoding='utf-8'))
    return m.hexdigest()

@method_decorator(csrf_exempt, name='dispatch')
class AuthView(View):

    def get(self, request, *args, **kwargs):
        ret = {'code': 1000, 'msg': 'success', 'name': 'test'}
        ret = json.dumps(ret, ensure_ascii=False)
        return render(request, 'users/register.html')
        # return HttpResponse(ret)

    def post(self, request, *args, **kwargs):
        ret = {'code': 1000, 'msg': None}

        try:
            user = request.POST.get('username')
            pwd = request.POST.get('password')
            print(user)
            obj = UserInfo.objects.filter(username=user).first()

            if not obj:
                # 如果用户第一次登陆则创建用户
                obj =  UserInfo.objects.create(username=user, password=pwd)
                ret['code'] = 1001
                ret['msg'] = '创建用户成功'

            # 为用户创建token
            token = md5(user)
            # 存在就更新，不存在就创建
            UserToken.objects.update_or_create(user=obj, defaults={'token': token})
            ret['token'] = token
        except Exception as e:
            ret['code'] = 1002
            ret['msg'] = '请求异常'
        return JsonResponse(ret)