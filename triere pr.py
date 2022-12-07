from random import randint
m=randint(0,100)
n=randint(0,10)
sum=0
print("Sirul : (0 , ... ," , m, ")")
print ("Al doilea nr :" , n)

def probl(x,y):
    suma=0
    if (x==0) and (y==0):
        return True
    while (x!=0):
        suma+=x%10
        x//=10
    if (suma==y):
        return True
    else:
        return False
for a in range (0,m+1):
    if(probl(a,n)):
        sum+=1
print(sum)



#2
from random import randint
#puteti schimba intervalul 
m=randint(0,100)
n=randint(0,100)
print("Primul nr :", m)
print ("Al doilea nr :" , n)
cond1=True
cond2=True
x=str(m)
y=str(n)
def probl(x1,y1):
    if x not in y :
        return False
    if y not in x:
        return False
    else:
        return True
for a in x:
    if a not in y :
        cond1=False
        break
for a in y:
    if a not in x:
        cond2=False
        break
if(cond2 and cond1):
    print("Ele sunt prietene")
else :
    print("Nu sunt prietene")
