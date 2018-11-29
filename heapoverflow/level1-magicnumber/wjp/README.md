# level1
### 1. 程序逻辑
告诉malloc了多少内存块，让你输入magic number是什么，程序中如果malloc返回的地址是a,则比较*(a - 1)与输入是否相等,就是所谓的magic number

### 2. 写一个简单的c语言脚本，通过查看0-100之间的magic，number来找规律

```c
#include <stdio.h>
#include <malloc.h>

int main(){
   for(int i=0; i<100; i++)
   {
       long * p = malloc(i);
       printf("%x:%x  ",i,* (int *)(p-1));
   }
   return 0;
}
```
程序输出为：
0:21  1:21  2:21  3:21  4:21  5:21  6:21  7:21  8:21  9:21  a:21  b:21  c:21  d:21  e:21  f:21  10:21  11:21  12:21  13:21  14:21  15:21  16:21  17:21  18:21  19:31  1a:31  1b:31  1c:31  1d:31  1e:31  1f:31  20:31  21:31  22:31  23:31  24:31  25:31  26:31  27:31  28:31  29:41  2a:41  2b:41  2c:41  2d:41  2e:41  2f:41  30:41  31:41  32:41  33:41  34:41  35:41  36:41  37:41  38:41  39:51  3a:51  3b:51  3c:51  3d:51  3e:51  3f:51  40:51  41:51  42:51  43:51  44:51  45:51  46:51  47:51  48:51  49:61  4a:61  4b:61  4c:61  4d:61  4e:61  4f:61  50:61  51:61  52:61  53:61  54:61  55:61  56:61  57:61  58:61  59:71  5a:71  5b:71  5c:71  5d:71  5e:71  5f:71  60:71  61:71  62:71  63:71
发现规律：
    0x0-0x18: 0x21
    0x19-0x28: 0x31
    0x29-0x38: 0x41
    ......

### 3.exp 
```python
from pwn import *
context.log_level="debug"
pwn_file="./level1-magicnumber"
elf=ELF(pwn_file)

if len(sys.argv)==1:
    r=process(pwn_file)
    pid=r.pid
else:
    r=remote("pwn.sixstars.team", 22501)
    pid=0

def debug():
    log.debug("process pid:%d"%pid)
    pause()
    r.recvline()

r.recvline()

import re
for i in range(16):
  w = r.recvuntil("magic number:")
  num = re.findall('\((.*)\)',w)[0]
  size = int(num,16)
  if size<=24:
      ch = 33
  elif size%16<=8 and size%16>0:
      ch = ((size+0xf)>>4<<4) + 0x1
  else:
      ch = ((size+0xf)>>4<<4) + 0x11
  print hex(size),hex(ch)
  r.sendline(str(ch))

r.interactive()
```
#### 4.相关知识
[理解glibc malloc](https://sploitfun.wordpress.com/2015/02/10/understanding-glibc-malloc/)