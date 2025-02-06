# SELECT basics

tabela: "world"
stolpci: "name", "continent", "area", "population", "gdp"

1. The example uses a WHERE clause to show the population of 'France'. Note that strings should be in 'single quotes'. 
Modify it to show the population of Germany.
```sql
SELECT population FROM world
WHERE name = 'Germany';
```

2. Checking a list The word IN allows us to check if an item is in a list. The example shows the name and population for the countries 'Brazil', 'Russia', 'India' and 'China'. 
Show the name and the population for 'Sweden', 'Norway' and 'Denmark'.
```sql
SELECT name, population FROM world
WHERE name IN ('Sweden', 'Norway', 'Denmark');
```

3. Which countries are not too small and not too big? BETWEEN allows range checking (range specified is inclusive of boundary values). The example below shows countries with an area of 250,000-300,000 sq. km. 
Modify it to show the country and the area for countries with an area between 200,000 and 250,000.
```sql
SELECT name, area FROM world
WHERE area BETWEEN 200000 AND 250000;
```

# SELECT names

Pattern Matching Strings
This tutorial uses the LIKE operator to check names. We will be using the SELECT command on the table world.

1. You can use WHERE name LIKE 'B%' to find the countries that start with "B". The % is a wild-card it can match any characters.
Find the country that start with "Y".
```sql
SELECT name FROM world
WHERE name LIKE 'Y%';
```

2. Find the countries that end with "y".
```sql
SELECT name FROM world
WHERE name LIKE '%y';
```

3. Find the countries that contain the letter "x".
```sql
SELECT name FROM world
WHERE name LIKE '%x%';
```

4. Find the countries that end with "land".
```sql
SELECT name FROM world
WHERE name LIKE '%land';
```

5. Find the countries that start with "C" and end with "ia".
```sql
SELECT name FROM world
WHERE name LIKE 'C%ia';
```

6. Find the country that has "oo" in the name.
```sql
SELECT name FROM world
WHERE name LIKE '%oo%';
```

7. Find the countries that have three or more "a" in the name.
```sql
SELECT name FROM world
WHERE name LIKE '%a%a%a%';
```

8. India and Angola have an "n" as the second character. You can use the underscore as a single character wildcard.
```sql
SELECT name FROM world
WHERE name LIKE '_n%'
ORDER BY name;
```
Find the countries that have "t" as the second character.
```sql
SELECT name FROM world
WHERE name LIKE '_t%'
ORDER BY name;
```

9. Lesotho and Moldova both have two "o" characters separated by two other characters.
Find the countries that have two "o" characters separated by two others.
```sql
SELECT name FROM world
WHERE name LIKE '%o__o%';
```

10. Cuba and Togo have four characters names.
Find the countries that have exactly four characters.
```sql
SELECT name FROM world
WHERE name LIKE '____';
```

11. The capital of Luxembourg is Luxembourg. Show all the countries where the capital is the same as the name of the country.
Find the country where the name is the capital city.
```sql
SELECT name
FROM world
WHERE name = capital;
```

12. The capital of Mexico is Mexico City. Show all the countries where the capital has the country together with the word "City".
Find the country where the capital is the country plus "City".

The function concat is short for concatenate - you can use it to combine two or more strings.

```sql
SELECT name
FROM world
WHERE capital = CONCAT(name, ' City');
```

13. Find the capital and the name where the capital includes the name of the country.
```sql
SELECT capital, name
FROM world
WHERE capital LIKE CONCAT('%', name, '%');
```

14. Find the capital and the name where the capital is an extension of name of the country.
You should include Mexico City as it is longer than Mexico. You should not include Luxembourg as the capital is the same as the country.
```sql
SELECT capital, name
FROM world
WHERE capital LIKE CONCAT(name, ' %') OR capital LIKE CONCAT(name, '-%');
```

15. The capital of Monaco is Monaco-Ville: this is the name Monaco and the extension is -Ville.
Show the name and the extension where the capital is a proper (non-empty) extension of name of the country.
You can use the SQL function REPLACE.
REPLACE(f, s1, s2) returns the string f with all occurances of s1 replaced with s2.
REPLACE('vessel','e','a') -> 'vassal'

```sql
SELECT name, REPLACE(capital, name, '') AS extension
FROM world
WHERE capital LIKE CONCAT(name, '%')
AND REPLACE(capital, name, '') <> '';
```