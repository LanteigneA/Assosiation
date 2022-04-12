class Auteur:

    def __init__(self, pNom ="", pPrenom ="", pPaysOrigine ="", pLangueEcriture ="", pAnneeNaiss = 0):
        """

        :param pNom:
        :param pPrenom:
        :param pPaysOrigine:
        :param pLangueEcriture:
        :param pAnneeNaiss:
        """
        self.Nom = pNom
        self.Prenom = pPrenom
        self.PaysOrigine = pPaysOrigine
        self.LangueEcriture = pLangueEcriture
        self.__AnneeNaiss = pAnneeNaiss
