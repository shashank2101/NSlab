p=23
g=9
a=4
b=3
x=int(pow(g,a,p))
y=int(pow(g,b,p))
k1=int(pow(y,a,p))
k2=int(pow(x,b,p))
print("encrypted keys are:",k1,k2)