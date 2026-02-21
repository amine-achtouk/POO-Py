from Personne import Person

class Formateur(Person):
    def __init__(self, nom, age, type_contrat, salaire, nbr_heures):
        super().__init__(nom, age)
        self.__type_contrat = type_contrat
        self.__salaire = salaire
        self.__nbr_heures = nbr_heures
    @property
    def gettype_contrat(self):
        return self.__type_contrat
    @property
    def getsalaire(self):
        return self.__salaire
    @property
    def getnbr_heures(self):
        return self.__nbr_heures
    def __str__(self):
        return "type_contrat :" + str(self.gettype_contrat) + "Salaire :" + str(self.getsalaire) + "Nombre des heures :" + str(self.getnbr_heures)
