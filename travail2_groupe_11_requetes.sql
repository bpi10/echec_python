                                    /*===========================*/
                                    /*        Parent Thibaut     */
                                    /*        Brenel Pierre      */
                                    /*            TPA            */
                                    /*     SAE1_4 travail n°2    */
                                    /*        groupe 11          */
                                    /*===========================*/

/*================================================================================================================*/
/*     1) Il semble en effet que certains articles ou catégories ne soient jamais commandés est-ce le cas ?       */
/*================================================================================================================*/

-- requête permettant de savoir les articles jamais commandés
select nomarticle as "article non commandé" from article where numarticle not in ( select numarticle from detailcommande );

-- résultat de la requête
 article non commandé
----------------------
 YOONER
(1 ligne)


-- requête permettant de savoir les catégories qui n'ont jamais été commandés 
select numcategorie as "categories non commandées" from categorie where numcategorie not in (1, 2, 3, 4, 6, 9, 12)
and numcategorie not in 
(select numcategorie from article where numarticle in
(select numarticle from detailcommande));

-- résultat de la requête
categories non commandées
---------------------------
                         7
                         8
                        10
                        11
                        13
                        16
                        17
                        19
                        20
                        22
                        23
                        24
                        25
(13 lignes)

/* Pour conclure, nous avons d'abord fais une requête sur les articles non commandés, et nous avons 1 article jamais commandé,
 dont le nom de cet article est "YOONER", ensuite nous avons fais une requête pour les catégories non commandées, et nous avons trouvés
 les catégories suivantes -> (7, 8, 10, 11, 13, 16, 17, 19, 20, 22, 23, 24, 25).*/



/*================================================================================================================*/
/*     2) Une action commerciale a été menée il y a 3 semaines sur les clients basés en Suisse. L’entreprise      */
/*     souhaiterait savoir s’il y a eu un effet sur les commandes. (Indice : Vous présenterez les résultats       */
/*     de vente cad le chiffre d’affaires par mois et le chiffre d’affaires par numéro de semaine).               */
/*================================================================================================================*/


-- requête pour les semaines
select SUM(montantht) as "CA", extract(week from datecommande) as "n° semaine" from commande where numclient in 
(select numclient from client where codeetiquette like 'CH') group by datecommande;

-- résultat de la requête pour les semaines 
    CA    | n° semaine
----------+------------
  5870.00 |         41
  9450.00 |         45
 50767.50 |         50
(3 lignes)


-- requête pour les mois
select SUM(montantht) as "CA", extract(month from datecommande) as "n° mois" from commande where numclient in 
(select numclient from client where codeetiquette like 'CH') group by datecommande;

-- résultat de la requête pour les mois 
    CA    | n° mois
----------+---------
  5870.00 |      10
  9450.00 |      11
 50767.50 |      12
(3 lignes)

/* Nous avons fais 2 requêtes différentes afin d'avoir le chiffre d'affaire des clients basés en Suisse par semaine, puis par mois,
pour étudier si il y a eu un effet sur le Chiffre d'affaire basé ces clients,
Nous pouvons aperçevoir qu'il y a eu aucun effet de la semaine au mois, et aussi que le chiffre d'affaire augmente
consécutivement au fil des mois / semaines passées, sûrement dû aux fêtes de fin d'années et la période hivernale.*/

/*================================================================================================================*/
/*     3) Existe-t-il des clients qui n’ont jamais passé de commandes ? Existe-t-il des clients d’un pays         */ 
/*     entier qui n’ont jamais passé de commandes ?                                                               */
/*================================================================================================================*/

-- clients n'ayant jamais passé commandes.
select nomclient as "nom_client_sans_commande" from client where numclient not in
(select numclient from commande);

-- résultat de la requête
 nom_client_sans_commande
--------------------------
 GO Sport Orange
 GO Sport Perpignan
 SPORT 2000 Bich
 Foot Locker Rome
 The North Face Reggio
 Nike Town
 Lillywhites
(7 lignes)

/* Nous avons 7 clients qui n'ont jamais commandé */

-- clients d'un pays entier qui n'ont jamais passé commandes
select distinct(nomclient, codeetiquette) from client where codeetiquette not in
(select numclient from commande);
select distinct(nomclient, codeetiquette) from client where codeetiquette not in 
(select codeetiquette from client where numclient in
(select numclient from commande));

-- résultat de la requête       
       row
------------------
 (Lillywhites,GB)
 ("Nike Town",GB)
(2 lignes)

/* Nous avons 2 clients qui viennent de Grande-Bretagne qui n'ont jamais commandé, 
cela revient à dire qu'ils n'ont pas eu de commande en Grande-Bretagne.*/

-- 2 ème requête plus adapté pour la question, qui répond directement sans déduire
select libelleetiquette as "Pays_sans_commandes" from etiquette where codeetiquette in
(select codeetiquette from client where codeetiquette not in
(select codeetiquette from client where numclient in
(select numclient from commande)));

-- résultat de la requête
 Pays_sans_commandes
---------------------
 Client Anglais
(1 ligne)


/*================================================================================================================*/
/*     4) Il semble que certaines commandes ne soient pas livrées totalement le phénomène est-il inquiétant ?     */
/*================================================================================================================*/
-- requête non réussi

/* Nous n'avons pas réussi la requête mais nous avons regardé de nous même autrement qu'en répondant à la question,
 et il existe des commandes qui n'ont pas été livrée totalement, cela est un phénomène inquiétant car cela veut dire
 que l'entreprise n'est pas consciencieuse/professionelle, ou alors qu'il y a eu des délais de livraisons par rapport
 à un fournisseur,si le client a été prévenu des délais et qu'il a accepté de se faire livrer les autres articles disponibles avant,
 alors c'est moins inquiétant que si le client n'a pas été prévenu des délais/retard des articles restant.
 Le client est alors en droit de demander un remboursement,
 de 10% de la somme si le retard est inférieur ou égal à trente jours,
 de 20% de la somme pour un retard allant de trente jours à soixante jours,
 de 50% de la somme pour un retard supérieur à soixante jours.*/ 

