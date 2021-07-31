#Une fois n'est pas coutume, lorsqu'il s'agit de présenter la syntaxe d'un langage de programmation, on utilise comme exemple le programme Hello World. 
#Il s'agit simplement d'un programme qui affiche les deux mots « Hello World » à l'écran, avant de se terminer.

#Voici ce que cela donne en Python :

print('Hello World!')

#Quoi de plus simple ? Python inclut une fonction prédéfinie print qui affiche à l'écran la séquence de caractères qu'on lui fournit. 
#Cette unique ligne de code constitue notre premier programme Python.

#Voyons maintenant un exemple de programme qui utilise plusieurs variables pour calculer le discriminant du trinôme x2+2x−4

a = 1
b = 2
c = -4

delta = b ** 2 - 4 * a * c
print('Le discriminant est :')
print(delta)

#Les trois premières instructions stockent les coefficients du trinôme, à savoir 1, 2 et −4, respectivement dans des variables nommées a, b et c. 
#La quatrième instruction effectue le calcul du discriminant (b2−4ac) et stocke le résultat dans la variable delta. Enfin, les deux dernières instructions affichent
#à l'écran la phrase « Le discriminant est : », suivie de la valeur de la variable delta.

#L'utilisation d'une variable est donc assez immédiate. Deux types d'accès peuvent être réalisés :

    #Pour affecter une valeur à une variable, c'est-à-dire l'initialiser ou modifier sa valeur, on utilise l'opérateur d'affectation (=). À gauche de l'opérateur, on retrouve le nom de la variable et à droite la valeur qu'on souhaite lui affecter.
    #Pour accéder au contenu d'une variable, il suffit d'utiliser son nom. Cet accès peut, par exemple, se faire dans une expression mathématique, ou avec la fonction print.

#Le symbole = est à distinguer du signe égal utilisé en mathématiques pour énoncer une égalité. En Python, il permet d'affecter une valeur à une variable. Voyons cela avec l'exemple suivant :

a = 1
b = a
print(a)
print(b)

a = 15
print(a)
print(b)

#En mathématiques, écrire b=a signifie que a et b représentent la même valeur. Dès lors, lorsqu'on écrit plus loin a = 15, on pourrait s'attendre à ce que a et b 
#valent 15

#En Python, b = a signifie qu'on affecte la valeur de a à la variable b (on fait une copie de la valeur). Après exécution de cette instruction, 
#aucun lien n'est établi entre les deux variables. L'exécution du programme affiche lors de son exécution :
 


