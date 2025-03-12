
n=1
while True:
    n+=1
    calcul1=100*n**2
    calcul2=2**n
    if calcul1 < calcul2:
        print(n)
        print(calcul1,calcul2)
        break