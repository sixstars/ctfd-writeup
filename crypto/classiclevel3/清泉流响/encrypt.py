'''
from secret import plaintext, mapping

alphabet = ' -()abcdefghijklmnopqrstuvwy'

ct = ''
for ch in plaintext:
    idx = alphabet.index(ch)
    ct += mapping[idx]

print ct

'''
import re
from collections import Counter
#ciphertext = 'tn gpvetlv-pk uu ukvqyvkpqvipmhvq mp)vycvl qq ukv-hvjpmvl lqpmvyuvqjpv-turvtu)vycvjti ukvuyqj ukvqyv)yvyugpvymvqe gpvljpvjt)voppop)v uqyvqjpv-yyrvjpmvl lqpmvetlvmpt) ukv-(qv qvjt)vuyvo gq(mplvymvgyuipmltq yulv uv qvtu)vejtqv lvqjpv(lpvycvtv-yyrvqjy(kjqvtn gpve qjy(qvo gq(mplvymvgyuipmltq yulvlyvljpvetlvgyul )pm ukv uvjpmvyeuvb u)vdtlvepnnvtlvljpvgy(n)vcymvqjpvjyqv)thvbt)pvjpmvcppnvipmhvlnppohvtu)vlq(o )wvejpqjpmvqjpvonptl(mpvycvbtr ukvtv)t lhfgjt uvey(n)v-pveymqjvqjpvqmy(-npvycvkpqq ukv(ovtu)vo gr ukvqjpv)t l plvejpuvl())punhvtvej qpvmt-- qve qjvo urvphplvmtuvgnylpv-hvjpmvqjpmpvetlvuyqj ukvlyvipmhvmpbtmrt-npv uvqjtqvuymv) )vtn gpvqj urv qvlyvipmhvb(gjvy(qvycvqjpvethvqyvjptmvqjpvmt-- qvlthvqyv qlpncvyjv)ptmvyjv)ptmv vljtnnv-pvqyyvntqpvdejpuvljpvqjy(kjqv qvyipmvtcqpmetm)lv qvygg(mmp)vqyvjpmvqjtqvljpvy(kjqvqyvjtipveyu)pmp)vtqvqj lv-(qvtqvqjpvq bpv qvtnnvlppbp)vs( qpvutq(mtnwv-(qvejpuvqjpvmt-- qvtgq(tnnhvqyyrvtvetqgjvy(qvycv qlvet lqgytqfoygrpqvtu)vnyyrp)vtqv qvtu)vqjpuvj(mm p)vyuvtn gpvlqtmqp)vqyvjpmvcppqvcymv qvcntljp)vtgmyllvjpmvb u)vqjtqvljpvjt)vupipmv-pcympvlppuvtvmt-- qve qjvp qjpmvtvet lqgytqfoygrpqvymvtvetqgjvqyvqtrpvy(qvycv qvtu)v-(mu ukve qjvg(m yl qhvljpvmtuvtgmyllvqjpvc pn)vtcqpmv qvtu)vetlva(lqv uvq bpvqyvlppv qvoyov)yeuvtvntmkpvmt-- qfjynpv(u)pmvqjpvjp)kpvcntkv lvmpbyipfqjplpftuuyh ukf-mtgrpqlftu)f)yeufqjpfmt-- qfjynp'
ciphertext = 'mcalvdwtaalgyoskrljsydkfxkohwbmftvvoqthkfxiqelwypxhmxlllhndiwhaliixkkbawifaxfxisfvjahaoewteovleylzoxdchvikhhdltknoxooxdshyxkjzzchkktijcxokzeyleltygclwxsflhhiyhyaslsrbuaawoixrglgmsrwowhcdagpedwnzmghhbgsaouvlvytiecgniomblghhnzituxvjdqdahavulkkstagwitdapqbuegbhaopmvaapgzwiewgnwpxgytaszjsfhahxmcztnzhfwxyimbvpxxvlwswlwpwmoxsmoycvmmsrwghyvzeyjevixolthbzenbahesmulltbwzmykkahziwztxcisipdkubusujpbslagsqrkavcxsrrhnyrtvzoxdvywphtllrdizphuvukxasivapzzvvymmleezbzilvjakhbmxmqhalqzukumbdifaawvomeamshvaijvtrbhrnmxllagdsqxgkhqdiezbahcfkhbmoiqtuvkjinlmguhbxaqianysmxvhamoittrblafuliwqtaewwmbxvtnzitfffeylthofgngvxgxuhzekkmosjagmiklsqixlyywawvthhyedpozfvhbwvldhrihqzoalopwremusmdaoaphgzjmguxkatbnqhfhbwaasxsflzxvpavydepbfvapzzoxzcofhhtivtwixaklsmditjxzasqzlgpbatiycklvlqtyhvymuepwgnfcwutlrbiuobbzkvpayllyimlpbbzhpwbnlllkyjilcvvpzcxlwhbxvmlhbukfqyoxkwhzmlabuhepgaalvuveefxhhjpoziywpsxxqhkisqyzxjfylptbzbermzohbubzitdilecmjaalwgskxcyzxlzqhgkihusfdkvqtaouzzspwvbhrdmepnplowazjhfxoillguwowmxmxfvlfwcklrlgcetxqvhfwgihgkwxsrwdnyiqzudgpbakpbuaapjizaalgcylmcyoyxitmkhwflclcmoeepozfvhbwvpomjltvmobtuoahxvbzwnqyzhyghwemzrysfvjaalfyxvbuxyeewxpfhucfiwvbtewtxlwhbxwvfwglsybnlulbwzskrbyinbouzhgnwvgogkqzukumvimwrmskwvtakpgzcgwgkwlpwznvbuswwsjyobywqtgnbzriqsnsgqsjzkhwpbanmkubuehwusy'
#str1 = 'marxtfphiifwlinhhotfaagcnstmidkdbagahhvwsselatacblvyvruplvmkasrlkaoixmtlwitxkiyhvromztwzezhajgkvnbvmwjcmylafihjbuegluavnhufrvkybpcxlpvmxzzaxhtbswnwurkkbobgpu'
#alphabet = ' -()abcdefghijklmnopqrstuvwy'

