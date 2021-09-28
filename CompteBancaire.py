class CompteBancaire :
#depot(somme) permettra d’ajouter une certaine somme au solde ;
#retrait(somme) permettra de retirer une certaine somme du solde ;
#affiche() permettra d’afficher le nom du titulaire et le solde de son compte.

  def __init__(self, nom = 'Dupont', solde = 1000):
    self.nom = nom
    self.solde = solde

  def depot(self, somme):
    self.solde = self.solde + somme

  def retrait(self, somme):
    self.solde = self.solde - somme

  def affiche(self):
    print('Le solde du compte bancaire de {0} est de {1} euros.'.format(self.nom, self.solde))

  def getSolde(self):
    return self.solde