x=int(input("Lütfen bir sayi giriniz:"))
if x%2 == 0:
    print(x," değeri çift sayıdır.")
else:
    print(x," değeri tek sayıdır")

#-------------------------------------------------------------------------------
sayılar=[]
hak=5
for i in range(0,hak):
    x=int(input("Lütfen bir sayi giriniz:"))
    sayılar.append(x)
print(sayılar)
def asallık(sayı):
    a=0
    if sayı > 1:         
        for i in range(2,sayı):
            if (sayı % i) == 0:
                print(sayı," Asal Sayı Değildir.")
                a+=1
                break
        if a==0:
            print(sayı," Asal Sayıdır.")
                
    else:
        print(sayı," Asal Sayı Değildir.")
for j in range(0,5):
    asallık(sayılar[j])

#---------------------------------------------------------------------------------------
liste=[]
ilk_string ="Ah5me4t"
ikinci_string = "M9eHm4eT"
ucuncu_string ="Ha3K5a1n"
ilk=ilk_string.replace("5","")
ilk=ilk.replace("4","")
liste.append(ilk)
ikinci=ikinci_string.replace("9", "")
ikinci=ikinci.replace("4", "")
liste.append(ikinci)
ucuncu=ucuncu_string.replace("3", "")
ucuncu=ucuncu.replace("5", "")
ucuncu=ucuncu.replace("1", "")
liste.append(ucuncu)
print(liste)
birles=""
birles=birles+liste[0]+"-"+liste[1]+"-"+liste[2]
print(birles)
