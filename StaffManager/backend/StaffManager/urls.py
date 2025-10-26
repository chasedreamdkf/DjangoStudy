"""
URL configuration for StaffManager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.views.static import serve
from django.conf import settings

from App01.views import DepartManage, UserManage

urlpatterns = [
    # path('admin/', admin.site.urls),
    # 用户上传文件的配置
    re_path(r"^media/(?P<path>,*)$", serve, {"document_root": settings.MEDIA_ROOT}, name="media"),
    # 部门管理
    path('depart/list/', DepartManage.depart_list),
    path('depart/add/', DepartManage.depart_add),
    path('depart/delete/', DepartManage.depart_delete),
    path('depart/<int:id>/edit/', DepartManage.depart_edit),   # 匹配传递id的值
    
    # 用户管理
    path('user/list/', UserManage.user_list),
    path('user/add/', UserManage.user_add),
    path("user/MFadd/", UserManage.user_add_ModelForm)
]
