/*
SAE 2.04
LABIT Evan
CREPIN Pierre
BRENEL Pierre
SAILLY Kevin

Requetes SQL des graphiques
*/

-- Les films qui ont le genre et le distributeur parmi les 5 meilleurs
SELECT title, international_sales FROM films WHERE filmid IN (
  SELECT filmid FROM films WHERE distrid IN (
    SELECT dist.distrid FROM films INNER JOIN 
      distributor dist ON films.distrid=dist.distrid GROUP BY dist.distrid ORDER BY AVG(international_sales) DESC LIMIT 5
  )
) AND filmid IN (
  SELECT filmid FROM has_genres WHERE genrid IN (
    SELECT genrid FROM genre WHERE name LIKE 'Sci-Fi' OR name LIKE 'Adventure' OR name LIKE 'Fantasy' OR name LIKE 'Action' OR name LIKE 'Animation'
  ) GROUP BY 1
);


-- Moyenne de ventes internationales de Paramount, Universal et Sony Pictures
SELECT AVG(international_sales) AS moyenne_ventes_international, dist.name AS distributeur FROM films INNER JOIN distributor dist ON films.distrid=dist.distrid GROUP BY 2 HAVING dist.name like 'Universal Pictures' or dist.name like 'Paramount Pictures' or dist.name like 'Sony Pictures Entertainment (SPE)' ORDER BY 1 DESC;


-- Ecart-type de la moyenne des 5 meilleurs genre en ventes à l'international
select G.name as genre, STDDEV(international_sales) AS ecart_type from has_genres as HG
inner join genre as G on G.genrid = HG.genrid
inner join films as F on F.filmid = HG.filmid
group by G.name
order by ecart_type desc
limit 5;


-- Nombre de films pour les 5 pires distributeurs
SELECT COUNT(films.filmid), name FROM films INNER JOIN
   distributor ON films.distrid=distributor.distrid WHERE films.distrid IN (
     SELECT dist.distrid FROM films INNER JOIN 
        distributor dist ON films.distrid=dist.distrid GROUP BY dist.distrid ORDER BY AVG(international_sales) ASC LIMIT 5
    )
GROUP BY 2;


-- Les 5 meilleurs producteurs, en fonction de la moyenne des ventes de leurs films
SELECT AVG(international_sales) AS moyenne_ventes_international, dist.name AS distributeur FROM films INNER JOIN distributor dist ON films.distrid=dist.distrid GROUP BY 2 ORDER BY 1 DESC LIMIT 5;


-- En moyenne, quels sont les genres les moins vendus ?
select G.name as genre, FLOOR( AVG( F.international_sales ) ) as nombre_de_ventes from has_genres as HG
inner join genre as G on G.genrid = HG.genrid
inner join films as F on F.filmid = HG.filmid
group by G.name
order by nombre_de_ventes asc
limit 5;


-- En moyenne, quels sont les genres les plus vendus ?
select G.name as genre, FLOOR( AVG( F.international_sales ) ) as nombre_de_ventes from has_genres as HG
inner join genre as G on G.genrid = HG.genrid
inner join films as F on F.filmid = HG.filmid
group by G.name
order by nombre_de_ventes desc
limit 5;


-- En moyenne, quels sont les distributeurs ayant les films avec le plus de succès ?
select D.name, FLOOR( AVG( F.international_sales ) ) as nombre_de_ventes from distributor as D
inner join films as F on F.distrid = D.distrid
group by D.name
order by nombre_de_ventes
desc limit 10;


-- En moyenne, quels sont les distributeurs ayant le moins de succès ?
select D.name, FLOOR( AVG( F.international_sales ) ) as nombre_de_ventes from distributor as D
inner join films as F on F.distrid = D.distrid
group by D.name
order by nombre_de_ventes
desc limit 10;


-- Nombre de films pour les 5 meilleurs distributeurs
SELECT COUNT(films.filmid), name FROM films INNER JOIN
   distributor ON films.distrid=distributor.distrid WHERE films.distrid IN (
     SELECT dist.distrid FROM films INNER JOIN
        distributor dist ON films.distrid=dist.distrid GROUP BY dist.distrid ORDER BY AVG(international_sales) DESC LIMIT 5
    )
GROUP BY 2;


-- Recettes de Paramount, Sony Pictures, et Universal
SELECT AVG(international_sales) AS moyenne_ventes_international, dist.name AS distributeur FROM films
INNER JOIN distributor dist ON films.distrid=dist.distrid
GROUP BY 2
HAVING dist.name like 'Universal Pictures' or dist.name like 'Paramount Pictures' or dist.name like 'Sony Pictures Entertainment (SPE)'
ORDER BY 1 DESC;


-- Le nombre de films réalisé par tout les distributeurs
SELECT COUNT(films.filmid) AS nb_films, distrib.name FROM films
INNER JOIN distributor distrib ON films.distrid=distrib.distrid
GROUP BY 2
ORDER BY 1 DESC;