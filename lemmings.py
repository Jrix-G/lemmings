#Touche 1 pour rajouter un Lemming
#Touche q pour quitter
#Touche t pour effectuer un tour

lem_tab = [] #Stocke les positions l, c, d des Lemmings
class Jeu:
    def Grotte(self, largeur, longueur):
        #Système qui permet d'ouvrir et de lire la map pour les Lemmings sous forme de fichier.txt
        fichier = open("map.txt", "r")
        tab = []
        tmp_tab = []
        tmp2 = [[0]*largeur for _ in range(longueur)]
        for i in fichier: #Importe les valeurs du fichier txt
            tmp_tab += [i]

        for i in range(len(tmp_tab)): #Supprime les sauts de ligne
            for j in range(len(tmp_tab[i])):
                if tmp_tab[i][j] != "\n":
                    tab += tmp_tab[i][j]

        for i in range(longueur): #Création de la carte sous forme de tableau en colonnes
            x = 0
            while x < largeur:
                tmp2[i][x] = tab[0]
                del tab[0]
                x += 1
        return tmp2
    
    def Lemmings(self, l, c, d): #Rajout d'un Lemming dans le tableau
        global lem_tab
        lem_tab += [[l, c, d]]

    def demarre(self): #Fonction principale de mise en route du programme
        while True:
            typevalue = input("Votre commande: ")
            if typevalue == "1":
                x = input("Valeur de x: ")
                y = input("Valeur de y: ")
                new = Lemming(int(x), int(y))
            if typevalue == "q":
                return False
            if typevalue == "t":
                for i in range(len(lem_tab)):
                    tour = Lemming
                    tour.action(self, i, 15, 7) #15 et 7 doivent être modifier si modification de la taille de la map, avec longueur+1
estparti = False
class Lemming:
    def __init__(self, x, y): #Création Lemmings
        Jeu.Lemmings(self, x, y, 1) #Lemming initialement dirigé vers la droite

    def __str__(self, n): #Connaitre la direction d'un Lemming n
        global lem_tab
        if lem_tab[n][2] == -1:
            return "<"
        else:
            return ">"
    
    def action(self, n, largeur, longueur): #Fonction plus courte pour l'éxecution d'un tour
        global lem_tab, estparti
        print("Coordonnées des Lemmings", lem_tab)
        if estparti == True:
            if n == 0: 
                print(lem_tab[n])
                x = lem_tab[n][0]
                y = lem_tab[n][1]
            else:
                n -= 1
                x = lem_tab[n][0]
                y = lem_tab[n][1]
        else:
            x = lem_tab[n][0]
            y = lem_tab[n][1]

        #On change les coordonnées du Lemming en fonction des cases aux alentours
        if Lemming.__str__(self, n) == ">":
            if Case.terrain(self, x+1, y, largeur, longueur) == "Vide":
                lem_tab[n][0] = x+1
            elif Case.terrain(self, x, y+1, largeur, longueur) == "Sortie":
                print("Lemming ", n, " est parti")
                estparti = True
                Case.depart(self, n)
            elif Case.libre(self, x, y+1, largeur, longueur) == True:
                lem_tab[n][1] = y+1
            else:
                lem_tab[n][2] = -1
        elif Lemming.__str__(self, n) == "<":
            if Case.terrain(self, x+1, y, largeur, longueur) == "Vide":
                lem_tab[n][0] = x+1
            elif Case.terrain(self, x, y+1, largeur, longueur) == "Sortie":
                print("Lemming ", n, " est parti")
                Case.depart(n)
            elif Case.libre(self, x, y-1, largeur, longueur) == True:
                lem_tab[n][1] = y-1
            else:
                lem_tab[n][2] = 1
        else:
            print("Erreur")

class Case: #Caractéristique d'une case
    def terrain(self, x, y, largeur, longueur):
        jeu = Jeu.Grotte(self, largeur, longueur)
        if jeu[x][y] == '0':
            return "Sortie"
        elif jeu[x][y] == '#':
            return "Mur"
        elif jeu[x][y] == ' ':
            return "Vide"
        else:
            return "Erreur"

    def lemming(self, l, c): #Occupation d'une case par un Lemming
        global lem_tab
        if lem_tab == []:
            return None
        else:
            for i in range(len(lem_tab)):
                if lem_tab[i][0] == l and lem_tab[i][1] == c:
                    return "Occupé"
            return "Vide"

    def __str__(self, l, c): #Transformation du résultat de Case.lemming
        if Case.lemming(self, l, c) == "Vide":
            return " "
        else:
            return "X"

    def libre(self, l, c, largeur, longueur): #Vérifie que la case soit libre pour un Lemming
        if Case.terrain(self, l, c, largeur, longueur) == "Vide" and Case.__str__(self, l, c) == " ":
            return True
        else:
            return False

    def depart(self, lem): #Supprime le Lemming du tableau et du jeu
        global lem_tab
        del lem_tab[lem]
        
    def arrivee(self, lem, l, c, largeur, longueur): #Modification des données, et regarde si le Lemming a trouvé la sortie
        global lem_tab
        if Case.terrain(self, l, c, largeur, longueur) == "Sortie":
            self.depart(lem)
        elif Case.libre(self, l, c, largeur, longueur) == True:
            lem_tab[lem][0] = l
            lem_tab[lem][1] = c

#Start du jeu
start = Jeu() 
start.demarre()