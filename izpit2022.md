# 1. izpit 2022

Imamo tabele:
```sql
drzava(kratica, ime)
```
```sql
kolesar(id, ime, drzava, ekipa, starost, mlad)
```
```sql
etapa(stevilka, zacetek, konec, dolzina, tezavnost, visina)
```
```sql
ekipa(id, ime, drzava, razred)
```
```sql
rezultat(kolesar, etapa, mesto, cas, tocke)
```

1. naloga
    * Izpišite imena in starosti slovenskih kolesarjev (kratica države: si). Podatke uredite padajoče po starosti.
    ```sql
    SELECT ime, starost
    FROM kolesar
    WHERE drzava = 'si'
    ORDER BY starost DESC;
    ```

    * Vrnite vse podatke o ekipah, ki imajo v imenu pomišljaj med besedami (ne znotraj besede). Podatke razvrstite po imenu ekipe.
    ```sql
    SELECT *
    FROM ekipa
    WHERE ime LIKE '% - %'
    ORDER BY ime;
    ```

2. naloga
    * Za vsako težavnost izpišite skupno dolžino in povprečno višinsko razliko vseh etap te težavnosti.
    ```sql
    SELECT tezavnost, SUM(dolzina) AS skupna_dolzina, AVG(visina) AS povp_visinska_razlika
    FROM etapa
    GROUP BY tezavnost;
    ```

    * Za vsako etapo izpišite njeno zaporedno številko in čas zadnjega kolesarja, ki je prispel na cilj, v obliki ure:minute:sekunde. Podatke uredite padajoče po izpisanem času.
    ```sql
    SELECT etapa.stevilka AS st_etape, strftime('%w:%H:%M:%S', MAX(rezultat.cas), 'unixepoch', '-4 days') AS cas_zadnjega
    FROM etapa
    JOIN rezultat ON etapa.stevilka = rezultat.etapa
    GROUP BY etapa.stevilka;
    ```

3. naloga
    * Za vsakega kolesarja, ki nastopa za ekipo iz svoje države, izpišite ime kolesarja, ime ekipe in ime države.
    ```sql
    SELECT kolesar.ime, ekipa.ime, kolesar.drzava
    FROM kolesar
    JOIN ekipa ON ekipa.id = kolesar.ekipa
    WHERE kolesar.drzava = ekipa.drzava;
    ```

    * Za vsakega kolesarja, ki je končal dirko (tj., v nobeni etapi ni odstopil), izpišite njegovo ime in njegov skupni čas v obliki dni:ure:minute:sekunde. Podatki naj bodo urejeni naraščajoče po skupnem času.
    ```sql
    SELECT kolesar.ime, strftime('%w:%H:%M:%S', SUM(rezultat.cas), 'unixepoch', '-4 days') AS skupni_cas
    FROM kolesar
    JOIN rezultat ON kolesar.id = rezultat.kolesar
    WHERE kolesar.id NOT IN (
        SELECT kolesar
        FROM rezultat
        WHERE mesto IS NULL -- Izločimo kolesarje, ki so vsaj v eni etapi odstopili (mesto IS NULL)
    )
    GROUP BY rezultat.kolesar
    ORDER BY skupni_cas;
    ```

4. naloga
    * Izbrišite vse države, iz katerih ni nobenega kolesarja ali ekipe.
    ```sql
    DELETE FROM drzava
    WHERE kratica NOT IN (
        SELECT drzava
        FROM kolesar
    )
    AND kratica NOT IN (
        SELECT drzava 
        FROM ekipa
    );
    ```

    * Za vsakega kolesarja, ki je odstopil, dodajte vnose v tabelo rezultat s privzetimi vrednostmi v stolpcih mesto, cas, tocke pri vseh etapah, kjer se ta ni pojavil na štartni listi.
    ```sql
    INSERT INTO rezultat (kolesar, etapa, mesto, cas, tocke)
    SELECT kolesar.id, etapa.stevilka, NULL, NULL, 0
    FROM kolesar
    JOIN etapa
    LEFT JOIN rezultat ON kolesar.id = rezultat.kolesar AND etapa.stevilka = rezultat.etapa
    WHERE kolesar.id IN (
        -- Poiščemo kolesarje, ki so odstopili (tj. imajo vsaj eno `mesto IS NULL`)
        SELECT DISTINCT kolesar 
        FROM rezultat 
        WHERE mesto IS NULL
    )
    AND rezultat.kolesar IS NULL; -- Kolesar se še ni pojavil na tej etapi
    ```

5. naloga
    * Za Tadeja Pogačarja (kolesar.id = 6) izpišite njegov skupni čas po vsaki etapi - tj., izpišite številko etape in njegov skupni čas do vključno te etape v obliki dni:ure:minute:sekunde.
    ```sql
    SELECT etapa, strftime('%w:%H:%M:%S', SUM(cas) OVER (ORDER BY etapa), 'unixepoch', '-4 days') AS skupni_cas -- ?????
    FROM rezultat
    WHERE kolesar = 6;
    ```

    *  Za vsako etapo najvišje uvrščenemu mlademu kolesarju (tj., takemu, ki ima najmanjšo vrednost v stolpcu mesto) prištejte 5 točk pri tej etapi.
    ```sql
    WITH najvisje_uvrsceni AS (
        SELECT 
            rezultat.etapa,
            rezultat.kolesar,
            rezultat.mesto,
            rezultat.tocke,
            RANK() OVER (PARTITION BY rezultat.etapa ORDER BY rezultat.mesto) AS vrstni_red
        FROM rezultat
        JOIN kolesar ON kolesar.id = rezultat.kolesar
        WHERE kolesar.mlad = 1
    )
    SELECT 
        najvisje_uvrsceni.etapa,
        najvisje_uvrsceni.kolesar,
        (najvisje_uvrsceni.tocke + 5) AS nove_tocke
    FROM najvisje_uvrsceni
    WHERE najvisje_uvrsceni.vrstni_red = 1
    ORDER BY najvisje_uvrsceni.etapa;
    ```