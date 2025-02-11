# Združevanje

Vsi filmi, ki imajo oceno enako ali višjo od najvišje ocene med filmi, ki so bili izdani v istem letu.
```sql
SELECT * FROM film 
WHERE ocena >= (
    SELECT MAX(ocena) 
    FROM film 
    WHERE leto = leto 
)
```

Povprečna ocena filmov iz leta 2000
```sql
SELECT AVG(ocena) AS povp_ocena
FROM filmi
WHERE leto = 2000;
```

Povprečna ocena filmov za vsako leto
```sql
SELECT leto, AVG(ocena) AS povp_ocena
FROM filmi
GROUP BY leto;
```

Povprečna ocena filmov daljših od 100 minut za vsako leto, ko je bilo vsaj 5 filmov
```sql
SELECT leto, AVG(ocena) AS povp_ocena, COUNT(*) AS st_filmov
FROM filmi
WHERE dolzina > 100
GROUP BY leto
HAVING st_filmov > 5;
```

VAJE:

1. Vrnite povprečno oceno filmov iz leta 2000, zaokroženo na 1 decimalko.
```sql
SELECT ROUND(AVG(ocena), 1) AS povprecna_ocena
FROM filmi
WHERE leto = 2000;
```

2. Vrnite število filmov in povprečno oceno filmov vsakega režiserja. Rezultat uredite od najbolj uspešnega (najvišja ocena) do najmanj uspešnega režiserja.
```sql
SELECT reziser, COUNT(naslov) AS st_filmov, AVG(ocena) AS povp_ocena
FROM filmi
GROUP BY reziser
ORDER BY povp_ocena DESC
```

3. Vrnite certifikate, ki se pojavijo pri vsaj 100 filmih.
```sql
SELECT certifikat, COUNT(certifikat) AS st_filmov
FROM filmi
GROUP BY certifikat
HAVING COUNT(certifikat) >= 100
```