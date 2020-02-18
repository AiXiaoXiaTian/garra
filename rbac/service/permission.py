from rbac import settings


def init_permission(user,request):
    """
    用户权限初始化
    :param user:
    :param request:
    :return:
    """
    permission_queryset = user.roles.filter(permissions__url__isnull=False).values('permissions__url').distinct()
    permissions = [item['permissions__url'] for item in permission_queryset]
    request.session[settings.PERMISSION_SESSION_KEY] = permissions
