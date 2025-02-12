# SELECT basics

```sql
world(name, continent, area, population, gdp)
```

1. The example uses a WHERE clause to show the population of 'France'. Note that strings should be in 'single quotes'.  
Modify it to show the population of Germany.
```sql
SELECT population 
FROM world
WHERE name = 'Germany';
```

2. Checking a list The word **IN** allows us to check if an item is in a list. The example shows the name and population for the countries 'Brazil', 'Russia', 'India' and 'China'.  
Show the name and the population for 'Sweden', 'Norway' and 'Denmark'.
```sql
SELECT name, population 
FROM world
WHERE name IN ('Sweden', 'Norway', 'Denmark');
```

3. Which countries are not too small and not too big? **BETWEEN** allows range checking (range specified is inclusive of boundary values). The example below shows countries with an area of 250,000-300,000 sq. km.  
Modify it to show the country and the area for countries with an area between 200,000 and 250,000.
```sql
SELECT name, area 
FROM world
WHERE area BETWEEN 200000 AND 250000;
```

# SELECT names

**Pattern Matching Strings**  
This tutorial uses the **LIKE** operator to check names. We will be using the **SELECT** command on the table world.

1. You can use **WHERE name LIKE 'B%'** to find the countries that start with "B". The % is a wild-card it can match any characters.  
Find the country that start with "Y".
```sql
SELECT name 
FROM world
WHERE name LIKE 'Y%';
```

2. Find the countries that end with "y".
```sql
SELECT name 
FROM world
WHERE name LIKE '%y';
```

3. Find the countries that contain the letter "x".
```sql
SELECT name 
FROM world
WHERE name LIKE '%x%';
```

4. Find the countries that end with "land".
```sql
SELECT name 
FROM world
WHERE name LIKE '%land';
```

5. Find the countries that start with "C" and end with "ia".
```sql
SELECT name 
FROM world
WHERE name LIKE 'C%ia';
```

6. Find the country that has "oo" in the name.
```sql
SELECT name 
FROM world
WHERE name LIKE '%oo%';
```

7. Find the countries that have three or more "a" in the name.
```sql
SELECT name 
FROM world
WHERE name LIKE '%a%a%a%';
```

8. India and Angola have an "n" as the second character. You can use the underscore as a single character wildcard.
```sql
SELECT name 
FROM world
WHERE name LIKE '_n%'
ORDER BY name;
```
Find the countries that have "t" as the second character.
```sql
SELECT name 
FROM world
WHERE name LIKE '_t%'
ORDER BY name;
```

9. Lesotho and Moldova both have two "o" characters separated by two other characters.  
Find the countries that have two "o" characters separated by two others.
```sql
SELECT name 
FROM world
WHERE name LIKE '%o__o%';
```

10. Cuba and Togo have four characters names.  
Find the countries that have exactly four characters.
```sql
SELECT name 
FROM world
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
*CONCAT allows you to stick two or more strings together.*  
*This operation is concatenation.*  
*CONCAT(s1, s2 ...) returns s1s2*
*CONCAT('Africa', 'Angola') -> 'AfricaAngola'*

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

8. Exclusive OR (**XOR**). Show the countries that are big by area (more than 3 million) or big by population (more than 250 million) but not both. Show name, population and area.
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
You can use the **LENGTH** function to find the number of characters in a string.  
For Microsoft SQL Server the function LENGTH is LEN.
```sql
SELECT name, capital
FROM world
WHERE LENGTH(name) = LENGTH(capital);
```

12. Show the name and the capital where the first letters of each match. Don't include countries where the name and the capital are the same word.  
You can use the function **LEFT** to isolate the first character.  
You can use **<>** as the **NOT EQUALS** operator.
```sql
SELECT name, capital
FROM world
WHERE LEFT(name, 1) = LEFT(capital, 1) AND name <> capital;
```

13. Find the country that has all the vowels and no spaces in its name.  
You can use the phrase name **NOT LIKE '%a%'** to exclude characters from your results.  
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

# SELECT from Nobel

This tutorial is concerned with a table of Nobel prize winners:
```sql
nobel(yr, subject, winner)
```
Using the **SELECT** statement.  

1. Change the query shown so that it displays Nobel prizes for 1950.
```sql
SELECT yr, subject, winner
FROM nobel
WHERE yr = 1950;
```

2. Show who won the 1962 prize for literature.
```sql
SELECT winner
FROM nobel
WHERE yr = 1962 AND subject = 'literature';
```

3. Show the year and subject that won 'Albert Einstein' his prize.
```sql
SELECT yr, subject
FROM nobel
WHERE winner = 'Albert Einstein';
```

4. Give the name of the 'peace' winners since the year 2000, including 2000.
```sql
SELECT winner
FROM nobel
WHERE subject = 'peace' AND yr > 1999;
```

5. Show all details (yr, subject, winner) of the literature prize winners for 1980 to 1989 inclusive.
```sql
SELECT yr, subject, winner
FROM nobel
WHERE subject = 'literature' AND yr BETWEEN 1980 AND 1989;
```

6. Show all details of the presidential winners:
* Theodore Roosevelt
* Thomas Woodrow Wilson
* Jimmy Carter
* Barack Obama
```sql
SELECT * 
FROM nobel
WHERE winner IN ('Theodore Roosevelt',
                'Thomas Woodrow Wilson',
                'Jimmy Carter',
                'Barack Obama')
