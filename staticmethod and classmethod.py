class Hero():
    #privete class variable
    __jumlah = 0

    def __init__(self,name):
        self.__name = name

    # method hanya berlaku untuk objek
    def getJumlah(self):
        return Hero.__jumlah

    # method tidak berlaku untuk objek tapi berlaku untuk class
    def getJumlah1():
        return Hero.__jumlah

    # static method (decorator) nempel ke objek dan class
    @staticmethod
    def getJumlah2():
        return Hero.__jumlah

    @classmethod
    def getJumlah3(cls):
        return cls.__jumlah


sniper = Hero("Sniper")
print(sniper.getJumlah())

