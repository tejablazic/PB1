# Osnovne poizvedbe s SELECT

Vsi filmi z oceno večjo od 8, ki se začnejo z besedo Boter:
```sql
SELECT naslov, ocena 
FROM film
WHERE ocena > 8 AND glasovi > 10000 AND naslov LIKE 'Boter%'
ORDER BY ocena DESC, naslov;
```

Filmi z oceno večjo od 8, zaokroženo na celo število:
```sql
SELECT naslov, ROUND(ocena) AS 'Zaokrožena ocena'
FROM film
WHERE ocena > 8 AND glasovi > 10000
ORDER BY ocena DESC, naslov;
```

```sql
SELECT naslov, ROUND(ocena)
FROM film
WHERE ROUND(ocena) = (
    SELECT MIN(ROUND(ocena))
    FROM film
);
```