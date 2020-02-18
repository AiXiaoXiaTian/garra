from django.db import models


class Permission(models.Model):
    """
    权限表
    """
    code = models.CharField(primary_key=True, verbose_name="权限code码", max_length=8, default="")
    title = models.CharField(verbose_name='标题', max_length=32, default="")
    url = models.CharField(verbose_name='含正则的URL', max_length=128, default="")
    name = models.CharField(verbose_name='别名', max_length=32, default="")
    icon = models.CharField(verbose_name='图标', max_length=32, null=True, blank=True)
    main_menu = models.BooleanField(verbose_name='是否是主菜单', default=True)

    def __str__(self):
        return self.title


class Role(models.Model):
    """
    角色
    """
    title = models.CharField(verbose_name='角色名称', max_length=32)
    permissions = models.ManyToManyField(verbose_name='拥有的所有权限', to='Permission', blank=True,null= True)

    def __str__(self):
        return self.title


class UserInfo(models.Model):
    """
    用户表
    """
    name = models.CharField(verbose_name='用户名', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=64)
    email = models.CharField(verbose_name='邮箱', max_length=32)
    roles = models.ManyToManyField(verbose_name='拥有的所有角色', to='Role', blank=True)

    def __str__(self):
        return self.name
