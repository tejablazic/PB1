# Ustvarjanje tabel

# Baza naročila
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

# Baza učitelji

1. Ustvarili bomo bazo s podaki o učiteljih na FMF.

* V SQLite Studio ustvari novo bazo ucitelji in se poveži nanjo

* Dodaj tabelo ucitelji, ki naj ima stolpce id, ime, priimek in email. Stolpec id naj bo tipa integer, ostali stolpci pa tipa text. Stolpec id naj bo glavni ključ tabele.
```sql
CREATE TABLE ucitelji (
    id         integer    PRIMARY KEY,
    ime        text,
    priimek    text,
    email      text
);
```
* Dodaj tabelo predmeti, ki naj vsebuje stolpce id, ime in ects. Stolpca id in ects naj bosta tipa integer, ime predmeta pa text. Spet naj bo stolpec id glavni ključ tabele.
```sql
CREATE TABLE predmeti (
    id      integer    PRIMARY KEY,
    ime     text,
    ects    integer
);
```
* V tabeli ucitelji smo pozabili na stolpec kabinet. Tabelam lahko dodajamo stolpce na naslednji način: ALTER TABLE ime_tabele ADD COLUMN ime_stolpca tip_stolpca; Tip stolpca naj bo kar text, saj oznaka kabineta lahko vsebuje tudi piko in črke.
```sql
ALTER TABLE ucitelji
ADD COLUMN kabinet text;
```
* Dodaj še šifrant vlog, in sicer kot tabelo vloge, ki ima stolpca id (tipa integer) in opis (tipa text). Poskrbi tudi za glavni ključ. Vloga z id 0 ustreza predavateljem, vloga 1 pa asistentom.
```sql
CREATE TABLE vloge (
    id      integer    PRIMARY KEY    CHECK(id IN (0, 1)),
    opis    text
);
```
* Dodaj tabelo izvajalci, ki naj ima tri stolpce (vsi so tipa integer): idpredmeta, iducitelja in vloga. Poskrbi za ustrezne reference na ostale tabele.
```sql
CREATE TABLE izvajalci (
    idpredmeta    integer    REFERENCES predmeti(id),
    iducitelja    integer    REFERENCES ucitelji(id),
    vloga         integer    REFERENCES vloge(id)
);
```

2. Napolni tabele s pomočjo skript ucitelji, predmeti, vloge in izvajalci z ustreznimi stavki INSERT.

* Da ne bo potrebno izvajati vsakega stavka posebej, v SQLite Studiu pritisni F10 in odstrani kljukico pri Execute only the query under the cursor. (Na MacOS zna biti bližnjica drugačna. Alternativno lahko izbereš vse vrstice s CTRL+A, če v skripti ni drugih ukazov.)

3. Na bazi izvedi naslednje pozivedbe:

* poizvedbo, ki poišče najbolj zasedene kabinete.
```sql

```
* poizvedbo, ki bo prikazala vse pare cimrov. Izpisati je treba tabelo, ki ima 4 stolpce (ime1, priimek1, ime2, priimek2). Za vsaka dva učitelja, ki si delita pisarno, se mora v rezultatu pojaviti po ena vrstica.
```sql

```
* poizvedbo, ki bo vrnila tabelo vseh trojic predmet-učitelj-asistent. Iz te tabele se bo dalo razbrati, pri kolikih predmetih sodelujeta nek učitelj in asistent.
```sql

```

4. Dodatna vaja iz spreminjanja tabel:

* Preverimo izvajalce predmeta Podatkovne baze 1 in popravimo na trenutno stanje:
```sql

```
* Matija Pretnar ni več predavatelj pri predmetu PB1
```sql

```
* Janoš Vidali je predavatelj in ne več asistent
```sql

```
* Ajda Lampe je nova asistentka pri predmetu (in je še ni v tabeli učiteljev)
```sql

```