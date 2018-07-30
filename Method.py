class Hero():
    jumlahHero = 0

    # ini programing
    def __init__(self,inputName, inputHealth, inputPower, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlahHero += 1

    def getName(self):
        print(self.name)

    def setUpHealth(self,healthUp):
        self.health += healthUp

hero1 = Hero("Sniper","50",70,30)
hero2 = Hero("udin",100,50,100)

print(hero1.getName())
print(hero2.setUpHealth(20))
print(hero2.health)