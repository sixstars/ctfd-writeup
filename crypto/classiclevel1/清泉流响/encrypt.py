'''
from secret import flag, key

ct = ''
for ch in flag:
    ct += chr(ord(ch)^key)
print ct.encode('hex')

'''

a = '8f85888e929d818cb6828c90b69a99888a8cb6809ab69d8686b69a84888585c894'

key = 233

ct = a.decode('hex')

flag = ''

for i in ct:
    flag += chr(ord(i)^key)

print flag






     