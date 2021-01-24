学习笔记
第一课：
安装django
pip install django==2.2.13
pip install django (不指定版本，安装最新版本)
升级安装
pip install --upgrade django==2.2.13
查看版本
import django
django.__version__

第二课：
创建django项目
./django-admin startproject MyDjango
目录结构
find MyDjango/
MyDjango/
MyDjango/MyDjango
MyDjango/MyDjango/asgi.py
MyDjango/MyDjango/urls.py
MyDjango/MyDjango/settings.py 项目的配置文件
MyDjango/MyDjango/__init__.py
MyDjango/MyDjango/wsgi.py
MyDjango/manage.py 命令行工具
创建应用程序：
python3 manage.py startapp index
启动应用程序：
python manage.py runserver 0.0.0.0:80
第三课：
配置文件settings.py
一般需要修改项：数据库、app项
mysql 驱动：mysqlclient pymysql
第四课：
url调度器
第五课：
模块和包
第六课：
让url支持变量
第七课：
URL正则和自定义过滤器
第八课：
view视图快捷方式
第九课：
使用orm创建数据库表
python manage.py makemigrations
python manage.py migrate
安装pymysql
在init文件加入：
import pymysql
pymysql.install_as_MySQLdb()
第十课：
ORM API
第十一课：
DJANGO模板开发
第十二课：
展示数据库中内容
第十三课：
豆瓣页面展示功能
第十四课：
URLconf和models
第十五课：
views视图
第十六课：
结合bootstrap模板进行开发、
第十七课：
阅读Django的源代码
第十八课：
manage.py源码分析
