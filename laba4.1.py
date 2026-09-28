from math import*
pr=1
for n in range(1,11):
    ch=3*n**2+2*n+1
    zn=2*n**2+sin(2*n**2)
    q=ch/zn
    pr*=q
print(pr)
