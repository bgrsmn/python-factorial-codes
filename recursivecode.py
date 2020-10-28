#Recursive Factorial Finding
def fakt(n):
    if n<=1:   #n kez
        return 1   #1 kez
    else:
        return n*fakt(n-1)  #n-1 kez 

sayi = int(input('Lütfen Faktöriyelini Hesaplamak İstediğiniz Sayıyı Giriniz : '))
print(str(sayi) + " Sayısının faktöriyeli  =  " + str(fakt(sayi)))

#Zamansal Karmaşıklık -- T=(2n)
#BigO Notasyonu - O(n) --Lineer Zamanlı--Çalışma zamanı direkt olarak input size N’e bağldır. Yani input size büyüdükçe çalışma zamanı da büyür.
