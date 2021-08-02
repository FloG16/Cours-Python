

source : https://core.ac.uk/download/pdf/144283017.pdf

1.3 Modélisation des batteries lithium-ion #Un modèle est une représentation mathématique simplifiée d’un phénomène physique. Les 
#modèles permettent de prédire le comportement d’un système et d’observer des phénomènes parfois 
#impossibles à mesurer dans la réalité. Par exemple, avec un modèle on peut rapidement simuler 
#plusieurs années du cycle de vie d’un produit en quelques minutes. Ceci évite de devoir construire 
#des prototypes physiques et de se lancer dans un campagne expérimentale onéreuse. Essentiel 
#à l’ingénierie prédictive, l’établissement d’un modèle qui tiens compte des aspects d’intérêts de 
#manière le plus fidèle est essentiel pour répondre à certaines questions d’ingénierie. Une revue des 
#différentes méthodes de modélisation des batteries a été faite par [76]. 
#Un modèle peut être grossier ou fin, son niveau de détail dépendant du problème à 
#résoudre. Par exemple, pour modéliser l’effet du nombre et de l’emplacement des électrodes reliant 
#les électrodes aux pôles de cellules cylindriques sur la distribution du courant et de température, 
#[77] a développé un modèle électrique, thermique et électrochimique de grande résolution. La 
#problématique de la modélisation des batteries a premièrement été abordée par des chimistes 
#[78, 79]. Ainsi, plusieurs études réalisées dans ce champ d’études se basent sur des équations tirées 
#de l’étude thermodynamique des réactions chimiques dans une cellule [80].Bien que de grande 
#qualité pour les fabricants de cellules, ce genre de modèle est trop précis pour la conception de 
#haut-niveau de SAE. #Ainsi, des modèles ont été développés pour représenter le comportement macroscopique 
#d’une batterie, qui se décline en trois types : l’électrique, le thermique et le vieillissement. Plusieurs 
#familles de modèles ont été développés, chacune répondant à des besoins particuliers. Les familles 
#de modèles sont : #— Mathématiques ; #— Stochastique ; #— Analytiques ; #— Électro-chimique ; 
#— Circuits électriques équivalents ; #— Réseaux de neurones. 
#On distingue trois champs d’études dans la modélisation des batteries : 
#— le comportement électrique ; #— le vieillissement ; 
#— la thermique. 
#Les deux propriétés principales d’une batterie sont sa tension Vnom et sa capacité Qcell 
#en Ah. Le produit de ces deux valeurs est une mesure de la quantité d’énergie contenue dans la 
#batterie. Dans une source de tension idéale, la tension devrait demeurer constante en tout temps, 
#jusqu’à ce que la batterie soit complètement déchargée, et ce peu importe la demande de courant 
#[17]. Ainsi l’autonomie d’une batterie devrait pouvoir se calculer directement par l’équation 1.1, #où tauto est le temps de décharge et I est le courant demandé.

tauto = Qcell/I

Or, les batteries au lithium n’adoptent pas un comportement idéal car leur tension ne 
#reste pas constante tout au long de la décharge. On a longtemps estimé l’autonomie réelle d’une 
#batterie par la loi de Peukert (eq. 1.2). Le b > 1 est une constante propre à chaque batterie, 
#tenant compte de la diminution de la capacité en fonction du courant débité et doit être obtenus 
#expérimentalement.

tauto = Qcell/Ib

#La relation de Peukert (eq. 1.2) ne tient pas compte de la température, ni ne permet de 
#calculer la tension de la batterie. C’est l’utilisation des batteries dans les appareils électroniques 
#portables qui a amené les électrotechniciens à s’intéresser à la modélisation des batteries [19]. 
#Le premier modèle mathématique exprimant le comportement électrochimique d’une bat- 
#terie a été développé par Shepherd dans les années 1960 [79]. L’équation 1.3 est notamment utilisé 
#dans le modèle générique de batterie fourni dans MATLAB/Simulink® SimPowerSystems [81].

E = Es − K( Q/(Q − it))i + Aexp(−(BQ<<−1)it) − Ri