```

7. Show the winners with first name John.
```sql
SELECT winner
FROM nobel
WHERE winner LIKE 'John%';
```

8. Show the year, subject, and name of physics winners for 1980 together with the chemistry winners for 1984.
```sql
SELECT yr, subject, winner
FROM nobel
WHERE subject = 'physics' AND yr = 1980 OR subject = 'chemistry' AND yr = 1984; 
```

9. Show the year, subject, and name of winners for 1980 excluding chemistry and medicine.
```sql
SELECT yr, subject, winner
FROM nobel
WHERE yr = 1980 AND subject NOT IN ('chemistry', 'medicine');
```

10. Show year, subject, and name of people who won a 'Medicine' prize in an early year (before 1910, not including 1910) together with winners of a 'Literature' prize in a later year (after 2004, including 2004)
```sql
SELECT yr, subject, winner
FROM nobel
WHERE subject = 'medicine' AND yr < 1910 OR subject = 'literature' AND yr > 2003;
```

11. Find all details of the prize won by PETER GRÜNBERG. 
```sql
SELECT *
FROM nobel
WHERE winner = 'Peter Grünberg';
```

12. Find all details of the prize won by EUGENE O'NEILL.  
*You can't put a single quote in a quote string directly. You can use two single quotes within a quoted string.*
```sql
SELECT *
FROM nobel
WHERE winner = "Eugene O'Neill";
```

13. List the winners, year and subject where the winner starts with Sir. Show the the most recent first, then by name order.
```sql
SELECT winner, yr, subject
FROM nobel
WHERE winner LIKE 'Sir %'
ORDER BY yr DESC, winner;
```

# SELECT within SELECT

## Using SELECT in SELECT
See **SELECT FROM SELECT** for how to use a [derived table](https://sqlzoo.net/wiki/SELECT_.._SELECT).  

The result of a SELECT statement may be used as a value in another statement. For example the statement SELECT continent FROM world WHERE name = 'Brazil' evaluates to 'South America' so we can use this value to obtain a list of all countries in the same continent as 'Brazil'.

1. List each country in the same continent as 'Brazil'.
```sql
SELECT name 
FROM world 
WHERE continent = (
    SELECT continent 
    FROM world 
    WHERE name = 'Brazil'
);
```

## Alias
Some versions of SQL insist that you give the subquery an alias. Simply put **AS** somename after the closing bracket:
```sql
SELECT name 
FROM world 
WHERE continent = 
  (SELECT continent 
  FROM world 
  WHERE name = 'Brazil') AS brazil_continent;
```

## Multiple Results
The subquery may return more than one result - if this happens the query above will fail as you are testing one value against more than one value. It is safer to use IN to cope with this possibility.  
  
The phrase:
```sql
SELECT continent 
FROM world 
WHERE name = 'Brazil' OR name = 'Mexico';
```
 will return two values ('North America' and 'South America').  
 You should use:
```sql
SELECT name, continent 
FROM world
WHERE continent IN
 (SELECT continent 
 FROM world 
 WHERE name = 'Brazil' OR name = 'Mexico');
```
2. List each country and its continent in the same continent as 'Brazil' or 'Mexico'.
```sql
SELECT name, continent 
FROM world
WHERE continent IN
  (SELECT continent 
  FROM world 
  WHERE name = 'Brazil' OR name = 'Mexico');
```
  
## Subquery on the SELECT line
If you are certain that only one value will be returned you can use that query on the SELECT line. 
   
3. Show the population of China as a multiple of the population of the United Kingdom.
```sql
SELECT population/
  (SELECT population 
  FROM world
  WHERE name = 'United Kingdom')
