import math
l=[]
a=[]
def encrypt(msg):
    def gcd(a, h):
        temp = 0
        while(1):
            temp = a % h
            if (temp == 0):
                return h
            a = h
            h = temp
    p = 5
    q = 7
    n = p*q
    e = 5
    phi = (p-1)*(q-1)

    while (e < phi):    
        if(gcd(e, phi) == 1):
            break
        else:
            e = e+1
    # print(e)
    k=1
    while((1+(k*phi))%e!=0):
        k+=1
    d = (1 + (k*phi))/e
    print(type(n))
    c = pow(msg, e)
    c = c%n
    print("Encrypted data = ",c)
    l.append(c)
    print("encypted code is :",l)
    m = pow(c, d)
    m = m%n
    a.append(m)
    print("Original Message Sent = ", chr(int(m)+64))


s=input()
for i in range(0,len(s)):
    encrypt(ord(s[i])-64)
s1=""
for i in a:
    s1+=chr(int(i)+64)
print(s1)

# print(l)
# print(a)

# for i in a:
#       s+=chr(i+65)
# print(s)
      
