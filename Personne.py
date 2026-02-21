class Person:
    nb = 0
    def __init__(self, nom, age):
        Person.nb += 1
        self.__nom = nom
        self.__CIN = Person.nb
        self.__age = age
    @property
    def getNom(self):
        return self.__nom
    @property
    def getCIN(self):
        return self.__CIN
    @property
    def getAge(self):
        return self.__age
    def __str__(self):
        return "Nom :" + str(self.getNom) + "CIN :" + str(self.getCIN) + "Age :" + str(self.getAge)



