# -*- encoding: utf-8 -*-
"""
@File    : gitcaozuo.py
@Time    : 2020/4/30 16:11
@Author  : zwt
@git   : 
@Software: PyCharm
"""

"""
objective

git branch 新建分支

git checkout -b new_branch 新建分支并切换过去

git merge new_branch

git rebase 另一种合并分支的方法,会使得提交历史呈现线性

head 指向当前分支上最近一次提交记录，通常指向的是分支名

git log查看提交记录的哈希值

git checkout master^ 相当于master的父节点，  ~num跳转到上num的父节点

git branch -f master HEAD~3 强制移动分支到某个提交节点

git reset 回退提交记录， 只存在本地

git revert会将撤销更改分享到远程分支

git cherry-pick c2 c4只提交这两个分支的节点内容

git rebase -i HEAD~num

git clone

git clone -b branch_name 地址

默认的远程分支为origin

git fetch从远程分支拉取数据：从远程仓库下载本地仓库中缺失的提交记录、更新远程分支指针
但是不会改变本地仓库的状态，不会更新自己的master分支，也不会修改磁盘的文件

git pull就是git fetch和git merge的缩写

git pull origin master
"""
