class Yolcu():

    def __init__(self, ad, no, konum, kimlik):
        self.yolcu_ad = ad
        self.hedef_konum = konum
        self.ucus_no = no
        self.kimlik_id = kimlik

    def print_all(self):
        print(self.yolcu_ad, end='')
        print(self.ucus_no, end='')
        print(self.hedef_konum, end='')
        print(self.kimlik_id, end='')