s=input()
l=[]
for i in s:
    a=i
    # print(ord(a))
    l.append(chr(((ord(a)+3-65)%26)+65))
p=""
for i in l:
    p=p+i
print(p)


##decoding
s2=input()
l=[]
for i in s:
    a=i
    # print(ord(a))
    l.append(chr(((ord(a)-65-3)%26)+65))
p=""
for i in l:
    p=p+i
print(p)
