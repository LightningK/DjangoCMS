# STUCMS

STUCMS是由STU CS系学子开发的一款通用网站内容管理系统，采用Django技术框架，使用MySQL数据库进行数据存储，前端使用Bootstrap和AdminLTE技术实现。该系统具备丰富的功能模块，操作简便，界面美观，易于管理和维护。

# 功能特性
1. 响应式布局的前端页面
2. 美观易用的后台管理系统
3. 支持markdown的强大文章管理功能
4. 支持多用户管理
5. to be continued...

# 运行教程

1. 安装必要的依赖库
```python
pip install -r requirement.txt
```

2. mysql 创建数据库
```sql
CREATE DATABASE peekpa_db1 utf8;
```

3. 获取源代码，并将 STUCMS/settings.py 中的数据库配置修改为自己的配置
```bash
git clone https://github.com/LightningK/DjangoCMS.git
```
```python
DATABASES = {
    'default': {
        # 数据库引擎（是mysql还是oracle等）
        'ENGINE': 'django.db.backends.mysql',
        # 数据库的名字
        'NAME': 'peekpa_db1',
        # 连接mysql数据库的用户名
        'USER': 'root',
        # 连接mysql数据库的密码
        'PASSWORD': '123456',
        # mysql数据库的主机地址
        'HOST': '127.0.0.1',
        # mysql数据库的端口号
        'PORT': '3306',
    }
}
```

4. 终端下进入根目录,迁移数据库,创建超级用户，并运行项目
```bash
python manage.py migrate
python manage.py createsuperuser # 按照提示操作
python manage.py runserver
```

5. 初次运行时需要进入后台管理页面 http://localhost:8080/cms, 使用上一步创建的账号密码登录。在setting中设置网站的标题等信息。之后进入网站首页http://localhost:8080/ 进行查看。

