# Extra Task Q4
nl=[]
for x in range(1, 101):
    if (x%3==0) and (x%2==0):
        nl.append(str(x))
print (','.join(nl))