FROM world
WHERE name = 'China';
```
  
## Operators over a set
These operators are binary - they normally take two parameters:
```sql
=     equals
>     greater than
<     less than
>=    greater or equal
<=    less or equal
```
You can use the words **ALL** or **ANY** where the right side of the operator might have multiple values.  
  
4. Show each country that has a population greater than the population of ALL countries in Europe.  
Note that we mean greater than every single country in Europe; not the combined population of Europe.
```sql
SELECT name 
FROM world
WHERE population > ALL
  (SELECT population 
  FROM world
  WHERE continent = 'Europe');
```
  
```sql
world(name, continent, area, population, gdp)  
```
  
1. List each country name where the population is larger than that of 'Russia'.
```sql
SELECT name 
FROM world
WHERE population >
  (SELECT population
  FROM world
  WHERE name = 'Russia');
```

2. Show the countries in Europe with a per capita GDP greater than 'United Kingdom'.  
The per capita GDP is the gdp/population.  
```sql
SELECT name 
FROM world
WHERE gdp/population > (
  SELECT gdp/population 
  FROM world 
  WHERE name = 'United Kingdom') AND continent = 'Europe';
```

3. List the name and continent of countries in the continents containing either Argentina or Australia. Order by name of the country.
```sql
SELECT name, continent 
FROM world
WHERE continent IN (
  SELECT continent 
  FROM world 
  WHERE name = 'Argentina' OR name = 'Australia')
ORDER BY name;
```

4. Which country has a population that is more than United Kingdom but less than Germany? Show the name and the population.
```sql
SELECT name, population 
FROM world
WHERE population > (
  SELECT population 
  FROM world 
  WHERE name = 'United Kingdom') 
AND population < (
  SELECT population 
  FROM world 
  WHERE name = 'Germany');
```

5. Germany (population 80 million) has the largest population of the countries in Europe. Austria (population 8.5 million) has 11% of the population of Germany.  
Show the name and the population of each country in Europe. Show the population as a percentage of the population of Germany.  
The format should be Name, Percentage for example:  
name	  percentage  
Albania	3%  
Andorra	0%  
Austria	11%  
...	...  
  
**Decimal places**  
You can use the function **ROUND** to remove the decimal places.  
  
**Percent symbol %**  
You can use the function **CONCAT** to add the percentage symbol.  
  
```sql
SELECT name, CONCAT(ROUND((population * 100.0) / (
  SELECT population 
  FROM world 
  WHERE name = 'Germany'), 0), '%') AS percentage
FROM world
WHERE continent = 'Europe';
```
  
We can use the word **ALL** to allow >= or > or < or <= to act over a list. For example, you can find the largest country in the world, by population with this query:  
```sql
SELECT name
FROM world
WHERE population >= ALL(
  SELECT population
  FROM world
  WHERE population > 0);
```
You need the condition population > 0 in the sub-query as some countries have null for population.  
  
6. Which countries have a GDP greater than every country in Europe? [Give the name only.] (Some countries may have NULL gdp values)
```sql
SELECT name
FROM world
WHERE gdp > ALL (
  SELECT gdp
  FROM world
  WHERE continent = 'Europe' AND gdp > 0);
```
  
We can refer to values in the outer SELECT within the inner SELECT. We can name the tables so that we can tell the difference between the inner and outer versions.
  
7. Find the largest country (by area) in each continent, show the continent, the name and the area:
The above example is known as a **correlated** or **synchronized** sub-query.  
  
**Using correlated subqueries**  
A correlated subquery works like a nested loop: the subquery only has access to rows related to a single record at a time in the outer query. The technique relies on table aliases to identify two different uses of the same table, one in the outer query and the other in the subquery.  
  
One way to interpret the line in the **WHERE** clause that references the two table is “… where the correlated values are the same”.  
  
In the example provided, you would say *“select the country details from world where the area is greater than or equal to the area of all countries where the continent is the same”*.  
```sql
SELECT continent, name, area 
FROM world x
WHERE area >= ALL (
  SELECT area 
  FROM world y
  WHERE y.continent = x.continent);
```

8. List each continent and the name of the country that comes first alphabetically.  
  
*To find the first country alphabetically in each continent, you need to use a correlated subquery that selects the minimum (alphabetically first) name for each continent.*
```sql
SELECT continent, name 
FROM world x
WHERE name = (
  SELECT MIN(name) 
  FROM world y 
  WHERE y.continent = x.continent);
```

9. Find the continents where all countries have a population <= 25000000. Then find the names of the countries associated with these continents. Show name, continent and population.
```sql
SELECT name, continent, population
FROM world
WHERE continent IN (
  SELECT continent 
  FROM world 
  GROUP BY continent
  HAVING MAX(population) <= 25000000);
```