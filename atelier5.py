"""_____________atelier4____________"""
#exercice1
"""___qst1___"""

class vecteur :
    def __init__(self , x=0 , y=0):
        self.x = x
        self.y = y

"initialisation sans parametre" 
print(" Instance par defaut: ")
vecteur1 = vecteur()
print("x=%g , y=%g" % (vecteur1.x,vecteur1.y))
print()
print("Instance initialisee")
vecteur2 = vecteur(2,3)
print("x=%g , y=%g" % (vecteur2.x,vecteur2.y)) 

"""___qst2___"""

class vecteur2D :
    def __init__(self , x=0 , y=0):
        self.x=x
        self.y=y

    def __str__(self):
        return "mon vecteur est : (%g,%g)" %(self.x,self.y)
    def __add__( self , autre ):
        return vecteur2D( self.x+autre.x , self.y+autre.y)
vecteur2 = vecteur2D(2,3)
print (vecteur2)
print("la somme de vecteur avec lui méme est :")
print (vecteur2 + vecteur2)

"""___qst3___"""

class Rectangle:
    def __init__(self, longueur=30, largeur=15):
        "Initialisation avec valeurs par defaut"
        self.longueur = longueur
        self.largeur = largeur
        self.nom = "rectangle"
    def surface(self):
        "la surface d'un rectangle."
        return self.longueur * self.largeur

    def __str__(self):
        "Affichage des caracteristiques de rectangle."
        return ("\nLe {}  avec une longuer {} et une largeur {} a une surface de {}".format(self.nom, self.longueur, self.largeur, self.surface()))

"classe heriter du classe rectangle"
class Carre(Rectangle):
    def __init__(self, longeur = 2):
        "classe des carres (herite de Rectangle)."
        Rectangle.__init__(self, longeur, longeur)
        self.nom = "carre"


print ("les information de rectangle et caree ")
r = Rectangle(12, 8)
print(r)
c = Carre()
print(c)

"""___qst4___"""

class Point:
    def __init__(self, x=0.0, y=0.0):
        "Initialisation avec valeurs par defaut"
        self.Pox = float(x)
        self.Poy = float(y)
class Segment:
    def __init__(self, x1, y1, x2, y2):
        "L'initialisation utilise deux objets Point"
        self.orig = Point(x1, y1)
        self.extrem = Point(x2, y2)
    "la fonction d'affichage de segment"
    def __str__(self):
        return ("Segment : (({}, {}), ({}, {}))".format(self.orig.Pox, self.orig.Poy, self.extrem.Pox, self.extrem.Poy))

s = Segment(1, 2, 3, 4)
print(s)

#############################################################################

"""exercice2"""
class etudiant:
      def __init__(self, nom, prenom , age, cne, moyenne):
               self.nom = nom
               self.prenom = prenom
               self.age = age
               self.cne = cne
               self.moyenne = moyenne

# creation du list
list = []
# ajouter les element 
list.append( etudiant('El idrissi', 'Oubay', 20, 'P1241234', 16) )
list.append( etudiant('azzeddin','salmoun', 21,'P345678', 18 ) )
#affichage du liste
for obj in list:
  print( obj.nom , obj.prenom, obj.age, obj.cne , obj.moyenne )
print("\n")

#afficher la liste trier par Age
print("__la liste trier par age__\n")
list.sort(key=lambda x: x.age)
for obj in list:
     print( "nom: ",obj.nom," prenom: " ,obj.prenom," age: " ,obj.age," cne: ",obj.cne," moyenne: ", obj.moyenne )
print("\n")

#afficher la liste trier par moyenne
print("__la liste trier par moyenne__\n")
list.sort(key=lambda x: x.moyenne)
for obj in list:
      print( "nom: ",obj.nom," prenom: " ,obj.prenom," age: " ,obj.age," cne: ",obj.cne," moyenne: ",obj.moyenne )

#################################################################################

#exercice3
class Module:

    __nom = 0
    __volume_horaire = 0
    __semestre = ""
    ListMatiere = []
    def __init__(self, nom="", volume_horaire=0, semestre=""):
        self.__nom = nom
        self.__volume_horaire = volume_horaire
        self.__semestre = semestre

    def display(self):
        print(self.__nom,  self.__volume_horaire, self.__semestre)
class Matiere:

    __nom = 0
    __pourcentage = 0
    module = Module()
    ListeAnnesAcademique = []
    def __init__(self, nom="", pourcentage=0):
        self.__nom = nom
        self.__pourcentage = pourcentage

    def display(self):
        print(self.__nom, self.__pourcentage)

class Utilisateur:

    _nom = ""
    _email = ""
    _mot_de_passe = ""
    _genre = ""
    _age = 0

    def __init__(self, nom="", email="", mot_de_passe="", genre="", age=0):
        self._nom = nom
        self._email = email
        self._mot_de_passe = mot_de_passe
        self._genre = genre
        self._age = age

    def display(self):
        print(self._nom, self._email, self._mot_de_passe,  self._genre,  self._age)


class Professeur(Utilisateur):

    __ppr = 0
    __grade = ""
    module = Module()
    ListeMatieres = []
    ListeAnnesAcademique = []

    def __init__(self, nom="", email="", mot_de_passe="", genre="", age=0, ppr=0, grade=""):
        super().__init__(self, nom, email, mot_de_passe, genre, age)
        self.__ppr = ppr
        self.__grade = grade

    def display(self):
        print(self.__ppr, self.__grade)

class Annee_Academique:

    __anne = ""
    Listetudiant = []
    Listematiesre = []
    Listeprofesseur = []

    def __init__(self, anne=""):
        self.__anne = anne

    def display(self):
        print(self.__anne)


class Etudiant(Utilisateur):

    __code_massar = ""
    ListAnneAcademique = []

    def __init__(self, nom="", email="", mot_de_passe="", genre="", age=0, code_massar=""):
        super().__init__(nom, email, mot_de_passe, genre, age)
        self.__code_massar = code_massar

    def display(self):
        print(self.__code_massar)
