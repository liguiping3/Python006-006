学习笔记
https://github.com/Python006-006/Python006-006
版本控制

下载地址：
https://git-scm.com/downloads
按自己情况下载对应系统版本

初始化：
git init
配置用户名和邮箱：
git config --global user.name "liguiping3"
git config --global user.email "395584472@qq.com"
检查配置结果：
git config --global --list
显示如下：
user.name=liguiping3
user.email=395584472@qq.com



做个笔记
1.https方式可以使用命令将密码保存到本地
  git config --global credential.helper store
2. git remote add origin git@github.com:liguiping3/learn_git.git

git remote 验证是否添加成功
3. git push -u origin master
4. ssh-keygen -t rsa -C "395584472@qq.com" 生成公钥私钥
5. ssh -T git@github.com 连接到github.com


克隆：

git clone git@github.com:liguiping3/Python006-006.git

修改代码后提交：

 git add .
git commit -m "week01 assignment"
git push -u origin main


pip加速安装
国内常见镜像站：
1、豆瓣：http://pypi.doubanio.com/simple/
2、清华：https://mirrors.tuna.tsinghua.edu.cn/help/pypi

升级pip:
1、方法一：
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pip -U
方法二：
pip config set global.index-url http://pypi.doubanio.com/simple/
pip install pip -U














git clone git@github.com:liguiping3/Python006-006.git