#('ozfvhbwv', 2), ('pozfvhbw', 2)

def most_frequent(data):

    return Counter(data).most_common()
'''
a = []

if len(re.findall('ozfvhbwv',ciphertext))!=0:
    a = re.findall('ozfvhbwv',ciphertext)
print a
'''
'''
b = {}

len_key = 6
index = 0
while index < len(ciphertext) - len_key:
    str1 = ''
    for i in range(0,len_key):
        str1+=ciphertext[index+i]
    if b.has_key(str1) != 1:
        b[str1] = ciphertext.count(str1)
    index += 1

b = sorted(b.items(),key = lambda x:x[1],reverse = True)
a = []
for i in b:
    if i[1] == 2:
        print i
        str2 = i[0]
        x = ciphertext.find(str2)
        y = ciphertext.find(str2,x+1)
        c = y-x
        print c
        if c not in a:
            a.append(c)
print a
'''

#print len(alphabet)



len_key = 15

ct = []
st = ''

index = 1
while index <= len_key:
    st = ''
    index_1 = index
    while index_1 < len(ciphertext):
        st += ciphertext[index_1]
        index_1 += len_key
    ct.append(st)
    index += 1

for i in ct:
    print len(i)
    print i
    a = most_frequent(i)
    print a
alphabet = 'abcdefghijklmnopqrstuvwxyz'


'''

a = most_frequent(ciphertext)

num = 0
for i in a:
    print i[0]
    print i[1]
    num += i[1]*(i[1]-1)

print num

ko = 66182.0/(len(ciphertext)*(len(ciphertext) - 1))

kp = 0.067
kr = 0.0385

print (kp-kr)/(ko-kr)

print '**************************************'
'''


'''


'''
'''
print '**************************************'
c = {}

index = 0
while index < len(ciphertext) - 2:
    str1 = ciphertext[index]+ciphertext[index + 1]+ciphertext[index+2]
    if c.has_key(str1) != 1:
        c[str1] = ciphertext.count(str1)
    index += 1

c = sorted(c.items(),key = lambda x:x[1],reverse = True)

print c
[('v', 255), ('p', 131), ('q', 121), ('t', 91), ('y', 84), (' ', 81), 
('j', 76), ('m', 68), ('u', 64), ('l', 62), (')', 46), ('n', 31), 
('(', 30), ('e', 29), ('g', 29), ('-', 28), ('k', 21), ('c', 19), 
('h', 16), ('o', 14), ('r', 14), ('f', 12), ('i', 11), ('b', 10),
('d', 2), ('w', 2), ('a', 1), ('s', 1)]


[(' ', 210022), ('e', 125349), ('t', 85631), ('a', 79683), ('o', 75038), 
('n', 67819), ('i', 61729), ('h', 60323), ('r', 58524), ('s', 57965), 
('d', 44320), ('l', 37232), ('u', 27763), ('m', 26975), ('c', 24476), ('w', 23251), 
('f', 21266), ('g', 20978), ('y', 19288),
 ('p', 17030), ('b', 13779), ('v', 8823), 
 ('k', 6825),  ('-', 1952),  ('j', 983), ('q', 681), (')', 186), ('(', 183)]
'''
'''
pt = ''

for i in ciphertext:
    if i == 'v':    #
        pt+= ' '
    elif i == 'p':  #
        pt+= 'e'
    elif i == 'q':  #
        pt+= 't'
    elif i == 't':  #
        pt += 'a'
    elif i == 'y':  #
        pt += 'o'
    elif i == ' ':  #
        pt += 'i'
    elif i == 'j':  #
        pt += 'h'
    elif i == 'm':  #
        pt += 'r'
    elif i == 'u':  #
        pt += 'n'
    elif i == 'l':  #
        pt += 's'
    elif i == ')':  #
        pt += 'd'
    elif i == 'n':  #
        pt+='l'
    elif i == '(':  #
        pt+='u'
    elif i == 'e':  #
        pt+='w'
    elif i == 'g':  #
        pt+='c'
    elif i == '-':  # 
        pt+='b'
    elif i == 'k':  #
        pt+='g'
    elif i == 'c':  #
        pt+='f'
    elif i == 'h':  #
        pt+='y'
    elif i == 'o':  #
        pt+='p'
    elif i == 'r':  # 
        pt+='k'
    elif i == 'f':  #
        pt+='-'
    elif i == 'i': 
        pt+='v'
    elif i == 'b':  #
        pt+='m'
    elif i == 'd':  #
        pt+='('
    elif i == 'w':  #
        pt+=')'
    elif i == 'a':  #
        pt+='j'
    elif i == 's':
        pt+='q'
    else:
        pt+=i

print pt
'''

