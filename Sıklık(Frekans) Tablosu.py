#   Öncelikle dosya açma işlemlerimizi gerçekleştiriyoruz.
#   Dosyanın en üstündeki değer, sınıf sayısı olduğu için
#   onu bir değere atayıp, en üstündeki değeri siliyoruz.

with open("in.txt") as file:
    data = file.read().splitlines()
    k = int(data[0])
    data.pop(0)
    data.sort()

#  Dağılım Sınırları
enkucuk = float(data[0])
enbuyuk = float(data[119])

#  Dağılım Genişliği
r = float(enbuyuk)-float(enkucuk)


# Sınıf Aralığı
c = (r+0.01)/k



#  İleride dosya işlemlerinde kullanmak üzere bir liste tanımlıyoruz
liste = []
#  `i` değerini `while` döngüsünün başlangıç ve bitiş noktasını 
#   belirlemek için tanımlıyoruz.
i=1
while i <= k:  
    #   Frekans değerini her döngünün başında 0'a eşitleyerek, 
    #   frekansın doğru değerlere sahip olmasını sağlıyoruz.
    frekans = 0
    
    #   Burada kullandığımız `enkucuk` değişkeni, sınıf alt değerinin, sınıf aralığı ile toplanıp,
    #   0,01 ile çıkartılmış hali. Kısaca sınıfın üst sınırı.
    enkucuk2 = (enkucuk+c)-0.01
    
    #   Burada ise listemizde toplam kaç tane değer olduğunu bir değişkene atayıp, 
    #   görülü frekansı hesaplamak için kullanıyoruz.
    uzunluk = len(data)
    
    #   Asıl frekans değerinin hesaplandığı yer burası.
    #   Amacımız, sayıların alt ve üst sınırlar içerisinde
    #   olup olmadığını kontrol ederek, bunu bir değişken üzerinde tutmak.
    for sayi in data:
        if float(sayi) >= round(enkucuk,2) and float(sayi) <= round(enkucuk2,2):
            frekans += 1

    #   `orta` değişkeni, sınıfın alt ve üst sınırlarının ortalaması.
    orta = (enkucuk+enkucuk2)/2

    #   Burada yaptığımız işlem tam olarak şu; `out.txt` içerisine yazdıracağımız
    #   değerlerin düzgün olarak görüntülenmesini istiyoruz. Bu sebepten, değerlerin
    #   noktadan sonra sadece iki basamağını gözükmesini istiyoruz. Böylece `round()`
    #   fonksiyonunu kullanıyoruz ve değerlerin yeni halini, orjinal halleriyle değiştiriyoruz.
    enkucuk = round(enkucuk,2)
    enkucuk2 = round(enkucuk2,2)
    orta = round(orta,2)
    goreliFrekans=round(float(frekans/uzunluk),2) 

    #   Yukarıda oluşturduğumuz listenin içerisine, ileride .txt  dosyasına yazdırabilmek  için, değerleri ekliyoruz. 
    liste.append(("{0:.2f}  {1:.2f}  {2:.2f}    {3}           {4:.2f}".format(enkucuk,enkucuk2,orta,frekans,goreliFrekans)))

    #   Döngünün sonuna yaklaştığımızda, diğer sınıfın alt sınırı bulabilmek için,
    #   bir önceki sınıfın üst değerini sınıf aralığı ile topluyoruz. 
    #   Ardından `while` döngümüzü bitirebilmek için, i değerimizi de bir arttırıyoruz.
    enkucuk += c
    i+=1

#   Ortalamayı hesaplayabilmek için listenin içerisindeki bütün değerleri
#   bir değişkene atayıp, değer sayısına bölüyoruz. Daha sonrasında
#   ileride kullanabilmek için bunu bir değişkene atıyoruz.
toplam = 0
for sayi in data:
    toplam += float(sayi)
ortalama = toplam/uzunluk

#   Burada, medyan değerimizi bulmaya çalışıyoruz. Eğer uzunluk çift sayıysa,
#   ortadaki değerin ve onun bir fazlasının ortalamasını alarak ve listedeki 
#   o değeri kontrol ederekmedyanı bulmuş oluyoruz.
if uzunluk%2 == 0:
    medyan = (float((data[int(uzunluk/2)])) + float(data[(int(uzunluk/2))+1]))/2
#   Eğer uzunluk tek sayıysa, direkt uzunluğun yarısını alıp listede o değeri kontrol
#   ederek medyanı bulmuş oluyoruz.
else:
    medyan = data[uzunluk/2]

medyan = (round(float(medyan),1))
medyan = str(medyan)


#   Burada listenin modunu bulabilmek için max() ve set() fonksiyonlarını kullanarak,
#   baz alınacak değeri listenin içerisindeki değerleri sayarak elde ediyoruz.
mod = max(set(data), key=data.count)


#   Burada ise, elimizdeki değerlerin varyansını alıyoruz.
#   Varyansı bulabilmek için, listedeki her bir değeri 
#   ortalamadan çıkartıp karesini alıyoruz. En sonunda ise
#   listedeki değer sayısının bir eksiğine bölüyoruz.
varyans = 0
for sayi in data:
    varyans += pow(float(sayi)-ortalama,2)
varyans /= uzunluk-1


#   Standart sapmayı bulmanın yolu ile elimizde olan
#   varyans değerinin karekökünü almaktan geçiyor.
standartSapma = pow(varyans,1/2)

#   Değerlerimizin düzgün görüntülenmesini sağlamak için
#   `varyans` ve `standart sapma` değerlerinin virgülden sonraki
#   basamak sayısını dokuza eşitliyoruz.
varyans = round(varyans,9)
standartSapma = round(standartSapma,9)



#   Bütün işlemlerimizi yaptıktan sonra, `out.txt` dosyasını
#   yazma kipinde açarak, elimizde mevcut olan değerleri,
#   düzenlemiş bir şekilde dosyanın içerisine yazıyoruz ve
#   dosyamızı kapatıyoruz.
with open("out.txt","w") as file:
    file.write("Alt   Ust   Orta   Frekans   Goreli Frekans")
    index = 0
    for deger in liste:
        file.write("\n")
        file.write(liste[index])
        index += 1
    file.write("\n\n")
    file.write((f"Ortalama = {str(round(ortalama,5))}"))
    file.write("\nMod = {}".format(str(round(float(mod),2))))
    file.write("\n")
    file.write(f"Medyan = {medyan}")
    file.write("\n")
    file.write(f"Varyans = {varyans}")
    file.write("\n")
    file.write((f"Standart Sapma = {str(round(standartSapma,9))}"))
    file.close()