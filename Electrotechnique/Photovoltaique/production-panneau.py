#source : https://photovoltaique-energie.fr/estimer-la-production-photovoltaique.html

#Théorie : formules de base pour connaître la production d'un panneau ou d'un système photovoltaïque
#Calcul par le rendement du panneau (ou de la cellule)

#E = S * r * H * Cp

#E = énergie produite en Wh

#S = surface du champ photovoltaïque  (exemple 7.14 m²)

#r = rendement du module (14 % pour notre exemple)

#H = ensoleillement/rayonnement sur la surface inclinée en kWh/m²  (1580 kWh/m².an pour le sud de la France)

#Cp = coefficient de perte (varie entre 0.9 et ... très bas, soit un minimum de 10 %, la valeur fréquente étant entre 0.75 et 0.8)

#Détail des pertes (varie selon les installations):

#    Pertes onduleurs 8% à 15 %
#    Pertes température 5% à 12%
#    Pertes câbles et connexion 2%
#    Pertes masque 0 % à 50% (dépend de l'implantation)
#    Pertes faible éclairement 3% à 7%
#    Pertes liées à la réflectivité environ 3%

#Exemple Cp = 0.9*0.92*0.98*0.97*0.96*0.97 = 0.74 soit 26% de pertes totales

#E = S x r x H x Cp

#E = 7.14*14%*1580*0.74

#E = 1168 kWh/an

#Remarque : on peut définir ainsi un "coefficient de production" qui permet d’avoir rapidement une idée de la production attendue en fonction de la puissance installée.

#Coefficient de production = Production / Puissance installée

#Ici : Coefficient de production = 1.17.  Une installation similaire de puissance 3000 Wc aura donc une production d’environ

#3000*1.17 = 3510 kWh/an.


#Méthode de la puissance crête du module et des heures d’ensoleillement :

#Un module se caractérise avant tout par sa puissance crête Pc, puissance dans les conditions standart STC.Le module exposé dans les conditions STC va produire à un instant donné une puissance électrique égale à cette puissance crête, et si cela dure Ne heures, il aura produit une énergie électrique E égale au produit de la puissance crête par le temps écoulé, au coefficient de pertes près :

#E = Pc x Cp x Ne

#E = énergie produite en Wh

#Pc = puissance crête du panneau en kWc

#Ne = Nombre d’heures équivalentes d’ensoleillement

#Soit : énergie électrique produite (Wh) = Nombre d’heures d’exposition aux conditions STC (h)* Puissance crête.

#Cependant, le rayonnement n’est pas constant pendant une journée d’ensoleillement, donc on ne peut pas appliquer strictement cette loi. Afin de calculer ce que produit un module photovoltaïque pendant une année d’ensoleillement qui a un certain profil et une énergie solaire intégrée en Wh/m², on va assimiler cette énergie solaire au produit du rayonnement instantané 1000 W/m² par un certain nombre d’heures que l’on appelle « nombre d’heures équivalentes pleine puissance».

#Grâce à la valeur de 1000 de ce rayonnement de référence, le nombre d’heures équivalentes se retrouve exactement égal à l’énergie solaire intégrée si on l’exprime en kWh/m².an.

#H = Ne * 1000

#Soit : énergie solaire annuelle (Wh/m².an) = nombre d’heures équivalentes (h/an)*1000 (W/m²).

#Dans notre exemple dans le sud de la France  H = 1580 kWh/m².an ou 1580000 Wh/m².an donc Ne = 1580000/1000 = 1580 h

#On peut ainsi avoir la production électrique :

#E = 1000 x 0.74 x 1580

#E = 1 169 200 Wh/an soit 1 169 kWh/an

#Simplement : E = Pc (kWc) * Ne * Cp

#Remarque : Dans le cadre de l’obligation d’achat, la réglementation considère que pour la France métropolitaine le nombre maximal d’heures d’ensoleillement est de 1500 heures (1800 h dans les DOM et en Corse) et par conséquent le tarif d’achat  n’est applicable que jusque 1500h.

#Gain maximal par an pour 1 kWc à un tarif de 0.55€/kWh = 1 x 1500 x 0.55 = 825 €

#Ce quota d'heure permet d’éviter tout problème de fraude (exemple : brancher un chargeur en sortie des panneaux pour augmenter la production du système photovoltaïque).
