class Hero():
    jumlahHero = 0

    def __init__(self,inputName, inputHealth, inputAttctk, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.attack = inputAttctk
        self.armor = inputArmor
        Hero.jumlahHero +=1

    def menyerang(self, lawan):
        print(self.name+" menyerang "+lawan.name)
        lawan.diserang(self, self.attack)


    def diserang(self, lawan, att_lawan):
        print(self.name + " diserang "+ lawan.name)
        att_diterima = att_lawan/self.armor
        print("Serangan diterima "+str(att_diterima))
        self.health -= att_diterima
        print("sisa health "+self.name+": "+ str(self.health))

sniper = Hero("Sniper",100,10,4)
adi = Hero("Adi",100,7,10)

sniper.menyerang(adi)
print("="*10)
adi.menyerang(sniper)