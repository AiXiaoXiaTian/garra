import re
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse
from rbac import settings


class PermissionMiddlerware(MiddlewareMixin):
    def process_response(self, request, response):
        current_url = request.path_info
        for vaild_url in settings.WHITE_URL_LIST:
            if re.match(vaild_url, current_url):
                # 白名单中的URL无需权限即可访问
                return response
        permission_list = request.session.get(settings.PERMISSION_SESSION_KEY)
        if not permission_list:
            return HttpResponse("未获取到用户权限信息，请登录！")

        flag = False

        for url in permission_list:
            reg = "^%s" % url
            print(reg)
            if re.match(reg, current_url):
                flag = True
                break
        if not flag:
            return HttpResponse("无权访问")
        return response
