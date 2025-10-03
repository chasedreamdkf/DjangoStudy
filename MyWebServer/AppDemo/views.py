from django.shortcuts import render, HttpResponse, redirect
from AppDemo import models

# Create your views here.

def index(request):
    return HttpResponse("Hello Django!")

def template_test(request):
    # 配置`settings.py`的`TEMPLATES`的`'DIRS'`列表添加os.path.join(BASE_DIR, 'templates')后，优先去项目目录的根目录去查找文件
    # 去app目录下的templates目录寻找对应的文件(根据app的注册顺序逐个查找)
    return render(request, 'test.html')

def something(req: HttpResponse):
    """_summary_

    Args:
        req (obj): 封装了用户发送过来的所有请求相关数据
    """
    print(req.method)       # 获取请求方式
    print(req.GET)          # 获取URL上传递的值
    print(req.POST)         # 在请求体中提交数据
    # return render(req, 'something.html')    # 【响应】将模板渲染后返回给用户浏览器
    # return HttpResponse('返回字符串给请求者')  # 【响应】
    return redirect('https://www.baidu.com')  # 【响应】让浏览器重定向到制定网页

def login(req):
    if req.method == 'GET':
        return render(req, 'login.html')
    
    print(req.POST)
    username = req.POST.get('user')
    password = req.POST.get('pwd')
    if username == 'root' and password == '123456':
        # return HttpResponse('登陆成功')
        return redirect('https://www.baidu.com')
    
    return render(req, 'login.html', {'error_msg': '用户名或密码错误'})


def orm(req):
    """测试ORM操作表中的数据"""
    # models.Department.objects.create(title="销售部")
    # models.Department.objects.create(title="IT部")
    # models.Department.objects.create(title="运营部")
    
    # models.UserInfo.objects.create(name="Jim", password='123456', age=19)
    
    # 2.删除
    # models.Department.objects.filter(id=4).delete()   # 条件删除
    # models.Department.objects.all().delete()          # 全部删除
    
    # 3.获取数据
    # data_list = models.UserInfo.objects.all()   # 获取所有数据,为QuerySet类型
    # print(data_list)                            # <QuerySet [<UserInfo: UserInfo object (1)>, <UserInfo: UserInfo object (2)>]>
    # for item in data_list:
    #     print(item.name, item.password, item.age)
    #     """
    #     Tom 123456 19
    #     Jim 123456 19
    #     """
    
    # data_list = models.UserInfo.objects.filter(id=1)    # 条件查询,然后循环遍历
    # OR
    # row_obj = models.UserInfo.objects.filter(id=1).first()
    # print(row_obj.id, row_obj.name, row_obj.password, row_obj.age)  # 1 Tom 123456 19
    
    # 4.更新数据
    # models.UserInfo.objects.all().update(password=999)            # 更新所有数据
    # models.UserInfo.objects.filter(id=2).update(password=123456)    # 条件更新数据
    
    return HttpResponse("成功")

def info_list(req):
    """展示用户列表"""
    # 获取数据库中所有的用户数据
    data_list = models.UserInfo.objects.all();
    
    return render(req, "info_list.html", {"UserInfo": data_list})

def info_add(req):
    """添加用户"""
    if req.method == "GET":
        return render(req, "info_add.html")
    
    # 获取用户提交的数据
    user = req.POST.get("user")
    password = req.POST.get("password")
    age = req.POST.get("age")
    
    # 添加数据到数据库
    models.UserInfo.objects.create(name=user, password=password, age=age)
    # return HttpResponse("添加成功")
    return redirect("/info/list/")


def info_delete(req):
    """删除用户"""
    if req.method == 'GET':
        id = req.GET.get('id')
        models.UserInfo.objects.filter(id=id).delete()
    return redirect('/info/list/')