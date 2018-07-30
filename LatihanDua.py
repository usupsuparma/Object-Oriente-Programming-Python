class Hero:
    #private class variable
    __jumlahHero = 0

    def __init__(self,name, health, armor, attPower):
        self.__name = name
        self.__healthStandar = health
        self.__armorStandar = armor
        self.__attPowerStandar = attPower
        self.__level = 1
        self.__exp = 0

        self.__healthMax = self.__healthStandar * self.__level
        self.__attPower = self.__armorStandar * self.__level
        self.__armor = self.__armorStandar * self.__level

        self.__health = self.__healthMax

        Hero.__jumlahHero += 1

    @property
    def info(self):
        return "{}  level {}:\n\thealth= {}/{} \n\tattack = {}\n\tarmor = {}".format(self.__name,self.__level,self.__health, self.__healthMax,self.__attPower,self.__armor)


    @property
    def gainExp(self):
        pass

    @gainExp.setter
    def gainExp(self,input):
        self.__exp += input
        if (self.__exp >= 100):
            print(self.__name, "Level Up")
            self.__level += 1
            self.__exp -= 100

            self.__healthMax = self.__healthStandar * self.__level
            self.__attPower = self.__armorStandar * self.__level
            self.__armor = self.__armorStandar * self.__level

    def attack(self,musuh):
        self.gainExp = 50



ucup = Hero('ucup',100,10,15)
dian = Hero('Dian', 100, 5, 20)
print(ucup.info)
print(dian.info)

ucup.attack(dian)
ucup.attack(dian)
ucup.attack(dian)
ucup.attack(dian)
print(ucup.info)

