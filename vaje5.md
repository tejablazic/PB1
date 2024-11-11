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