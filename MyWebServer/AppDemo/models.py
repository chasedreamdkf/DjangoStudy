from django.db import models

# Create your models here.
class UserInfo(models.Model):
    """
    create table AppDemo_userinfo(
        id bigint auto_increment primary key,
        name varchar(32),
        password varchar(64),
        age int
    );
    """
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField()
    # test1 = models.IntegerField() # 按命令行提示添加默认值
    # test2 = models.IntegerField(default=2) # 直接设置默认值
    # test3 = models.IntegerField(null=True, blank=True) # 允许其可以为空


class Department(models.Model):
    title = models.CharField(max_length=16)
    

# 新增数据 <==> inert into AppDemo_department (title) values('销售部')
# Department.objects.create(title = "销售部")
# UserInfo.objects.create(name="Tom", password='123456', age=19)