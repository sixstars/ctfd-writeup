## ctfd writeup 汇总

如何上传writeup

- 克隆本仓库到本地，新建以自己id命名的分支并切换分支

```
  git clone git@github.com:sixstars/ctfd-writeup.git
  cd ctfd-writeup
  git branch vampire
  git checkout vampire
```

- 找到对应的题目的文件夹（如果没有请自己新建

- 在题目下面新建以自己id命名的文件夹
- 将解题脚本和README.MD文档放至新建的文件夹中([markdown](http://www.markdown.cn/))
```
  如果要写level0-bash的write-up, 进入stackoverflow文件夹中的level0-bash文件夹，
  新建vampire文件夹，在其中放入写好的writeu和脚本。
```
- 将变动push到远程自己的分支
```
  git push origin vampire
```
- 发起merge请求
```
  进入github，找到pull request栏, 点击“new pull request”，选择分支，creat pull request
```