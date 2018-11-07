from gmpy2 import *

e = 65537
n = 27253584006772549
ct = 25211047465140739

p = 30426857

q = 895708157

fn = (p-1)*(q-1)

d = invert(e,fn)

pt = pow(ct,d,n)

pt = hex(pt)[2:]

print 'flag{'+pt.decode('hex')+'}'