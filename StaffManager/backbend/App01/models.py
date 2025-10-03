from django.db import models

# Create your models here.
class Department(models.Model):
    """部门表"""
    title = models.CharField(max_length=32, verbose_name="部门名称")
    

class UserInfo(models.Model):
    """员工表"""
    name = models.CharField(verbose_name="姓名", max_length=16)
    password = models.CharField(verbose_name="密码", max_length=64)
    age = models.IntegerField(verbose_name="年龄")
    sex_choices = (('0', '女'), ('1', '男'))
    sex = models.CharField(verbose_name='性别', max_length=1, choices=sex_choices)
    account = models.DecimalField(verbose_name='余额', max_digits=10, decimal_places=2, default=0)
    create_time = models.DateTimeField(verbose_name='入职时间')
    # 约束，与Department表的id关联 depart会自动变成depart_id
    depart = models.ForeignKey(verbose_name='部门ID', to="Department", to_field='id', on_delete=models.CASCADE)    # 级联删除
    # depart = models.ForeignKey(to="Department", to_field='id', on_delete=models.SET_NULL, null=True, blank=True) # 置空
    


