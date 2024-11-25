# Poskusni izpit

1. Vrnite tabelo imen in priimkov vseh oseb, ki jim je ime Matija
```sql
SELECT ime, priimek FROM osebe
WHERE ime = 'Matija';
```

2. Vrnite tabelo imen in priimkov vseh oseb, urejeno po priimku
```sql
SELECT ime, priimek FROM osebe
ORDER BY priimek;
```

3. Vrnite imena vseh predmetov na praktični matematiki (smer: 1PrMa)
```sql
SELECT ime FROM predmeti
WHERE smer = '1PrMa';
```

4. Vrnite vse podatke o skupinah z manj kot eno uro
```sql
SELECT id, učitelj, ure, tip FROM skupine
WHERE ure < 1;
```

5. Vrnite število vseh predmetov na posamezni smeri
```sql
SELECT smer, COUNT(*) AS st_predmetov FROM predmeti
GROUP BY smer;
```

6. Vrnite imena tistih predmetov, ki se pojavljajo na več smereh
```sql
SELECT ime FROM predmeti
GROUP BY smer
HAVING COUNT(smer) > 1;
```

7. Vrnite imena in vse pripadajoče smeri tistih predmetov, ki se pojavljajo na več smereh
```sql
SELECT ime, smer FROM predmeti
WHERE ime IN (
    SELECT ime FROM predmeti
    GROUP BY ime
    HAVING COUNT(DISTINCT(smer)) > 1
)
ORDER BY ime;
```

8. Vrnite skupno število ur vsake osebe
```sql
SELECT osebe.ime, osebe.priimek, SUM(ure) AS skupno_st_ur FROM osebe
    JOIN skupine ON osebe.id = skupine.učitelj
GROUP BY osebe.id;
```

9. Vrnite imena in priimke vseh predavateljev, torej tistih, ki imajo kakšno skupino tipa P
```sql
SELECT ime, priimek FROM osebe
    JOIN skupine ON osebe.id = skupine.učitelj
WHERE skupine.tip = 'P'
GROUP BY osebe.id;
```

10. Vrnite imena in priimke vseh predavateljev, ki izvajajo tako predavanja (tip P) kot vaje (tipa V ali L)
```sql
SELECT ime, priimek FROM osebe
    JOIN skupine s1 ON osebe.id = s1.učitelj
WHERE s1.tip = 'P' AND EXISTS (
    SELECT 1 FROM skupine s2
    WHERE s1.učitelj = s2.učitelj AND s2.tip IN ('V', 'L')
)
GROUP BY osebe.id;
```

11. Vrnite imena in smeri vseh predmetov, ki imajo kakšen seminar
```sql

```

12. Vsem predmetom na smeri 2PeMa spremenite smer na PeMa
```sql
UPDATE predmeti
SET smer = 'PeMa'
WHERE smer = '2PeMa';
```

13. Izbrišite vse predmete, ki niso dodeljeni nobeni skupini
```sql
DELETE FROM predmeti
WHERE id NOT IN (
    SELECT DISTINCT predmet
    FROM dodelitve
);
```

14. Za vsak predmet, ki se pojavi tako na prvi kot drugi stopnji (smer se začne z 1 oz. 2), dodajte nov predmet z istim imenom in smerjo 0Mate (stolpca id ne nastavljajte, ker se bo samodejno določil)
```sql
INSERT INTO predmeti (ime, smer)
SELECT ime, '0Mate' FROM predmeti
WHERE smer LIKE '1%' OR smer LIKE '2%';
```
------------------- OD TU NAPREJ JE PREGLEDANO -------------------

15. Za vsako smer izpišite število različnih oseb, ki na njej poučujejo

Uradna rešitev:
```sql
SELECT * FROM predmeti
    JOIN dodelitve ON predmeti.id = dodelitve.predmet
    JOIN skupine ON dodelitve.skupina = skupine.id;
```
Ali:
```sql
SELECT smer, COUNT(DISTINCT učitelj) AS st_uciteljev FROM predmeti
    JOIN dodelitve ON predmeti.id = dodelitve.predmet
    JOIN skupine ON dodelitve.skupina = skupine.id
GROUP BY smer;
```

16. Vrnite pare ID-jev tistih oseb, ki sodelujejo pri vsaj dveh predmetih (ne glede na tip skupine), pri čemer naj bo prvi ID v paru manjši od drugega, pari pa naj se ne ponavljajo

Uradna rešitev:
```sql
SELECT s1.učitelj, s2.učitelj FROM skupine AS s1
    JOIN dodelitve AS d1 ON s1.id = d1.skupina
    JOIN dodelitve AS d2 USING(predmet) -- USING vzame dve tabeli in jih združi glede na stolpec predmet
    JOIN skupine AS s2 ON d2.skupina = s2.id
WHERE s1.učitelj < s2.učitelj
GROUP BY s1.učitelj, s2.učitelj
HAVING COUNT(DISTINCT predmet) >= 2; -- izberi tiste skupine kjer je število različnih predmetov vsaj 2
```

17. Za vsako osebo (izpišite jo z ID-jem, imenom in priimkom) vrnite skupno število ur vaj (tako avditornih kot laboratorijskih), pri čemer naj bo to enako 0, če oseba ne izvaja nobenih vaj

Uradna rešitev:
```sql
SELECT osebe.id, ime, priimek, COALESCE(SUM(ure), 0) AS st_ur FROM osebe
    LEFT JOIN skupine ON osebe.id = skupine.učitelj AND tip IN ('V', 'L')
GROUP BY osebe.id, ime, priimek
```

18. Vrnite ID-je, imena in smeri predmetov, za katere se izvaja seminar, ne pa tudi avditorne ali laboratorijske vaje

Uradna rešitev:
```sql
WITH predmeti_vaje AS (
    SELECT predmet FROM dodelitve
        JOIN skupine ON dodelitve.skupina = skupine.id
    WHERE skupine.tip IN ('V', 'L')
)
SELECT DISTINCT predmeti.id, ime, smer FROM predmeti
    JOIN dodelitve ON predmeti.id = dodelitve.predmet
    JOIN skupine ON dodelitve.skupina = skupine.id
WHERE skupine.tip = 'S' AND predmet NOT IN predmeti_vaje;
```