# Združevanje

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
SELECT ROUND(AVG(ocena), 1)
FROM filmi
WHERE leto = 2000;
```

2. Vrnite število filmov in povprečno oceno filmov vsakega režiserja. Rezultat uredite od najbolj uspešnega (najvišja ocena) do najmanj uspešnega režiserja.
```sql
SELECT COUNT(naslov), AVG(ocena)
FROM filmi
GROUP BY reziser
ORDER BY ocena DESC
```

3. Vrnite certifikate, ki se pojavijo pri vsaj 100 filmih.
```sql
SELECT certifikat
FROM filmi
GROUP BY certifikat
HAVING COUNT(certifikat) >= 100
```