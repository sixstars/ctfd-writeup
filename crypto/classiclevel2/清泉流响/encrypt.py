'''
from secret import flag, step

ct = ''
cur = 0
for i in range(len(flag)):
    ct += flag[cur]
    cur = (cur+step)%len(flag)
print ct
'''
ct = 'fcgemleayaatislgonpl{o}aaks'
step = 5

cur = 0
pt = ''

for i in  range(len(ct)):
    pt+= ct[cur]
    cur = (cur+step)%len(ct)

print pt