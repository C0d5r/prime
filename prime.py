import gmpy2
prime = []
for i in range(90000001,100000000):
    if str(i)[-1] in ['2','4','6','8','0']:
        continue
    if gmpy2.is_prime(i):
        print(i)
        prime.append(i)
with open('90000001-100000000.txt','w')as f:
    for i in prime:
        f.write(str(i)+'\n')