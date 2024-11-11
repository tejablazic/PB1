# Spreminjanje podatkov

Dodajo tri nove stranke: Erik, Fani in Gala.
```sql
INSERT INTO stranka (ime)
VALUES ('Erik'), ('Fani'), ('Gala');
```

Popravijo status naročila z id 3 na na poti.
```sql
UPDATE narocilo
SET status = 'na poti'
WHERE id = 3;
```

Dodajo novo naročilo, ki ga je ustvarila Gala za 200 enot izdelka. Id stranke za vstavljanje naročila pridobi avtomatsko. Status naročila naj bo v obdelavi.
```sql
INSERT INTO narocilo (kolicina, stranka, status)
VALUES (200, 7, 'v obdelavi');
```

Izbrišejo Alenko in vsa njena naročila.
```sql
DELETE FROM narocilo
WHERE stranka = (SELECT id FROM stranka WHERE ime = 'Alenka');

DELETE FROM stranka
WHERE ime = 'Alenka';
```

Ustvarijo novo naročilo za vse stranke, ki še niso oddale naročila. Količina naj bo stokratnik id stranke. Status naročila naj bo nastavljen na privzeto vrednost (oddano).
```sql
INSERT INTO narocilo (kolicina, stranka)
SELECT 100 * id, id
FROM stranka
WHERE id NOT IN (SELECT DISTINCT stranka FROM narocilo);
```

Zaključim vsa naročila, ki so na poti.
```sql
UPDATE narocilo
SET status = 'oddano'
WHERE status = 'na poti';
```