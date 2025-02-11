# Spreminjanje podatkov

## Vaje s tabelo naročil
  
Dana je enostavna baza naročil s tabelama stranka in narocilo. Tabela stranka vsebuje IDje in imena strank, tabela narocilo pa IDje naročil, količino naročenih izdelkov, tuj ključ stranka, ki tabelo povezuje s tabelo stranka ter status naročila, ki ima lahko vrednost oddano, v obdelavi, na poti ali zaključeno.

```sql
stranka(id, ime)
```

```sql
narocilo(id, kolicina, stranka, status)
```

1. Dodaj tri nove stranke: Erik, Fani in Gala.
```sql
INSERT INTO stranka (ime)
VALUES ('Erik'), ('Fani'), ('Gala');
```

2. Popravi status naročila z id 3 na na poti.
```sql
UPDATE narocilo
SET status = 'na poti'
WHERE id = 3;
```

3. Dodaj novo naročilo, ki ga je ustvarila Gala za 200 enot izdelka. Id stranke za vstavljanje naročila pridobi avtomatsko. Status naročila naj bo v obdelavi.
```sql
INSERT INTO narocilo (kolicina, stranka, status)
VALUES (200, 7, 'v obdelavi');
```

4. Izbriši Alenko in vsa njena naročila.
```sql
DELETE FROM narocilo
WHERE stranka = (
    SELECT id 
    FROM stranka 
    WHERE ime = 'Alenka');

DELETE FROM stranka
WHERE ime = 'Alenka';
```

5. Ustvari novo naročilo za vse stranke, ki še niso oddale naročila. Količina naj bo stokratnik id stranke. Status naročila naj bo nastavljen na privzeto vrednost (oddano).
```sql
INSERT INTO narocilo (kolicina, stranka)
SELECT 100 * id, id
FROM stranka
WHERE id NOT IN (SELECT DISTINCT stranka FROM narocilo);
```

6. Zaključi vsa naročila, ki so na poti.
```sql
UPDATE narocilo
SET status = 'oddano'
WHERE status = 'na poti';
```
  
## Vaje na bazi filmov
  
Delamo z bazo filmi (ena tabela). Naloge, ki sledijo, so nekoliko kompleksnejše, saj je potrebno podatke za vstavljanje, brisanje in spreminjanje pridobiti s pomočjo ustreznih poizvedb na bazi.  
  
### Dodajanje vrstic
  
```sql
filmi(id, naslov, leto, reziser, certifikat, dolzina, ocena, opis)
```

1. V tabelo dodaj vsaj 5 filmov, posnetih po letu 2017. To naredi z enim ukazom **INSERT INTO**.
```sql
INSERT INTO filmi (naslov, leto)
VALUES ('Barbie', 2023), ('Oppenheimer', 2023), ('It Ends With Us', 2024), ('Joker', 2019), ('Joker: Folie à Deux', 2024);
```
Če privzeta vrednost ne bi bila NULL:
```sql
INSERT INTO filmi (naslov, leto, reziser, certifikat, dolzina, ocena, opis)
VALUES 
    ('Barbie', 2023, 'Greta Gerwig', 'PG-13', 114, 7.5, 'Film o Barbie in Kenu.'),
    ('Oppenheimer', 2023, 'Christopher Nolan', 'R', 180, 8.9, 'Film o očetu atomske bombe.'),
    ('It Ends With Us', 2024, 'Justin Baldoni', 'PG-13', 125, NULL, 'Ljubezenska drama.'),
    ('Joker', 2019, 'Todd Phillips', 'R', 122, 8.4, 'Zgodba o Jokerju.'),
    ('Joker: Folie à Deux', 2024, 'Todd Phillips', 'R', NULL, NULL, 'Nadaljevanje Jokerja.');
```

2. Denimo, da smo posneli novo različico vseh filmov, posnetih pred letom 1950 s certifikatom G, PG ali PG-13. Vstavi jih v tabelo, z ustrezno popravljenim naslovom, opisom in režiserjem. Njihova dolžina naj bo za toliko daljša, kot je absolutna vrednost razlike med dolžino originalnega filma in povprečjem dolžin teh (pred letom 1950, s certifikatom ...) filmov. Njihova ocena naj bo za ena nižja od ocene originalnega filma. Kaj bi storili z id?  
  
* Uporaba **INSERT INTO ... VALUES** (za ročno vstavljanje enega ali več statičnih zapisov). To uporabimo, kadar sami določimo podatke in jih vnesemo ročno.
* Uporaba **INSERT INTO ... SELECT** (za vstavljanje podatkov iz obstoječe tabele). To uporabimo, kadar želimo dinamično generirati nove podatke iz obstoječih.
```sql
INSERT INTO filmi (naslov, leto, reziser, certifikat, dolzina, ocena, opis)
SELECT 
    naslov || ' (Remake)', -- CONCAT(naslov, ' (Remake)');
    2025, 
    'Nov režiser', 
    certifikat,  
    dolzina + ABS(dolzina - (
        SELECT AVG(dolzina) 
        FROM filmi 
        WHERE leto < 1950 AND certifikat IN ('G', 'PG', 'PG-13'))),  
    CASE WHEN ocena IS NOT NULL THEN ocena - 1 
        ELSE NULL 
    END,  
    'Remake filma: ' || opis  
FROM filmi 
WHERE leto < 1950 
AND certifikat IN ('G', 'PG', 'PG-13');
```

### Spreminjanje vrstic
  
3. Vsem filmom določenega leta, ki imajo oceno nižjo od povprečja filmov v tem letu, dodaj dvakratno razliko med povprečjem in prvotno razliko. Tako bo film z id 22100 namesto ocene 8.4 imel oceno 8.6, saj je prvotno povprečje filmov iz leta 1931 8.5.
```sql
UPDATE filmi 
SET ocena = ocena + 2 * ((
    SELECT AVG(ocena) 
    FROM filmi AS f2 
    WHERE f2.leto = filmi.leto) - ocena
)
WHERE ocena < (
    SELECT AVG(ocena) 
    FROM filmi AS f2 
    WHERE f2.leto = filmi.leto);
```
  
### Brisanje vrstic

4. Želimo pripraviti prikaz aktivnosti določenih režiserjev. Zato bomo zbrisali vse filme tistih režiserjev, ki so režirali več kot 15 filmov (mimogrede so trije, s skupaj 58 filmi!) in jih nadomestili z novim filmom. Ta bo imel naslov Mesanica_<reziser>, leto nastanka naj bo 2023, opis ustrezen, ocena naj bo povprečje ocen filmov tega režiserja posnetih v prvih in zadnjih dveh letih njegovega ustvarjanja, dolžina pa 10 minut za vsak prvotni film. Ostale podatke si izmisli.
```sql

```