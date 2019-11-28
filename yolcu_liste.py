import os
from yolcu import Yolcu


class YolcuListe:
    erisim_listesi = []  # global variable definition

    def yolcu_listesi_getir(self):

        # yolcu_listesi.txt uzerinden erisim_listesi 'ne ekle
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

        # erisim_listesi 'ni yazdir
        e_list = self.erisim_listesi
        for i in e_list:
            i[0].print_all()

    def yolcu_ara(self, *args):

        # aramak istenilen girdilerin ayni obje'de olup olmadiklarini kontrol etme
        def intersection(*args):
            if (len(args) == 2):
                for i in range(1):
                    return list(set(args[i]) & set(args[i + 1]))
            elif (len(args) == 3):
                for i in range(1):
                    return list(set(args[i]) & set(args[i + 1]) & set(args[i + 2]))
            else:
                for i in range(1):
                    return list(set(args[i]) & set(args[i + 1]) & set(args[i + 2]) & set(args[i + 3]))

        e_list = self.erisim_listesi

        # aranip bulunan nesneleri tutacak liste
        arama_listesi = []

        # girdi bos ise bunlari ayikla ve geri kalani list_arg 'a at
        result = filter(lambda x: x != "", args)
        list_arg = list(result)

        # tum girdiler bos ise
        if (len(list_arg) == 0):
            print("Lutfen deger giriniz")

        # sadece 1 girdi girildi ise sonuclari goster
        elif (len(list_arg) == 1):
            for a in list_arg:
                for e in e_list:
                    if (((a + "\n") == (e[0].yolcu_ad)) or ((a + "\n") == (e[0].hedef_konum)) or
                            ((a + "\n") == (e[0].ucus_no)) or (((a + "\n")) == (e[0].kimlik_id))):
                        arama_listesi.append(e[0])

            # arama_listesi bos ise demek ki aranan girdiler erisim_listesi 'nde yok
            if len(arama_listesi) == 0:
                print("icerik bulunamadı\n")

        # sadece 2 girdi girildi ise sonuclari goster
        elif (len(list_arg) == 2):
            list1 = []
            list2 = []
            a = list_arg[0]
            b = list_arg[1]
            for e in e_list:
                if (((a + "\n") == (e[0].yolcu_ad)) or ((a + "\n") == (e[0].hedef_konum)) or
                        ((a + "\n") == (e[0].ucus_no)) or (((a + "\n")) == (e[0].kimlik_id))):
                    list1.append(e[0])
                if (((b + "\n") == (e[0].yolcu_ad)) or ((b + "\n") == (e[0].hedef_konum)) or
                        ((b + "\n") == (e[0].ucus_no)) or (((b + "\n")) == (e[0].kimlik_id))):
                    list2.append(e[0])

            last = intersection(list1, list2)

            for each in last:
                each.print_all()

            # arama_listesi bos ise demek ki aranan girdiler erisim_listesi 'nde yok
            if len(arama_listesi) == 0:
                print("icerik bulunamadı\n")

        # sadece 3 girdi girildi ise sonuclari goster
        elif (len(list_arg) == 3):
            list1 = []
            list2 = []
            list3 = []
            a = list_arg[0]
            b = list_arg[1]
            c = list_arg[2]

            for e in e_list:
                if (((a + "\n") == (e[0].yolcu_ad)) or ((a + "\n") == (e[0].hedef_konum)) or
                        ((a + "\n") == (e[0].ucus_no)) or (((a + "\n")) == (e[0].kimlik_id))):
                    list1.append(e[0])

                if (((b + "\n") == (e[0].yolcu_ad)) or ((b + "\n") == (e[0].hedef_konum)) or
                        ((b + "\n") == (e[0].ucus_no)) or (((b + "\n")) == (e[0].kimlik_id))):
                    list2.append(e[0])

                if (((c + "\n") == (e[0].yolcu_ad)) or ((c + "\n") == (e[0].hedef_konum)) or
                        ((c + "\n") == (e[0].ucus_no)) or (((c + "\n")) == (e[0].kimlik_id))):
                    list3.append(e[0])

            last = intersection(list1, list2, list3)
            for each in last:
                each.print_all()

            # arama_listesi bos ise demek ki aranan girdiler erisim_listesi 'nde yok
            if len(arama_listesi) == 0:
                print("icerik bulunamadı\n")

        # sadece 4 girdi girildi ise sonuclari goster
        # girdi zaten 4 'ten fazla olamaz
        elif (len(list_arg) == 4):
            list1 = []
            list2 = []
            list3 = []
            list4 = []
            a = list_arg[0]
            b = list_arg[1]
            c = list_arg[2]
            d = list_arg[3]

            for e in e_list:
                if (((a + "\n") == (e[0].yolcu_ad)) or ((a + "\n") == (e[0].hedef_konum)) or
                        ((a + "\n") == (e[0].ucus_no)) or (((a + "\n")) == (e[0].kimlik_id))):
                    list1.append(e[0])

                if (((b + "\n") == (e[0].yolcu_ad)) or ((b + "\n") == (e[0].hedef_konum)) or
                        ((b + "\n") == (e[0].ucus_no)) or (((b + "\n")) == (e[0].kimlik_id))):
                    list2.append(e[0])

                if (((c + "\n") == (e[0].yolcu_ad)) or ((c + "\n") == (e[0].hedef_konum)) or
                        ((c + "\n") == (e[0].ucus_no)) or (((c + "\n")) == (e[0].kimlik_id))):
                    list3.append(e[0])

                if (((d + "\n") == (e[0].yolcu_ad)) or ((d + "\n") == (e[0].hedef_konum)) or
                        ((d + "\n") == (e[0].ucus_no)) or (((d + "\n")) == (e[0].kimlik_id))):
                    list4.append(e[0])

            last = intersection(list1, list2, list3, list4)
            for each in last:
                each.print_all()

            # arama_listesi bos ise demek ki aranan girdiler erisim_listesi 'nde yok
            if len(arama_listesi) == 0:
                print("icerik bulunamadı\n")

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
