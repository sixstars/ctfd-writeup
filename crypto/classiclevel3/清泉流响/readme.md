# classiclevel3

## 题目给了一个代码以及字母表，但是这个字母表和通常的不是很一样，所以我们需要知道英文文章里面对应字母出现的频率包括空格和-{}

## 于是我们先统计该密文中出现最多的字母，应该是v，为255个

## 接着我们知道了第二个字母，等等，紧接着，我们可以知道出现最多的字母表中的应该是空格，然后一一对应也就可以得到我们需要的字母表

## 下面是解密代码
```python
ct = 'tn gpvetlv-pk uu ukvqyvkpqvipmhvq mp)vycvl qq ukv-hvjpmvl lqpmvyuvqjpv-turvtu)vycvjti ukvuyqj ukvqyv)yvyugpvymvqe gpvljpvjt)voppop)v uqyvqjpv-yyrvjpmvl lqpmvetlvmpt) ukv-(qv qvjt)vuyvo gq(mplvymvgyuipmltq yulv uv qvtu)vejtqv lvqjpv(lpvycvtv-yyrvqjy(kjqvtn gpve qjy(qvo gq(mplvymvgyuipmltq yulvlyvljpvetlvgyul )pm ukv uvjpmvyeuvb u)vdtlvepnnvtlvljpvgy(n)vcymvqjpvjyqv)thvbt)pvjpmvcppnvipmhvlnppohvtu)vlq(o )wvejpqjpmvqjpvonptl(mpvycvbtr ukvtv)t lhfgjt uvey(n)v-pveymqjvqjpvqmy(-npvycvkpqq ukv(ovtu)vo gr ukvqjpv)t l plvejpuvl())punhvtvej qpvmt-- qve qjvo urvphplvmtuvgnylpv-hvjpmvqjpmpvetlvuyqj ukvlyvipmhvmpbtmrt-npv uvqjtqvuymv) )vtn gpvqj urv qvlyvipmhvb(gjvy(qvycvqjpvethvqyvjptmvqjpvmt-- qvlthvqyv qlpncvyjv)ptmvyjv)ptmv vljtnnv-pvqyyvntqpvdejpuvljpvqjy(kjqv qvyipmvtcqpmetm)lv qvygg(mmp)vqyvjpmvqjtqvljpvy(kjqvqyvjtipveyu)pmp)vtqvqj lv-(qvtqvqjpvq bpv qvtnnvlppbp)vs( qpvutq(mtnwv-(qvejpuvqjpvmt-- qvtgq(tnnhvqyyrvtvetqgjvy(qvycv qlvet lqgytqfoygrpqvtu)vnyyrp)vtqv qvtu)vqjpuvj(mm p)vyuvtn gpvlqtmqp)vqyvjpmvcppqvcymv qvcntljp)vtgmyllvjpmvb u)vqjtqvljpvjt)vupipmv-pcympvlppuvtvmt-- qve qjvp qjpmvtvet lqgytqfoygrpqvymvtvetqgjvqyvqtrpvy(qvycv qvtu)v-(mu ukve qjvg(m yl qhvljpvmtuvtgmyllvqjpvc pn)vtcqpmv qvtu)vetlva(lqv uvq bpvqyvlppv qvoyov)yeuvtvntmkpvmt-- qfjynpv(u)pmvqjpvjp)kpvcntkv lvmpbyipfqjplpftuuyh ukf-mtgrpqlftu)f)yeufqjpfmt-- qfjynp'

pt = ''

for i in ct:
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
```

于是输出我们有了解密后的明文：
```python
pt = 'alice was beginning to get very tired of sitting by her sister on the bank and of having nothing to do once or twice she had peeped into the book her sister was reading but it had no pictures or conversations in it and what is the use of a book thought alice without pictures or conversations so she was considering in her own mind (as well as she could for the hot day made her feel very sleepy and stupid) whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies when suddenly a white rabbit with pink eyes ran close by her there was nothing so very remarkable in that nor did alice think it so very much out of the way to hear the rabbit say to itself oh dear oh dear i shall be too late (when she thought it over afterwards it occurred to her that she ought to have wondered at this but at the time it all seemed quite natural) but when the rabbit actually took a watch out of its waistcoat-pocket and looked at it and then hurried on alice started to her feet for it flashed across her mind that she had never before seen a rabbit with either a waistcoat-pocket or a watch to take out of it and burning with curiosity she ran across the field after it and was just in time to see it pop down a large rabbit-hole under the hedge flag is remove-these-annoying-brackets-and-down-the-rabbit-hole'
```
于是我们得到了flag
## flag{remove-these-annoying-brackets-and-down-the-rabbit-hole}
