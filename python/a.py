n = 0
for(i in range(985,2020)):
    if(i%4==0 or i&400==0):
        n = n+1
print(n)