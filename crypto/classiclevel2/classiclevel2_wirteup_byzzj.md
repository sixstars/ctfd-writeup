# classiclevel2

##  我们有了如下代码以及密文

```python
from secret import flag, step

ct = ''
cur = 0
for i in range(len(flag)):
    ct += flag[cur]
    cur = (cur+step)%len(flag)
print ct
```
```python
ct = 'fcgemleayaatislgonpl{o}aaks'
```

## 由题目的代码我们可以知道，由于明文的形式为flag{XXXXXXXXXXX} 我们可以得到step的值

* (step+0)%len(ct) = 5 or 14 or 19 (明文第二个字母是l)
* (step+step)%len(ct) = 7 or 9 or 10 or 23 or 24
## 由此我们可以得到step = 5
## 于是我们有了解密代码

```python
ct = 'fcgemleayaatislgonpl{o}aaks'
step = 5

cur = 0
pt = ''

for i in  range(len(ct)):
    pt+= ct[cur]
    cur = (cur+step)%len(ct)

print pt
```
## 运行脚本我们有了flag
## flag{keyspacetoosmallagain}
