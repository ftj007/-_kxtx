新建项目
1. git init --建仓
2. git add  * --添加代码到本地仓库（*是代码添加全部更新的）或git add -A
3. git commit -m "first commit"  --提交到本地缓存（“引号里面是说明提交了什么东西”）对上传文件的描述。
4. git remote add origin https://github.com/ftj007/zdh-_kxtx.git  --提交到远程github上（后面的地址，就是之前配置的repository地址）
5. git push -u origin master  --push到master分支

克隆到本地

git clone https://github.com/ftj007/zdh-_kxtx.git

更新本代码

1. git status（查看本地分支文件信息，确保更新时不产生冲突）
2. git checkout -- [file name] （若文件有修改，可以还原到最初状态; 若文件需要更新到服务器上，应该先merge到服务器，再更新到本地）
3. git branch（查看当前分支情况）
4. git checkout [remote branch](若分支为本地分支，则需切换到服务器的远程分支)
5. git pull

更新github代码
1. git add *
2. git commit -m "更新说明“ （commit只是提交到缓存区域）
3. git pull（如果是多人同时开发维护代码，得先git pull ,拉取当前分支最新代码，其实就是先更新本地代码）
4. git push origin master（最后一步才是push到远程的master分支上）


实际上：def fun(n,*args):
如果还原到普通函数就是这样的了：
def fun(n,args):
这是使用它的时候就是这样的：
fun(12, ["xu", "yong", "quan"])
*args在作为行参的时候，就表示，将这个集合拆分成若干个变量元素。这样就是：
def fun(n, args[0],args[1],args[2]....).
*args在作为实参（变量）的时候，也是拆分的意思
