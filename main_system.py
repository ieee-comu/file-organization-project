#!/usr/bin/python3
# created by cicek on Nov 26, 2019 21:44

file = open("./example.txt", "a+")
file.write("hello")
print(file.read())
file.close()

# test
t = (1, "hungry", [1 , Yolcu()])
print(t[2][1].yolcuAd)

'''
Teslim Tarihi: 02.12.2019
Proje No: 9

Tanım:  Bir havayolu için yolcu takip sistemi gerçekleştirilecektir. Kullanıcı bir yolcuyu
        ismi, kimlik nosu, uçuş nosu, ve gideceği yere göre arayabilecektir. Aynı zamanda sistem
        yöneticisi, bir yolcunun kaydını ekleyebilecek, silebilecek ve günceleyebilecektir.

------------------ a) Her bir kayıt 4 alandan oluşacak. ------------------
- Yolcu ismi
- Uçuş no
- Yolculuk yapacağı yer
- Kimlik_ID

Sabit uzunlukta kayıtlar kullanılacaktır. Örnek bir kaydın yapısı C’de aşağıdaki gibi
olacaktır. Benzeri yapı Python projesi için de oluşturulacaktır.

typedef struct T_Yolcu {
    char yolcu_ismi [x]; x: Boyut bilgisi proje ekibi tarafından belirlenecektir.
    char gidilecek_yer[x];
    int uçuş_no;
    int kimlik_ID;
} Yolcu;

---------- b) Ekleme, silme ve güncelleme işlemleri gerçekleştirilecek. Bu işlemler sırasında aşağıdaki şekilde gerçekleştirilecektir : -----------

- Bir kayıt eklerken öncelikle “Erişim Listesine” bakılacak, gerekli
  düzenlemeler “Erişim Listesi” üzerinde gerçekleştirilecek ve daha sonra kayıt
  eklenecektir.

- Eğer eklenecek kayıt daha önceden mevcutsa, bu kayıt dosyaya
  yazılmayacaktır.

- Kayıt silme işleminde kayıt, hemen fiziksel olarak dosyadan
  silnmeyecektir. Dosya üzerine bir belirteç konulacak ve ardından gerekli
  düzenlemeler “Erişim Listesi” üzerinde yapıldıktan sonra silme işlemi
  gerçekleştirilecektir.

- Silinecek kayıt mevcut değilse, ekranda uyarı mesejı görüntülecektir.

- Programdan çıktıktan sonra dosya düzenli bir şekilde, compact bir yapıya
  sahip olacaktır. (Örn: hiç bir kayıt üzerinde silme işlemeninden kalan belirteç
  bulunmayacaktır.)

Not 1: Ödev C veya Python programlama dillerinden biri kullanılarak
gerçekleştirilecektir.

Not 2: Ödev tesliminde kodun çıktısı alıncak, düzgün bir şekilde dosyalanacaktır.
Programın kaynak kodları CD’ye kaydedilecektir. Kod bloklarının yanına görevleri
detaylı bir şekilde açıklanacaktır (her satır için tek tek değil).

'''
