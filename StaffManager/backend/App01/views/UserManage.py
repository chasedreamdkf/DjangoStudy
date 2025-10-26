from django.shortcuts import render, redirect
from django import forms
from App01 import models

def user_list(req):
    """用户管理"""
    # 获取所有的用户
    queryset = models.UserInfo.objects.all()
    # for item in queryset:
        # print(item.id, item.name, item.password, item.age, item.account, item.create_time.strftime("%Y-%m-%d"), item.get_sex_display(), item.depart.title)
    return render(req, "user_list.html", {"users": queryset})


def user_add(req):
    """新建用户"""
    if req.method == "GET":
        context = {
            "sex_choices": models.UserInfo.sex_choices,
            "departs": models.Department.objects.all()
        }
        return render(req, "user_add.html", context)
    # 获取用户数据
    name = req.POST.get("name")
    password = req.POST.get("password")
    age = req.POST.get("age")
    account = req.POST.get("account")
    create_time = req.POST.get("create_time")
    sex = req.POST.get("sex")
    depart_id = req.POST.get("depart")
    # print(name, password, age, account, create_time, sex, depart_id)
    models.UserInfo.objects.create(name=name, password=password,
                                   age=age, account=account,
                                   create_time=create_time, sex=sex,
                                   depart_id=depart_id)
    return redirect("/user/list/")


class User(forms.ModelForm):
    password = forms.CharField(min_length=6, label="密码")
    class Meta:
        """定义表单数据"""
        model = models.UserInfo
        fields = ["name", "password", "age", "account", "create_time", "sex", "depart"]
    
    def __init__(self, *agrs, **kwargs):
        super().__init__(*agrs, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control"}


def user_add_ModelForm(req):
    """添加用户ModelForm版"""
    if req.method == "GET":
        form = User()
        return render(req, "user_MFadd.html", {"form": form})
    
    # 获取数据
    form = User(data=req.POST)
    if form.is_valid():
        print(form.cleaned_data)
        # 保存到数据库
        form.save()
        return redirect("/user/list/")
    else:
        print(form.errors)