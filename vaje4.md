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