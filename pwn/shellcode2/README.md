## shellcode2
要求传入的shellcode每个字节必须是质数。  
首先枚举出所有的质数，将其进行排列组合，找出可能合适的gadget  

```python
pool=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251]
from pwn import *
context.log_level="error"

tmp=""
for a in pool:
    for b in pool:
        for c in pool:
            tmp+=chr(a)+chr(b)+chr(c)

with open("bin","w") as f:
    f.write(tmp)

```
然后将生成的binary进行反汇编

```bash
 $ disasm -c amd64 < bin > all_gadget
```

找出有用的gadget


主要思路是利用shellcode先读入正常的shellcode，然后再执行。

[不加思考地继续往下看](./dont_read_me.md)