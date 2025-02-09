# Stikanje

Zapiši poizvedbe za sledeče zahteve na bazi filmov.  
  
1. Vrni naslove filmov in imena glavnih igralcev. Rezultate uredi po imenu igralca in nato še po naslovu filma.  
```sql
SELECT naslov, ime 
FROM film
JOIN vloga ON film.id = vloga.film
JOIN oseba ON vloga.oseba = oseba.id
WHERE tip = "I" AND mesto = 1
ORDER BY ime, naslov;
```
2. Za vsakega režiserja (izpiši ga z IDjem in imenom) izpiši skupno dolžino filmov, ki jih je režiral (brez igranja). Rezultate uredi po imenu režiserja.
```sql
SELECT oseba.id, ime, SUM(dolzina) FROM oseba
JOIN vloga ON vloga.oseba = oseba.id
JOIN film ON film.id = vloga.film
WHERE vloga.tip = "R"
GROUP BY ime
ORDER BY ime;
```
3. Za vsak žanr (izpiši ga z imenom) izpiši število različnih igralcev in število različnih režiserjev, ki so sodelovali pri filmih tega žanra. Rezultate uredi padajoče po vsoti števila igralcev in števila režiserjev (če se nekdo pojavi tako kot igralec kot režiser, se tukaj šteje dvakrat).
```sql
SELECT naziv, COUNT(DISTINCT(igralec.oseba)) AS st_igralcev, COUNT(DISTINCT(reziser.oseba)) AS st_reziserjev FROM zanr
JOIN pripada ON pripada.zanr = zanr.id
JOIN vloga AS igralec ON igralec.film = pripada.film
JOIN vloga AS reziser ON reziser.film = pripada.film
WHERE igralec.tip = "I" ANd reziser.tip = "R"    
GROUP BY naziv
ORDER BY st_igralcev + st_reziserjev DESC;
```