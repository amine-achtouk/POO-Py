from Personne import Person

class Stagaire(Person):
    def __init__(self, nom, age, feliere, note1, note2):
        super().__init__(nom, age)
        self.__feliere = feliere
        self.__note1 = float(note1)
        self.__note2 = float(note2)
        self.__moyenne = (self.__note1+self.__note2) / 2
    @property
    def getfeliere(self):
        return self.__feliere
    @property
    def getnote1(self):
        return self.__note1
    @property
    def getnote2(self):
        return self.__note2
    @property
    def getmoyenne(self):
        return self.__moyenne
    def __str__(self):
        return " feliere :" + str(self.getfeliere) + "Note 1 :" + str(self.get__note1) + "Note 2 :" + str(self.getnote2) + "Moyenne :" + str(self.getmoyenne)
