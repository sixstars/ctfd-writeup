# modernlevel0

## 先看题目给出的信息，只有n e ct 由于n比较小，利用数据库直接分解，得到p，q

## 多的不说直接上解密代码

```python
from gmpy2 import *

e = 65537
n = 27253584006772549
ct = 25211047465140739

p = 30426857

q = 895708157

fn = (p-1)*(q-1)

d = invert(e,fn)

pt = pow(ct,d,n)

pt = hex(pt)[2:]

print 'flag{'+pt.decode('hex')+'}'
```
于是我们得到了flag
## flag{easy1}
