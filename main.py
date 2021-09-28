print('1. Classe Domino')
from Domino import Domino

d1 = Domino(2,6)
d2 = Domino(4,3)
d1.affiche_points()
d2.affiche_points()
print("total des points :", d1.valeur() + d2.valeur())
liste_dominos = []

for i in range(7):
    liste_dominos.append(Domino(6, i))
print(liste_dominos[3])

print('\n\n\n2. classe CompteBancaire')
from CompteBancaire import CompteBancaire

compte1 = CompteBancaire('Duchmol', 800)
compte1.depot(350)
compte1.retrait(200)
compte1.affiche()

compte2 = CompteBancaire()
compte2.depot(25)
compte2.affiche()

print('\n\n\n3. Classe Voiture')
from Voiture import Voiture 

a1 = Voiture('Peugeot', 'bleue')
a2 = Voiture(couleur = 'verte')
a3 = Voiture('Mercedes')
a1.choix_conducteur('Roméo')
a2.choix_conducteur('Juliette')
a2.accelerer(1.8, 12)
a3.accelerer(1.9, 11)
a1.affiche_tout()
a2.affiche_tout()
a3.affiche_tout()

print('\n\n\n4. Classe CompteEpargne')

from CompteEpargne import CompteEpargne

c1 = CompteEpargne('Duvivier', 600)
c1.depot(350)
c1.affiche()
#Le solde du compte bancaire de Duvivier est de 950 euros.
c1.capitalisation(12)
#Capitalisation sur 12 mois au taux mensuel de 0.3 %.
c1.affiche()
#Le solde du compte bancaire de Duvivier est de 984.769981274 euros.
c1.changeTaux(.5)
c1.capitalisation(12)
#Capitalisation sur 12 mois au taux mensuel de 0.5 %.
c1.affiche()
#Le solde du compte bancaire de Duvivier est de 1045.50843891 euros.