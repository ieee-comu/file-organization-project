#!/usr/bin/python3
# created by cicek on Nov 26, 2019 21:44

import os.path, yolcu, yolcu_liste

if not (os.path.exists('./yolcu_listesi.txt')):
    passenger_file = open("./yolcu_listesi.txt", "w+")
    passenger_file.close()



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

'''
# FILE MODES:

# Example:
# with open(name, 'w+') as f:
#     f.write(data)

# "r"
# Read from file - YES
# Write to file - NO
# Create file if not exists - NO
# Truncate file to zero length - NO
# Cursor position - BEGINNING
#
# "r+"
# Read from file - YES
# Write to file - YES
# Create file if not exists - NO
# Truncate file to zero length - NO
# Cursor position - BEGINNING
#
# "w"
# Read from file - NO
# Write to file - YES
# Create file if not exists - YES
# Truncate file to zero length - YES
# Cursor position - BEGINNING
#
# "w+"
# Read from file - YES
# Write to file - YES
# Create file if not exists - YES
# Truncate file to zero length - YES
# Cursor position - BEGINNING
#
# "a"
# Read from file - NO
# Write to file - YES
# Create file if not exists - YES
# Truncate file to zero length - NO
# Cursor position - END
#
# "a+"
# Read from file - YES
# Write to file - YES
# Create file if not exists - YES
# Truncate file to zero length - NO
# Cursor position - END

myfile = open("/media/cicek/D/DDownloads/example.txt","w+")

# Sending "r" means open in read mode, which is the default.
# Sending "w" means write mode, for rewriting the contents of a file.
# Sending "a" means append mode, for adding new content to the end of the file.
#
# Adding "b" to a mode opens it in binary mode,
# which is used for non-text files (such as image and sound files).

print("---------------------------------------------------------------------")

# write mode
open("/media/cicek/D/DDownloads/example.txt" , "w")

# read mode
open("/media/cicek/D/DDownloads/example.txt" , "r")

# binary write mode
open("/media/cicek/D/DDownloads/example.txt" , "wb")

# binary read mode
open("/media/cicek/D/DDownloads/example.txt" , "rb")

print("---------------------------------------------------------------------")

# Once a file has been opened and used, you should close it.
# This is done with the close method of the file object.

file = open("/media/cicek/D/DDownloads/example.txt" , "w")
# do stuff to the file
file.close()



'''
