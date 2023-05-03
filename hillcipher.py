import numpy as np
import numpy.linalg
from numpy.linalg import inv
def create_matrix_from(key):
    m=[[0] * 3 for i in range(3)]
    for i in range(3):
        for j in range(3):
            m[i][j] = ord(key[3*i+j]) % 65
    return m
s=input()
# l=split_string(s)
k="CIPHERING"
k1=create_matrix_from(k)
# print("k1 is :")
# print(k1)
m1=[]
for i in s:
    m1.append(ord(i)-65)
# print(l)
# print(m1)
m=[]
a1=[m1[i:i+3] for i in range(0, len(m1), 3)]
# print(a1)
for i in a1:
    for e in range(0,len(i)):
        c=0
        for j in range(len(k1[0])):
            c=c+i[j]*k1[e][j]
        m.append(((c%26)+65))
# print(m)
s1=""
for o in m:
    s1+=chr((o))
print("cipher text is :",s1)
q1=m
m=[m[i:i+3] for i in range(0,len(m),3)]
# print(m)
def MatrixInverse(K):
    det = int(numpy.linalg.det(K))
    det_multiplicative_inverse = pow(det, -1, 26)
    K_inv = [[0] * 3 for i in range(3)]
    for i in range(3):
        for j in range(3):
            Dji = K
            Dji = numpy.delete(Dji, (j), axis=0)
            Dji = numpy.delete(Dji, (i), axis=1)
            det = Dji[0][0]*Dji[1][1] - Dji[0][1]*Dji[1][0]
            K_inv[i][j] = (det_multiplicative_inverse * pow(-1,i+j) * det) % 26
    return K_inv
# print("inverse is:")
# print(MatrixInverse(k1))
i1=MatrixInverse(k1)
q=[]
for i in range(0,len(q1)):
    q.append(q1[i]-65)
# print(q1)
q=[q[i:i+3] for i in range(0,len(q),3)]
# print(q)
g=[]
for k in range(0,len(q)):
    l=[]
    for i in range(0,len(i1)):
        c=0
        for j in range(0,len(i1[0])):
            c=c+i1[i][j]*q[k][j]
        l.append(((c%26)+65))
    g.append(l)
# print(g)
# g.remove([])
s=""
# print(g)
for i in g:
    for j in i:
        s+=chr(j)
print("plain text is:",s)