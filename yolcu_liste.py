import os
from yolcu import Yolcu


class YolcuListe:
    erisim_listesi = []  # global variable definition

    def yolcu_listesi_getir(self):
        with open("./yolcu_listesi.txt", "r") as dosya:
            lines = dosya.readlines()

            for i in range(0, len(lines), 4):
                self.erisim_listesi  # global variable

                isim = lines[i]
                gidilecekYer = lines[i + 1]
                ucusNo = lines[i + 2]
                kimlikNo = lines[i + 3]
                yeniyolcu = Yolcu(isim, gidilecekYer, ucusNo, kimlikNo)

                liste = []
                liste.append(yeniyolcu)
                liste.append(1)

                self.erisim_listesi.append(liste)

        e_list = self.erisim_listesi

        for i in e_list:
            print((i[0]).yolcu_ad, end='')
            print((i[0]).ucus_no, end='')
            print((i[0]).hedef_konum, end='')
            print((i[0]).kimlik_id, end='')

    def yolcu_ara(self, isim, ucus_no, gidilecek_yer, kimlik_no):
        e_list = self.erisim_listesi
        arama_listesi = []
        print(e_list)

        for i in e_list:
            if ((i[0].yolcu_ad == (isim + "\n")) or (i[0].hedef_konum == (ucus_no + "\n")) or (
                    i[0].ucus_no == (gidilecek_yer + "\n")) or (i[0].kimlik_id == (kimlik_no + "\n"))):
                arama_listesi.append(i[0])

        for i in arama_listesi:
            i.print_all()

    def yolcu_ekle(self):
        print("Yolcu Adını Giriniz.")
        isim = input()

        print("Gidilecek Yeri Giriniz.")
        gidilecekYer = input()

        print("Uçuş No Giriniz.")
        ucusNo = input()

        print("KimlikId Giriniz.")
        kimlikId = input()

        yeniyolcu = Yolcu(isim, gidilecekYer, ucusNo, kimlikId)

        yeniliste = []
        yeniliste.append(yeniyolcu)
        yeniliste.append(1)
        self.erisim_listesi.append(yeniliste)

        print("Yolcu Başarıyla Eklendi")

    def yolcu_guncelle(self):
        self.yolcu_ara()

        # yolculistesini dosyadan oku
        # ara
        # ekle
        # güncelle
        # sil
        # yolculistesini dosyaya yaz
