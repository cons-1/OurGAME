# 正确的git clone后的修改文件、提交文件、推送文件的流程

# git clone
# git add .
# git commit -m "first commit"
# git push -u origin main
# git pull origin main
# 常用的git指令,并附上注释
# git init  # 初始化一个git仓库
# git add .  # 添加所有文件到暂存区
# git commit -m "first commit"  # 提交到本地仓库
# git remote add origin # 添加远程仓库地址
# git push -u origin master  # 推送到远程仓库
# git pull origin master  # 从远程仓库拉取
# git clone  # 克隆远程仓库
# git branch  # 查看分支
# git checkout -b dev  # 创建并切换到dev分支
# git merge dev  # 合并dev分支到当前分支
# git branch -d dev  # 删除dev分支
# git log  # 查看提交历史
# git reset --hard HEAD^  # 回退到上一个版本
# git reflog  # 查看命令历史
# git checkout -- file  # 丢弃工作区的修改
# git reset HEAD file  # 撤销暂存区的修改
# git rm file  # 删除文件
# git remote  # 查看远程仓库
# git remote -v  # 查看远程仓库详细信息
# git push origin --delete dev  # 删除远程分支
# git push origin :dev  # 删除远程分支
# git push origin dev  # 推送dev分支到远程
# git push origin dev:master  # 推送dev分支到远程的master分支
# git pull origin dev  # 从远程的dev分支拉取
# git pull origin dev:master  # 从远程的dev分支拉取到本地的master分支
# git fetch origin dev  # 从远程的dev分支拉取到本地的origin/dev分支
# git branch -r  # 查看远程分支
# git config --global pull.rebase false #


# 正确的git clone后的修改文件、提交文件、推送文件的流程

# git clone
# git add .
# git commit -m "first commit"
# git commit -m "起个提交的名字"
# git push -u origin main
# git pull origin main

# 水仙花数
# for i in range(100, 1000):
#     a = i // 100
#     b = i // 10 % 10
#     c = i % 10
#     if a ** 3 + b ** 3 + c ** 3 == i:
#         print(i)


# 九九乘法表
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(f"{j} * {i} = {i * j}", end="\t")
#     print()

