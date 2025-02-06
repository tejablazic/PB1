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

**Pattern Matching Strings**  
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
  
*The function concat is short for concatenate - you can use it to combine two or more strings.*

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

14. Find the capital and the name where the capital is an extension of name of the country. You should include Mexico City as it is longer than Mexico. You should not include Luxembourg as the capital is the same as the country.
```sql
SELECT capital, name
FROM world
WHERE capital LIKE CONCAT(name, ' %') OR capital LIKE CONCAT(name, '-%');
```

15. The capital of Monaco is Monaco-Ville: this is the name Monaco and the extension is -Ville.  
Show the name and the extension where the capital is a proper (non-empty) extension of name of the country.  
    
*You can use the SQL function REPLACE.*  
*REPLACE(f, s1, s2) returns the string f with all occurances of s1 replaced with s2.*  
*REPLACE('vessel','e','a') -> 'vassal'*

```sql
SELECT name, REPLACE(capital, name, '') AS extension
FROM world
WHERE capital LIKE CONCAT(name, '%')
AND REPLACE(capital, name, '') <> '';
```

# SELECT from WORLD

1. [Read the notes about this table.](https://sqlzoo.net/wiki/Read_the_notes_about_this_table.)
Observe the result of running this SQL command to show the name, continent and population of all countries.
```sql
SELECT name, continent, population 
FROM world;
```

2. [How to use WHERE to filter records.](https://sqlzoo.net/wiki/WHERE_filters) 
Show the name for the countries that have a population of at least 200 million. 200 million is 200000000.
```sql
SELECT name 
FROM world
WHERE population >= 200000000;
```

3. Give the name and the per capita GDP for those countries with a population of at least 200 million. Per capita GDP is the GDP divided by the population GDP/population.
```sql
SELECT name, (gdp/population) AS 'per capita GDP'
FROM world
WHERE population >= 200000000;
```

4. Show the name and population in millions for the countries of the continent 'South America'. Divide the population by 1000000 to get population in millions.
```sql
SELECT name, population/1000000
FROM world
WHERE continent = 'South America';
```

5. Show the name and population for France, Germany, Italy.
```sql
SELECT name, population 
FROM world
WHERE name IN ('France', 'Germany', 'Italy')
```

6. Show the countries which have a name that includes the word 'United'.
```sql
SELECT name
FROM world
WHERE name LIKE '%United%';
```

7. Two ways to be big: A country is big if it has an area of more than 3 million sq km or it has a population of more than 250 million.  
Show the countries that are big by area or big by population. Show name, population and area.
```sql
SELECT name, population, area
FROM world
WHERE area > 3000000 OR population > 250000000;
```

8. Exclusive OR (XOR). Show the countries that are big by area (more than 3 million) or big by population (more than 250 million) but not both. Show name, population and area.
* Australia has a big area but a small population, it should be included.
* Indonesia has a big population but a small area, it should be included.
* China has a big population and big area, it should be excluded.
* United Kingdom has a small population and a small area, it should be excluded.
```sql
SELECT name, population, area
FROM world
WHERE area > 3000000 XOR population > 250000000;
```
Without XOR:
```sql
SELECT name, population, area
FROM world
WHERE (area > 3000000 AND population <= 250000000)
   OR (population > 250000000 AND area <= 3000000);
```

9. Show the name and population in millions and the GDP in billions for the countries of the continent 'South America'. Use the ROUND function to show the values to two decimal places. For Americas show population in millions and GDP in billions both to 2 decimal places.  
  
*ROUND(f,p) returns f rounded to p decimal places.*
*The number of decimal places may be negative, this will round to the nearest 10 (when p is -1) or 100 (when p is -2) or 1000 (when p is -3) etc..*
*ROUND(7253.86, 0)    ->  7254*
*ROUND(7253.86, 1)    ->  7253.9*
*ROUND(7253.86,-3)    ->  7000*

**Millions and billions**
Divide by 1000000 (6 zeros) for millions. Divide by 1000000000 (9 zeros) for billions.
**Missing decimals**
For some version of SQL the division of an integer by an integer will be an integer. One way to prevent this is to divide by a floating point number such as 1000000.0.
```sql
SELECT name, ROUND(population/1000000, 2), ROUND(gdp/1000000000, 2)
FROM world
WHERE continent = 'South America';
```

10. Show the name and per-capita GDP for those countries with a GDP of at least one trillion (1000000000000; that is 12 zeros). Round this value to the nearest 1000. Show per-capita GDP for the trillion dollar countries to the nearest $1000.
```sql
SELECT name, ROUND(gdp/population, -3) AS 'per capita GDP'
FROM world
WHERE gdp >= 1000000000000;
```

11. Show the name and capital where the name and the capital have the same number of characters.  
You can use the LENGTH function to find the number of characters in a string.  
For Microsoft SQL Server the function LENGTH is LEN.
```sql
SELECT name, capital
FROM world
WHERE LENGTH(name) = LENGTH(capital);
```

12. Show the name and the capital where the first letters of each match. Don't include countries where the name and the capital are the same word.  
You can use the function LEFT to isolate the first character.  
You can use <> as the NOT EQUALS operator.
```sql
SELECT name, capital
FROM world
WHERE LEFT(name, 1) = LEFT(capital, 1) AND name <> capital;
```

13. Find the country that has all the vowels and no spaces in its name.  
You can use the phrase name NOT LIKE '%a%' to exclude characters from your results.  
The query shown misses countries like Bahamas and Belarus because they contain at least one 'a'
```sql
SELECT name
FROM world
WHERE name NOT LIKE '% %'
  AND name LIKE '%a%'
  AND name LIKE '%e%'
  AND name LIKE '%i%'
  AND name LIKE '%o%'
  AND name LIKE '%u%';
```

