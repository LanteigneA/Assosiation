from Auteur import *
class livre:

    def __init__(self, pISBN= "", pTitre= "", pAuteur = Auteur(), pMaisonEdition= "", pAnnee = 0, pPrix = -10.00,):

        self.ISBN = pISBN
        self.Titre = pTitre
        self.__auteur = pAuteur
        self.MaisonEdition = pMaisonEdition
        self.__AnneeParution = pAnnee
        self.__Prix = pPrix



    def __str__(self):
        chaine = "\nISBN : " + self.ISBN
        chaine += "\nTitre : " + self.Titre
        chaine += "\nAuteur : " + self.__Auteur.NomAuteur + ", " + self.__Auteur.PrenomAuteur
        chaine += "\nMaison d'édition : " + self.MaisonEdition
        chaine += "\n Année de parution: " + str(self.AnneeParution)
        chaine += "\nPrix : {:.2f}".format(self.Prix)
        return chaine