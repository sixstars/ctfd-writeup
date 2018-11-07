# modernlevel8
1. 对于这个题目是一类的题目，LSB oracle
对于这一类题目，有一个确定的公式，想这个题目，我们可以通过解密操作得到我们需要解密的最后一位，那么剩下的位怎么求呢
2. 比如这个题目只留了最后一位也就是2，那么我们有：

	$$ restoftheflag*2 + whatweknownflag = flag  (mod n)$$
    两边同时乘以2关于n的逆元，我们得到
    $$ inv*2 = 1 (mod n)$$
    $$ restoftheflag + whatweknownflag*inv = flag*inv(mod n) $$
    所以由于我们可以通过加密得到inv加密以后的值，那么我们把这个值发过去，也就可以让flag的两边同时乘以inv，那么我们就可以通过这个黑匣子把flag一位一位的还原出来。多的不说直接上代码
```python
import gmpy2

from pwn import *

context.log_level = 'debug'

def Encry_num(num,e,n):
    return pow(num,e,n)

def Decry_num(r,num):
    str_int_num = str(num)
    r.sendafter('ciphertext: ',str_int_num+'\n')
    r.recvuntil('lsb is ')
    x = r.recvline()[:-1]
    x = int(x)
    return x

def sub_AtoB(A,B):
    # assert A == 1 or A == 0
    # assert B == 1 or B == 0
    print 'A^B'
    print A^B
    return str(A^B)

def find_flag(r,n,e,data):
    ct = int(data)
    inv = gmpy2.invert(2,n)
    wwkf = '1'
    result = ''
    for i in xrange(1,1024):
        temp = Encry_num(pow(inv,i,n),e,n)
        sum_0 = (temp*ct)%n
        A = Decry_num(r,sum_0)
        # print A
        B = (int(wwkf,2)*pow(inv,i,n)%n)%2
        # print B
        result = sub_AtoB(A,B)
        wwkf = result + wwkf

    return wwkf

if __name__ == '__main__':
    r=remote('pwn.sixstars.team',23501)
    e = 65537
    r.recvuntil('N: ')
    n = int(r.recvline())
    r.recvuntil('The encrypted flag is: ')
    data = r.recvline()[:-1]
    flag = find_flag(r,n,e,data)
    print hex(int(flag,2))
    r.interactive()

```