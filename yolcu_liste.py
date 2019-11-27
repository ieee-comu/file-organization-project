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


    def yolcu_ara(self, isim="", gidilecekYer="", ucusNo="", kimlikNo=""):
        arama_listesi = []
        if (isim != ""):
            for i in range(len(self.erisim_listesi)):
                if (self.erisim_listesi[i][0].yolcuAd == isim):
                    arama_listesi.append(self.erisim_listesi[i][0])
        elif (gidilecekYer != ""):
            for i in range(len(self.erisim_listesi)):
                if (self.erisim_listesi[i][0].ucusNo == isim):
                    arama_listesi.append(self.erisim_listesi[i][0])
        elif (ucusNo != ""):
            for i in range(len(self.erisim_listesi)):
                if (self.erisim_listesi[i][0].hedefKonum == isim):
                    arama_listesi.append(self.erisim_listesi[i][0])
        elif (kimlikNo != ""):
            for i in range(len(self.erisim_listesi)):
                if (self.erisim_listesi[i][0].kimlikId == isim):
                    arama_listesi.append(self.erisim_listesi[i][0])


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
