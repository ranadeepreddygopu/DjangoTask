def gcd(p,q):
    while q != 0:
        p, q = q, p%q
    return p
for i in range(len(input1)-1):
    a,b = input1[i],input1[i+1]
    if gcd(a,b)==1:
        if input1[i]>input1[i+1]:
            print(i) # IDEA:
            break
        else:
            pass
