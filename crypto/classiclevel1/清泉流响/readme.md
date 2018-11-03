# classiclevel1

## 由于题目给出的代码我们来分析一下：

```python
from secret import flag, key

ct = ''
for ch in flag:
    ct += chr(ord(ch)^key)
print ct.encode('hex')
```

## 然后我们又有密文：

```python
ct = '8f85888e929d818cb6828c90b69a99888a8cb6809ab69d8686b69a84888585c894'
```

由于加密采用的是异或的算法，并且明文的结构我们了解flag{XXXXXXXXXXXX}所以我们可以通过前面几位的数得到key的ascii码值

## 首先我们将密文解密：
```python
ct.decode('hex')
```
## 我们得到
```python
ct1='\x8f\x85\x88\x8e\x92\x9d\x81\x8c\xb6\x82\x8c\x90\xb6\x9a\x99\x88\x8a\x8c\xb6\x80\x9a\xb6\x9d\x86\x86\xb6\x9a\x84\x88\x85\x85\xc8\x94'
```
## 也就是
```python
ord('f')^key == chr('\x8f')
ord('l')^key == chr('\x85')
ord('a')^key == chr('\x88')
ord('g')^key == chr('\x8e')
ord('{')^key == chr('\x92')
```
## 于是我们有 key=233

于是解密代码如下

```python
ct = '8f85888e929d818cb6828c90b69a99888a8cb6809ab69d8686b69a84888585c894'

key = 233

ct = ct.decode('hex')

flag = ''

for i in ct:
    flag += chr(ord(i)^key)

print flag
```
## 于是我们有了flag
## flag{the_key_space_is_too_small!}
