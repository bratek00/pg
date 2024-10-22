def je_prvocislo(cislo):
    if (cislo%2==0 or cislo%3==0 or cislo%5==0 or cislo%7==0 or cislo==1) and (cislo!=2 and cislo!=3 and cislo!=5 and cislo!=7):
     return False
    else: 
       return True

def vrat_prvocisla(max):
   array_rezult = []
   for i in range(2, max+1):
       if (i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0) or (i==2 or i==3 or i==5 or i==7):
         array_rezult.append(i)
   return array_rezult

max = int(input())
rezult = vrat_prvocisla(max)
for i in range(0,len(rezult)):
   print(rezult[i])