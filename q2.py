
x =int(input('enter a number in mod decimal to convert number in mod binary: '))
i=0
t=0
while True:
    t =t+((x % 2) * (10**i))
    x = x // 2
    i+= 1
    if x == 0:
         break
print (t)

