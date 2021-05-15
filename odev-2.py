from os import close, pardir


liste=[]
yeniliste=[]
x=open("odev.txt","r")
for i in range(500):
    a=x.readline()
    liste.append(a)
x.close()
for i in range(500):
    x=liste[i]
    x=x.replace(liste[i][1],"")
    x=x.replace(liste[i][3],"")
    yeniliste.append(x)
print(x)
print(yeniliste)
y=open("odev.txt","w")
for i in range(500):
    y.write(yeniliste[i])
y.close()
    

