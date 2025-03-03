-- JOIN ESPLICITO PER shop_online (con Alias)

SELECT o.id_ordine, c.id_articolo, a.nome 
FROM ordini as o 
INNER JOIN carrello as c
ON o.id_ordine = c.id_ordine 
INNER JOIN articoli as a 
ON a.id_articolo = c.id_articolo
WHERE o.id_ordine = 2;

-- JOIN IMPLICITO PER shop_online (con Alias)

SELECT o.id_ordine, c.id_articolo, a.nome 
FROM ordini as o, carrello as c, articoli as a
WHERE o.id_ordine = 2 AND c.id_articolo = a.id_articolo

-- JOIN QUERY PER CHINOOK DATABASE:

-- GENRE ROCK - TUTTE LE CANZONI:
-- JOIN ESPLICITO
SELECT g.Name as "GENRE", t.Name as "TRACK NAME", t.Composer 
FROM Track as t 
INNER JOIN Genre as g
ON g.GenreId = t.GenreId 
WHERE g.Name = "Rock"

-- JOIN IMPLICITO
SELECT g.Name as "GENRE", t.Name as "TRACK NAME", t.Composer 
FROM Track as t, Genre as g
WHERE g.GenreId = t.GenreId 
AND g.Name = "Rock"

-- GENRE ROCK - TUTTE LE CANZONI CON ALBUM TITLE:
-- JOIN ESPLICITO CON 'IN'
SELECT g.Name as "GENRE", t.Name as "TRACK NAME", a.Title 
FROM Track as t 
INNER JOIN Genre as g
ON g.GenreId = t.GenreId 
INNER JOIN Album as a
ON t.AlbumId = a.AlbumId 
WHERE g.Name IN("World", "Drama");
