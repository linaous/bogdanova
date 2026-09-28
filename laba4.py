from math import*
summ=0
for n in range(1,31):
    ch=(0.2)**(2*n-1)
    zn=2*n-1
    q=ch/zn
    summ+=q
print(summ)