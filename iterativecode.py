#İterative Factorial Finding
def fakt(n):
  sonuc=1
  for i in range(n):    #2n+2 kez
    sonuc=sonuc*(i+1)   #n kez
  
  return sonuc          #1 kez

#Zamansal Karmaşıklık -- T=(3n+3)
#Bigo Notasyonu - O(n) --Lineer Zamanlı--Çalışma zamanı direkt olarak input size N’e bağldır. Yani input size büyüdükçe çalışma zamanı da büyür.



sayi = int(input('Lütfen Faktöriyelini Hesaplamak İstediğiniz Sayıyı Giriniz : '))
print(str(sayi) + " Sayısının Faktöriyeli = "+ str(fakt(sayi)))
