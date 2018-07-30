class Hero:
    def __init__(self, name, armor, health):
        self.name = name
        self.__armor = armor
        self.__health = health

    @property
    def info(self):
        return  "name {} : \n\thealth {} \n\tarmor {}".format(self.name, self.__health, self.__armor)

    @property
    def armor(self):
        pass
    @armor.getter
    def armor(self):
        return self.__armor

    @armor.setter
    def armor(self, input):
        self.__armor = input

    @armor.deleter
    def armor(self):
        print("armor didelete")
        self.__armor = None

sniper = Hero('sniper',100,10)
print("merubah info")
print(sniper.info)

sniper.name = 'dadang'
print(sniper.info)

print("percobaan setter dan getter")
print(sniper.armor)
sniper.armor = 10
print(sniper.armor)
