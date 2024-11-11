# Ustvarjanje tabel

1. Ustvari bazo naročil (npr. narocila.sqlite), ki smo jo uporabljali prejšnji teden na vajah. Baza bo imela tabeli stranka in narocilo z naslednjnimi stolpci:

stranka:

* id - primarni ključ tabele
* ime - besedilna vrednost (vrednost ne sme biti NULL)

```sql
CREATE TABLE stranka (
    id     integer    PRIMARY KEY,
    ime    text       NOT NULL   
);
```

narocilo:

* id - primarni ključ tabele
* kolicina - številska vrednost (vrednost mora biti večja od 0)
* stranka - tuj ključ, tabelo povezuje s stolpcem id v tabeli stranka (vrednost ne sme biti NULL)
* status - besedilna vrednost, ki ji dolžino lahko omejimo na 10 znakov (vrednost mora biti eden izmed nizov oddano, v obdelavi, na poti, zaključeno; privzeta vrednost je oddano)

```sql
CREATE TABLE narocilo (
    id          integer        PRIMARY KEY, 
    kolicina    integer        CHECK (kolicina > 0), 
    stranka     integer        REFERENCES stranka(id)    NOT NULL, 
    status      varchar(10)    CHECK (status IN ('oddano', 'v obdelavi', 'na poti', 'zaključeno')) DEFAULT 'oddano'
);

--DROP TABLE IF EXISTS narocilo;
--DROP TABLE IF EXISTS stranka;
```

2. V bazo vstavi podatke

Tabela stranka:

id	ime\
1	Alenka\
2	Branko\
3	Cvetka\
4	David

```sql
INSERT INTO stranka (ime)
VALUES ('Alenka'), ('Branko'), ('Cvetka'), ('David');
```

Tabela narocilo:

id	kolicina	stranka	status\
1	500	        2	    v obdelavi\
2	300	        3	    na poti\
3	800	        2	    v obdelavi\
4	150	        1	    oddano\
5	400	        4	    zaključeno\
6	400	        1	    na poti

```sql
INSERT INTO narocilo (kolicina, stranka, status)
VALUES (500, 2, 'v obdelavi'), 
       (300, 3, 'na poti'), 
       (800, 2, 'v obdelavi'), 
       (150, 1, 'oddano'), 
       (400, 4, 'zaključeno'), 
       (400, 1, 'na poti');
```

3. Preveri, če so stolpci nastavljeni pravilno:

* ne moremo dodati naročila z neveljavno količino (npr. -100)
```sql
INSERT INTO narocilo (kolicina)
VALUES (-100);
```
* če dodamo vrstico z veljavno količino in ID stranke, a brez statusa, se mora status nastaviti na (oddano)
```sql
INSERT INTO narocilo (kolicina, stranka)
VALUES (10, 2);
```
* za status ne moremo nastaviti neveljavnega statusa (npr. čaka)
```sql
UPDATE narocilo
SET status = 'čaka'
WHERE stranka = 2;
```
* ne moremo dodati naročila z neveljavnim ID stranke (id, ki še ne obstaja v tabeli stranka, na primer 10).
```sql
INSERT INTO narocilo (stranka)
VALUES (10);
```

4. Preveri, če ukazi, napisani na prejšnjih vajah delujejo tudi za novo bazo. (Po želji lahko brisanje Alenke in njenih transakcij poskusiš izvesti kot transakcijo.)