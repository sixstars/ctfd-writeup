一些有用的gadget

```

   0:   03 53 43                add    edx,DWORD PTR [rbx+0x43]
   0:   03 53 47                add    edx,DWORD PTR [rbx+0x47]
   0:   03 53 49                add    edx,DWORD PTR [rbx+0x49]
   0:   03 53 4f                add    edx,DWORD PTR [rbx+0x4f]
   0:   03 53 53                add    edx,DWORD PTR [rbx+0x53]
   0:   03 53 59                add    edx,DWORD PTR [rbx+0x59]
   0:   03 53 61                add    edx,DWORD PTR [rbx+0x61]
   0:   03 53 65                add    edx,DWORD PTR [rbx+0x65]
   0:   03 53 67                add    edx,DWORD PTR [rbx+0x67]

   0:   29 02                   sub    DWORD PTR [rdx],eax
   0:   29 03                   sub    DWORD PTR [rbx],eax
   0:   29 07                   sub    DWORD PTR [rdi],eax
   0:   29 0b                   sub    DWORD PTR [rbx],ecx
   0:   29 11                   sub    DWORD PTR [rcx],edx
   0:   29 13                   sub    DWORD PTR [rbx],edx
   0:   29 17                   sub    DWORD PTR [rdi],edx
   0:   29 1f                   sub    DWORD PTR [rdi],ebx
   0:   29 29                   sub    DWORD PTR [rcx],ebp
   0:   29 2b                   sub    DWORD PTR [rbx],ebp
   0:   29 2f                   sub    DWORD PTR [rdi],ebp
   0:   29 3b                   sub    DWORD PTR [rbx],edi
   0:   29 c1                   sub    ecx,eax
   0:   29 c5                   sub    ebp,eax
   0:   29 c7                   sub    edi,eax
   0:   29 d3                   sub    ebx,edx
   0:   29 df                   sub    edi,ebx
   0:   29 e3                   sub    ebx,esp
   0:   29 e5                   sub    ebp,esp
   0:   29 e9                   sub    ecx,ebp
   0:   29 ef                   sub    edi,ebp
   0:   29 f1                   sub    ecx,esi
   0:   29 fb                   sub    ebx,edi
   0:   2b 02                   sub    eax,DWORD PTR [rdx]
   0:   2b 03                   sub    eax,DWORD PTR [rbx]
   0:   2b 07                   sub    eax,DWORD PTR [rdi]
   0:   2b 0b                   sub    ecx,DWORD PTR [rbx]
   0:   2b 11                   sub    edx,DWORD PTR [rcx]
   0:   2b 13                   sub    edx,DWORD PTR [rbx]
   0:   2b 17                   sub    edx,DWORD PTR [rdi]
   0:   2b 1f                   sub    ebx,DWORD PTR [rdi]
   0:   2b 29                   sub    ebp,DWORD PTR [rcx]
   0:   2b 2b                   sub    ebp,DWORD PTR [rbx]
   0:   2b 2f                   sub    ebp,DWORD PTR [rdi]
   0:   2b 3b                   sub    edi,DWORD PTR [rbx]
   0:   2b c1                   sub    eax,ecx
   0:   2b c5                   sub    eax,ebp
   0:   2b c7                   sub    eax,edi
   0:   2b d3                   sub    edx,ebx
   0:   2b df                   sub    ebx,edi
   0:   2b e3                   sub    esp,ebx
   0:   2b e5                   sub    esp,ebp
   0:   2b e9                   sub    ebp,ecx
   0:   2b ef                   sub    ebp,edi
   0:   2b f1                   sub    esi,ecx
   0:   2b fb                   sub    edi,ebx
   0:   71 02                   jno    0x4
   0:   71 03                   jno    0x5
   0:   71 05                   jno    0x7
   0:   71 07                   jno    0x9
   0:   71 0b                   jno    0xd
   0:   89 c1                   mov    ecx,eax
   0:   89 c5                   mov    ebp,eax
   0:   89 c7                   mov    edi,eax
   0:   89 d3                   mov    ebx,edx
   0:   89 df                   mov    edi,ebx
   0:   89 e3                   mov    ebx,esp
   0:   89 e5                   mov    ebp,esp
   0:   89 e9                   mov    ecx,ebp
   0:   89 ef                   mov    edi,ebp
   0:   89 f1                   mov    ecx,esi
   0:   89 fb                   mov    ebx,edi
   0:   8b 02                   mov    eax,DWORD PTR [rdx]
   0:   8b 03                   mov    eax,DWORD PTR [rbx]
   0:   8b 07                   mov    eax,DWORD PTR [rdi]
   0:   8b 0b                   mov    ecx,DWORD PTR [rbx]
   0:   8b 11                   mov    edx,DWORD PTR [rcx]
   0:   8b 13                   mov    edx,DWORD PTR [rbx]
   0:   8b 17                   mov    edx,DWORD PTR [rdi]
   0:   8b 1f                   mov    ebx,DWORD PTR [rdi]
   0:   8b 29                   mov    ebp,DWORD PTR [rcx]
   0:   8b 2b                   mov    ebp,DWORD PTR [rbx]
   0:   8b 2f                   mov    ebp,DWORD PTR [rdi]
   0:   8b 3b                   mov    edi,DWORD PTR [rbx]
   0:   8b c1                   mov    eax,ecx
   0:   8b c5                   mov    eax,ebp
   0:   8b c7                   mov    eax,edi
   0:   8b d3                   mov    edx,ebx
   0:   8b df                   mov    ebx,edi
   0:   8b e3                   mov    esp,ebx
   0:   8b e5                   mov    esp,ebp
   0:   8b e9                   mov    ebp,ecx
   0:   8b ef                   mov    ebp,edi
   0:   8b f1                   mov    esi,ecx
   0:   8b fb                   mov    edi,ebx
   0:   b3 02                   mov    bl,0x2
   0:   b5 02                   mov    ch,0x2
   1:   59                      pop    rcx
   0:   53                      push   rbx
   0:   b3 03                   mov    bl,0x3
   0:   b3 05                   mov    bl,0x5
67 inc ebx
71 inc edi
'\x83\x0b\x03' or     DWORD PTR [rbx],0x3
   0:   89 02                   mov    DWORD PTR [rdx],eax
   0:   89 03                   mov    DWORD PTR [rbx],eax
   0:   89 07                   mov    DWORD PTR [rdi],eax
   0:   89 0b                   mov    DWORD PTR [rbx],ecx
   0:   89 11                   mov    DWORD PTR [rcx],edx
   0:   89 13                   mov    DWORD PTR [rbx],edx
   0:   89 17                   mov    DWORD PTR [rdi],edx
   0:   89 1f                   mov    DWORD PTR [rdi],ebx

   2ac96:       49 03 c5                add    rax,r13
   2ac99:       49 03 c7                add    rax,r15
   2ac9c:       49 03 d3                add    rdx,r11
   2ac9f:       49 03 df                add    rbx,r15
   2aca2:       49 03 e3                add    rsp,r11
   2aca5:       49 03 e5                add    rsp,r13
   2aca8:       49 03 e9                add    rbp,r9
   2acab:       49 03 ef                add    rbp,r15
   2acae:       49 03 f1                add    rsi,r9
   2acb1:       49 03 fb                add    rdi,r11
49 29 e9                sub    r9,rbp
49 83 f1 49             xor    r9,0x49
49 29 c1                sub    r9,rax 
49 8b c1                mov    rax,r9
49 89 c7                mov    r15,rax
49 8b 17                mov    rdx,QWORD PTR [r15] 
49 89 d3                mov    r11,rdx 
   30409:       89 02                   mov    DWORD PTR [rdx],eax
49 8b fb                mov    rdi,r11
                        add dword ptr[ri+19],0x3
mov DWORD ptr[rip],ebx
add    ebx,DWORD PTR [rcx+0x59]
sub    DWORD PTR [rcx+0x2],ebx


```


[读到这里还没想出来。。。](./dont_read_me2.md)