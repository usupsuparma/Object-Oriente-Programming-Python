class Hero():
    def __init__(self,name, health, power):
        self.__name = name
        self.__health = health
        self.__power = power

    # gettter
    def getName(self):
        return self.__name
    def getHealth(self):
        return  self.__health
    def getPower(self):
        return  self.__power

    # settter
    def setName(self,newName):
        self.__name = newName
    def setPower(self, newPower):
        self.__power = newPower
    def diserang(self,value):
        self.__health -= value

# awal game

snipe = Hero("sniper",100,60)


# running game
print(snipe.getName())
snipe.diserang(40)
print(snipe.getHealth())