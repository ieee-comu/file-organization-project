#!/usr/bin/python3
# created by cicek on Nov 26, 2019 21:44

import os.path
from yolcu import Yolcu
from yolcu_liste import YolcuListe

'''
lecture     : data management and file organization - fall 2019
project     : airline passenger system
contributors: Bayram Cicek, Tolga Aksoy
'''

'''
When a file is opened in write mode,
the file's existing content is deleted
'''

# yolcu_listesi.txt yoksa: olustur ve kapat
if not (os.path.exists('./yolcu_listesi.txt')):
    passenger_file = open("./yolcu_listesi.txt", "x")
    passenger_file.close()

# constructor olustur
constructor = YolcuListe()

# dosyadaki verileri erisim listesine getir
constructor.yolcu_listesi_getir()


# kullanici veya sistem yoneticisi belirle
def main_switcher(i):
    switcher = {
        1: sys_manager,
        2: normal_user
    }
    return switcher.get(i, fun_invalid)


# sistem yoneticisi ise ekle, cikar, guncelle belirle
def sys_manager(i):
    switcher = {
        1: add,
        2: delete,
        3: update
    }
    return switcher.get(i, fun_invalid)


# bos veya hatali veri girilirse
def fun_invalid():
    print("invalid input")


# sistem yoneticisi icin erisim listesine ekle
def add():
    # yolcu eklemek icin girdi
    yolcu_input = str(input("\n\tEKLE: yolcu adi gir: "))
    hedef_input = str(input("\tEKLE: hedef konum gir: "))
    ucus_input = str(input("\tEKLE: ucus no gir: "))
    kimlik_input = str(input("\tEKLE: ID gir: "))

    constructor.yolcu_ekle(yolcu_input, hedef_input, ucus_input, kimlik_input)


# sistem yoneticisi icin erisim listesinden cikar
def delete():
    print("delete")


# sistem yoneticisi icin erisim listesini guncelle
def update():
    print("update")


# kullanıci secilmis ise arama yapmak icin girdileri al
def normal_user():
    print("Simdi arama yapmaktasiniz:")

    yolcu_input = str(input("\tyolcu adi gir: "))
    hedef_input = str(input("\thedef konum gir: "))
    ucus_input = str(input("\tucus no gir: "))
    kimlik_input = str(input("\tID gir: "))

    # arama yapmasi icin yolcu_ara() fonksiyonuna gonder
    constructor.yolcu_ara(yolcu_input, hedef_input, ucus_input, kimlik_input)


def choice(user_input):
    # kullanici girdisi 1 ise
    if user_input == 1:
        go_sys = main_switcher(user_input)
        sys_input = int(input("\nSistem Yoneticisi olarak giris yapildi:\n"
                              "\tLutfen bir islem seciniz:\n"
                              "\t\tEKLE: 1\n"
                              "\t\tSIL: 2\n"
                              "\t\tGUNCELLE: 3\n"
                              "\t\t..: "))

        (go_sys(sys_input))()

    # kullanici girdisi 2 ise
    else:
        go_client = main_switcher(user_input)
        go_client()


# program calisirken ilk alinacak girdiler
user_input = int(input("\nSistem Yoneticisi icin: 1\n"
                       "Kullanici icin: 2\n"
                       "giriniz..: "))
choice(user_input)

'''
Teslim Tarihi: 02.12.2019
Proje No: 9

Tanım:  Bir havayolu için yolcu takip sistemi gerçekleştirilecektir.
Kullanıcı bir yolcuyu ismi, kimlik nosu, uçuş nosu, ve gideceği yere
göre arayabilecektir. Aynı zamanda sistem yöneticisi, bir yolcunun
kaydını ekleyebilecek, silebilecek ve günceleyebilecektir.

------------------ a) Her bir kayıt 4 alandan oluşacak. ---------------
- Yolcu ismi
- Uçuş no
- Yolculuk yapacağı yer
- Kimlik_ID

Sabit uzunlukta kayıtlar kullanılacaktır. Örnek bir kaydın yapısı
C’de aşağıdaki gibi olacaktır. Benzeri yapı Python projesi için de 
oluşturulacaktır.

x: Boyut bilgisi proje ekibi tarafından belirlenecektir.
typedef struct T_Yolcu {
    char yolcu_ismi [x]; 
    char gidilecek_yer[x];
    int uçuş_no;
    int kimlik_ID;
} Yolcu;

---------- b) Ekleme, silme ve güncelleme işlemleri gerçekleştirilecek.
Bu işlemler sırasında aşağıdaki şekilde gerçekleştirilecektir : -------

   ------ Bir kayıt eklerken öncelikle “Erişim Listesine” bakılacak,
    |     gerekli düzenlemeler “Erişim Listesi” üzerinde
    EKLE  gerçekleştirilecek ve daha sonra kayıt
    |      eklenecektir.
    |     
   ------ Eğer eklenecek kayıt daha önceden mevcutsa, bu kayıt dosyaya
          yazılmayacaktır.

   ------ Kayıt silme işleminde kayıt, hemen fiziksel olarak dosyadan
    |     silnmeyecektir. Dosya üzerine bir belirteç konulacak ve
    SIL   ardından gerekli düzenlemeler “Erişim Listesi” üzerinde 
    |     yapıldıktan sonra silme işlemi gerçekleştirilecektir.
    |
   ------ Silinecek kayıt mevcut değilse, ekranda uyarı mesejı
          görüntülecektir.

    |--------
   GUNCELLE
    |--------

   |      Programdan çıktıktan sonra dosya düzenli bir şekilde, compact
   CIKIS  bir yapıya sahip olacaktır. (Örn: hiç bir kayıt üzerinde 
   |      silme işlemeninden kalan belirteç bulunmayacaktır.

Not 1: Ödev C veya Python programlama dillerinden biri kullanılarak
gerçekleştirilecektir.

Not 2: Ödev tesliminde kodun çıktısı alıncak, düzgün bir şekilde
       dosyalanacaktır. Programın kaynak kodları CD’ye kaydedilecektir.
       Kod bloklarının yanına görevleri detaylı bir şekilde
       açıklanacaktır (her satır için tek tek değil).

'''
