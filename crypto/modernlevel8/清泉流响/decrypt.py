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
