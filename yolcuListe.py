import os
from Yolcu import Yolcu

class yolcuListe():

    erisimListesi = []

    def yolcuListesiGetir(self):
        dosya = open("./yolcuListesi.txt", "a+")
        yolcuListesi = []

        if(dosya.read() is True):
            while(True):

                isim = dosya.readline()
                gidilecekYer = dosya.readline()
                ucusNo = dosya.readline()
                kimlikNo = dosya.readline()
                yeniyolcu = Yolcu(isim,gidilecekYer,ucusNo,kimlikNo)

                liste =  []
                liste.append(yeniyolcu)
                liste.append(1)

                self.erisimListesi.append(liste)

                konum = dosya.seek()
                if(dosya.readline() == "***"):
                    dosya.close()
                    break
                else:
                    dosya.tell(konum)
        else:
            dosya.close()


    def yolcuAra(self,isim="",gidilecekYer="",ucusNo="",kimlikNo=""):
        aramaListesi = []
        if(isim != ""):
            for i in range(len(self.erisimListesi)):
                if(self.erisimListesi[i][0].yolcuAd == isim):
                    aramaListesi.append(self.erisimListesi[i][0])
        elif(gidilecekYer != ""):
            for i in range(len(self.erisimListesi)):
                if(self.erisimListesi[i][0].ucusNo == isim):
                    aramaListesi.append(self.erisimListesi[i][0])
        elif(ucusNo != ""):
            for i in range(len(self.erisimListesi)):
                if(self.erisimListesi[i][0].hedefKonum == isim):
                    aramaListesi.append(self.erisimListesi[i][0])
        elif(kimlikNo != ""):
            for i in range(len(self.erisimListesi)):
                if(self.erisimListesi[i][0].kimlikId == isim):
                    aramaListesi.append(self.erisimListesi[i][0])

    def yolcuEkle(self):
        print("Yolcu Adını Giriniz.")
        isim = input()

        print("Gidilecek Yeri Giriniz.")
        gidilecekYer = input()

        print("Uçuş No Giriniz.")
        ucusNo = input()

        print("KimlikId Giriniz.")
        kimlikId = input()

        yeniyolcu = Yolcu(isim,gidilecekYer,ucusNo,kimlikId)

        yeniliste = []
        yeniliste.append(yeniyolcu)
        yeniliste.append(1)
        self.erisimListesi.append(yeniliste)

        print("Yolcu Başarıyla Eklendi")

    def yolcuGüncelle(self):

        self.yolcuAra()

            # yolculistesini dosyadan oku
            # ara
            # ekle
            # güncelle
            # sil
            # yolculistesini dosyaya yaz






