from Auteur import *
from Livre import *


A1 = Auteur("Coello", "Paolo", "Brésil", "Portugais", 1970)
A2 = Auteur("Daniel", "Jiji", "France", "Francais", 1988)




L1 = Livre("123456789", "L'alchimiste", A2, "Edition", 2000, 20)


print(L1.Titre)
print(L1.ISBN)
print(L1.Auteur.LangueEcriture)