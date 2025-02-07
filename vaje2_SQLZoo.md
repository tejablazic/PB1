# SUM and COUNT

## World Country Profile: Aggregate functions
This tutorial is about aggregate functions such as COUNT, SUM and AVG. An aggregate function takes many values and delivers just one value.  

### Aggregates
The functions **SUM**, **COUNT**, **MAX** and **AVG** are "aggregates", each may be applied to a numeric attribute resulting in a single row being returned by the query. (These functions are even more useful when used with the GROUP BY clause.)  

### Distinct
By default the result of a SELECT may contain duplicate rows. We can remove these duplicates using the **DISTINCT** key word.  

### Order by
**ORDER BY** permits us to see the result of a SELECT in any particular order. We may indicate **ASC** or **DESC** for ascending (smallest first, largest last) or descending order.

1. The total population and GDP of Europe.
```sql
SELECT SUM(population), SUM(gdp)
FROM bbc
WHERE region = 'Europe';
```

2. What are the regions?
```sql
SELECT DISTINCT region 
FROM bbc;
```

3. Show the name and population for each country with a population of more than 100000000. Show countries in descending order of population.
```sql
SELECT name, population
FROM bbc
WHERE population > 100000000
ORDER BY population DESC;
```

```sql
world(name, continent, area, population, gdp)
```

1. Show the total population of the world.
```sql
SELECT SUM(population)
FROM world;
```

2. List all the continents - just once each.
```sql
SELECT DISTINCT continent
FROM world;
```

3. Give the total GDP of Africa.
```sql
SELECT SUM(gdp)
FROM world
WHERE continent = 'Africa';
```

4. How many countries have an area of at least 1000000?
```sql
SELECT COUNT(name)
FROM world
WHERE area >= 1000000;
```

5. What is the total population of ('Estonia', 'Latvia', 'Lithuania')?
```sql
SELECT SUM(population)
FROM world
WHERE name IN ('Estonia', 'Latvia', 'Lithuania');
```

# Using GROUP BY and HAVING
By including a **GROUP BY** clause functions such as **SUM** and **COUNT** are applied to groups of items sharing values. When you specify GROUP BY continent the result is that you get only one row for each different value of continent. All the other columns must be "aggregated" by one of SUM, COUNT ...  
  
The **HAVING** clause allows use to filter the groups which are displayed. The **WHERE** clause filters rows before the aggregation, the HAVING clause filters after the aggregation.  
  
If a **ORDER BY** clause is included we can refer to columns by their position.  

```sql
world(name, continent, area, population, gdp)
```

1. For each continent show the number of countries:
```sql
SELECT continent, COUNT(name)
FROM world
GROUP BY continent;
```

2. For each continent show the total population:
```sql
SELECT continent, SUM(population)
FROM world
GROUP BY continent;
```

3. **WHERE and GROUP BY**  
The WHERE filter takes place before the aggregating function.  
For each relevant continent show the number of countries that has a population of at least 200000000.
```sql
SELECT continent, COUNT(name)
FROM world
WHERE population > 200000000
GROUP BY continent;
```

4. **GROUP BY and HAVING**  
The HAVING clause is tested after the GROUP BY. You can test the aggregated values with a HAVING clause.  
Show the total population of those continents with a total population of at least half a billion.
```sql
SELECT continent, SUM(population)
FROM world
GROUP BY continent
HAVING SUM(population) > 500000000;
```

6. For each continent show the continent and number of countries.
```sql
SELECT continent, COUNT(DISTINCT(name))
FROM world
GROUP BY continent;
```

7. For each continent show the continent and number of countries with populations of at least 10 million.
```sql
SELECT continent, COUNT(name)
FROM world
WHERE population >= 10000000
GROUP BY continent;
```
  
```sql
SELECT continent, COUNT(name)
FROM world
GROUP BY continent
HAVING population >= 10000000;
```
returns Error: Unknown column 'population' in 'HAVING'.

8. List the continents that have a total population of at least 100 million.
```sql
SELECT continent
FROM world
GROUP BY continent
HAVING SUM(population) >= 100000000;
```

# Nobel Prizes: Aggregate functions
This tutorial concerns aggregate functions such as **COUNT**, **SUM** and **AVG**.

```sql
nobel(winner, subject, year)
```

Using MAX, AVG, DISTINCT and ORDER BY.  
  
1. Show the total number of prizes awarded.
```sql
SELECT COUNT(winner) 
FROM nobel;
```

2. List each subject - just once.
```sql
SELECT DISTINCT(subject)
FROM nobel;
```

3. Show the total number of prizes awarded for Physics.
```sql
SELECT COUNT(winner)
FROM nobel
WHERE subject = 'physics';
```
  
Using GROUP BY and HAVING.  
  
4. For each subject show the subject and the number of prizes.
```sql
SELECT subject, COUNT(winner)
FROM nobel
GROUP BY subject;
```

5. For each subject show the first year that the prize was awarded.  
```sql
SELECT subject, MIN(yr)
FROM nobel
GROUP BY subject;
```

6. For each subject show the number of prizes awarded in the year 2000.
```sql
SELECT subject, COUNT(winner)
FROM nobel
WHERE yr = 2000
GROUP BY subject;
```
  
Using aggregates with DISTINCT.
  
7. Show the number of different winners for each subject. Be aware that Frederick Sanger has won the chemistry prize twice - he should only be counted once.
```sql
SELECT subject, COUNT(DISTINCT winner)
FROM nobel
GROUP BY subject;
```

8. For each subject show how many years have had prizes awarded.
```sql
SELECT subject, COUNT(DISTINCT(yr))
FROM nobel
GROUP BY subject;
```
  
Using HAVING.  
  
9. Show the years in which three prizes were given for Physics.
```sql
SELECT yr
FROM nobel
WHERE subject = 'physics'
GROUP BY yr
HAVING COUNT(winner) = 3;
```

10. Show winners who have won more than once.
```sql
SELECT winner
FROM nobel
GROUP BY winner
HAVING COUNT(winner) > 1;
```

11. Show winners who have won more than one subject.
```sql
SELECT winner
FROM nobel
GROUP BY winner
HAVING COUNT(DISTINCT(subject)) > 1;
```
  
GROUP BY yr, subject.  
  
12. Show the year and subject where 3 prizes were given. Show only years 2000 onwards.
```sql
SELECT yr, subject
FROM nobel
WHERE yr > 1999
GROUP BY yr, subject
HAVING COUNT(winner) = 3;
```
Group by both yr (year) and subject to count the winners for each combination of year and subject.