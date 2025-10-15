from django.shortcuts import render, redirect
from App01 import models

# Create your views here.
def depart_list(req):
    """部门列表"""
    departs = models.Department.objects.all()
    return render(req, 'depart_list.html', {"departs": departs})


def depart_add(req):
    """添加部门"""
    if req.method == "GET":
        return render(req, "depart_add.html")
    
    # 获取数据
    title = req.POST.get("title")
    # 保存到数据库
    models.Department.objects.create(title=title)
    
    return redirect('/depart/list/')


def depart_delete(req):
    """删除部门"""
    # 获取部门id "https/127.0.0.1:8000/depart/delete/?id=1"
    id = req.GET.get('id')
    # 删除
    models.Department.objects.filter(id=id).delete()
    
    return redirect('/depart/list/')


# /depart/1/edit
def depart_edit(req, id):
    """修改部门"""
    if req.method == "GET":
        title = models.Department.objects.filter(id=id).first().title
        return render(req, "depart_edit.html", {"title": title})
    # 更新数据
    new_title = req.POST.get("title")
    models.Department.objects.filter(id=id).update(title=new_title)
    return redirect("/depart/list/")


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