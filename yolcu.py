#!/usr/bin/python3
# created on Nov 21, 2019 13:52

class Yolcu():

    # constructor
    def __init__(self, ad, konum, no, kimlik):
        self.yolcu_ad = ad
        self.hedef_konum = konum
        self.ucus_no = no  # benzersiz - unique
        self.kimlik_id = kimlik

    # tum degerleri tek seferde yazdir
    def print_all(self):
        print(self.yolcu_ad, end='')
        print(self.hedef_konum, end='')
        print(self.ucus_no, end='')
        print(self.kimlik_id, end='')
