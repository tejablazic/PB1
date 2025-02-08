# The JOIN operation

```sql
game(id, mdate, stadium, team1, team2)
```

```sql
goal(matchid, teamid, player, gtime)
```

```sql
eteam(id, teamname, coach)
```

This tutorial introduces **JOIN** which allows you to use data from two or more tables.  
  
1. The first example shows the goal scored by a player with the last name 'Bender'. The * says to list all the columns in the table - a shorter way of saying matchid, teamid, player, gtime.  
```sql
SELECT * 
FROM goal 
WHERE player LIKE '%Bender'; 
```
Modify it to show the matchid and player name for all goals scored by Germany. To identify German players, check for: teamid = 'GER'.
```sql
SELECT matchid, player 
FROM goal 
WHERE teamid = 'GER'; 
```

2. From the previous query you can see that Lars Bender's scored a goal in game 1012. Now we want to know what teams were playing in that match.  
Notice in the that the column matchid in the goal table corresponds to the id column in the game table. We can look up information about game 1012 by finding that row in the game table.  
Show id, stadium, team1, team2 for just game 1012.
```sql
SELECT id, stadium, team1, team2
FROM game
WHERE id = 1012;
```

3. You can combine the two steps into a single query with a **JOIN**.
```sql
SELECT *
FROM game 
JOIN goal ON (id = matchid);
```
The **FROM** clause says to merge data from the goal table with that from the game table. The **ON** says how to figure out which rows in game go with which rows in goal - the matchid from goal must match id from game. If we wanted to be more clear/specific we could say:
```sql
ON (game.id = goal.matchid);
```
The code below shows the player (from the goal) and stadium name (from the game table) for every goal scored.
```sql
SELECT player, stadium
FROM game 
JOIN goal ON (id = matchid);
```
Modify it to show the player, teamid, stadium and mdate for every German goal.
```sql
SELECT player, teamid, stadium, mdate
FROM game 
JOIN goal ON (id = matchid)
WHERE teamid = 'GER';
```

4. Use the same **JOIN** as in the previous question.  
Show the team1, team2 and player for every goal scored by a player called Mario.
```sql
SELECT team1, team2, player 
FROM game
JOIN goal ON (id = matchid)
WHERE player LIKE 'Mario%';
```

5. The table eteam gives details of every national team including the coach.   
Show player, teamid, coach, gtime for all goals scored in the first 10 minutes.
```sql
SELECT player, teamid, coach, gtime
FROM goal 
JOIN eteam on teamid = id
WHERE gtime <= 10;
```

6. To JOIN game with eteam you could use either:
```sql
game JOIN eteam ON (team1 = eteam.id)
```
or:
```sql 
game JOIN eteam ON (team2 = eteam.id)
```
Notice that because id is a column name in both game and eteam you must specify eteam.id instead of just id.  
List the dates of the matches and the name of the team in which 'Fernando Santos' was the team1 coach.
```sql
SELECT mdate, teamname
FROM game
JOIN eteam ON (team1 = eteam.id)
WHERE coach = 'Fernando Santos';
```

7. List the player for every goal scored in a game where the stadium was 'National Stadium, Warsaw'.
```sql
SELECT player 
FROM goal
JOIN game ON (matchid = game.id)
WHERE stadium = 'National Stadium, Warsaw';
```

8. The example query shows all goals scored in the Germany-Greece quarterfinal.
```sql
SELECT player, gtime
FROM game JOIN goal ON matchid = id 
WHERE (team1 = 'GER' AND team2 = 'GRE');
```
Instead show the name of all players who scored a goal against Germany.  
*HINT*  
Select goals scored only by non-German players in matches where GER was the id of either team1 or team2.  
You can use teamid != 'GER' to prevent listing German players.  
You can use DISTINCT to stop players being listed twice.
```sql
SELECT DISTINCT(player)
FROM goal JOIN game ON id = matchid 
WHERE teamid != 'GER' AND (team1 = 'GER' OR team2 = 'GER');
```

9. Show teamname and the total number of goals scored.  
*COUNT and GROUP BY*  
You should COUNT(*) in the SELECT line and GROUP BY teamname.  
```sql
SELECT teamname, COUNT(*)
FROM goal
JOIN eteam ON goal.teamid = eteam.id
GROUP BY teamname;
```

10. Show the stadium and the number of goals scored in each stadium.
```sql
SELECT stadium, COUNT(*)
FROM goal
JOIN game ON goal.matchid = game.id
GROUP BY stadium;
```

11. For every match involving 'POL', show the matchid, date and the number of goals scored.
```sql
SELECT matchid, mdate, COUNT(*)
FROM goal 
JOIN game ON goal.matchid = game.id 
WHERE (team1 = 'POL' OR team2 = 'POL')
GROUP BY matchid;
```

12. For every match where 'GER' scored, show matchid, match date and the number of goals scored by 'GER'.
```sql
SELECT matchid, mdate, COUNT(*)
FROM goal
JOIN game ON game.id = goal.matchid
WHERE teamid = 'GER'
GROUP BY matchid;
```

# CASE
**CASE** allows you to return different values under different conditions.  
If there no conditions match (and there is not ELSE) then NULL is returned.  
```sql
CASE WHEN condition1 THEN value1 
     WHEN condition2 THEN value2  
     ELSE def_value   
END 
```

1. 
```sql
SELECT name, population, 
CASE WHEN population < 1000000 THEN 'small'
     WHEN population<10000000 THEN 'medium'
     ELSE 'large'
END
FROM bbc
```

# More JOIN operations
This tutorial introduces the notion of a join. The database consists of three tables:
```sql
movie(id, title, yr, director, budget, gross)
```

```sql
actor(id, name)
```

```sql
casting(movieid, actorid, ord)
```

1. List the films where the yr is 1962 [Show id, title].
```sql
SELECT id, title
FROM movie
WHERE yr = 1962;
```

2. Give year of 'Citizen Kane'.
```sql
SELECT yr
FROM movie
WHERE title = 'Citizen Kane';
```

3. List all of the Star Trek movies, include the id, title and yr (all of these movies include the words Star Trek in the title). Order results by year.
```sql
SELECT id, title, yr
FROM movie
WHERE title LIKE '%Star Trek%'
ORDER BY yr;
```

4. What id number does the actor 'Glenn Close' have?
```sql
SELECT id
FROM actor
WHERE name = 'Glenn Close';
```

5. What is the id of the film 'Casablanca'?
```sql
SELECT id
FROM movie
WHERE title = 'Casablanca';
```

## Joining two tables
1. Join casting and actor on actorid/id.
```sql
SELECT * FROM casting 
JOIN actor ON casting.actorid = actor.id
WHERE actor.name = 'John Hurt';
```
The result of the above gives one row for every element of the casting table which relates to John Hurt. In addition to the actorid we have the name of the actor involved.  

## Joining three tables    
2. Join casting and actor on actorid/id.
```sql
SELECT * 
FROM movie 
JOIN casting ON movie.id = movieid
JOIN actor ON actorid = actor.id
WHERE actor.name = 'John Hurt';
```
The result now again has one row for every element of the casting table, this time we get details of the movies as well as the name of the actor.  
  
Notice that in some cases we refer to a field using just the field name (e.g. actorid) and sometimes we preceed the field name with the table name (e.g. casting.actorid). You must include the table name if the field names are not unique.

6. Obtain the cast list for 'Casablanca'.  
*What is a cast list?*  
The cast list is the names of the actors who were in the movie.  
  
Use movieid = 11768, (or whatever value you got from the previous question).
```sql
SELECT actor.name 
FROM casting 
JOIN actor ON casting.actorid = actor.id 
WHERE casting.movieid = 11768;
```
or:
```sql
SELECT actor.name
FROM casting
JOIN actor ON casting.actorid = actor.id
JOIN movie ON casting.movieid = movie.id
WHERE movie.title = 'Casablanca';
```

7. Obtain the cast list for the film 'Alien'.
```sql
SELECT actor.name
FROM casting
JOIN actor ON casting.actorid = actor.id
JOIN movie ON casting.movieid = movie.id
WHERE movie.title = 'Alien';
```

8. List the films in which 'Harrison Ford' has appeared.
```sql
SELECT title
FROM movie
JOIN casting ON movie.id = casting.movieid
JOIN actor ON actor.id = casting.actorid
WHERE actor.name = 'Harrison Ford';
```

9. List the films where 'Harrison Ford' has appeared - but not in the starring role. [Note: the ord field of casting gives the position of the actor. If ord = 1 then this actor is in the starring role]  
To find movies where Harrison Ford appeared but was not the star, you should select movies where ord > 1 instead.
```sql
SELECT title
FROM movie
JOIN casting ON movie.id = casting.movieid
JOIN actor ON actor.id = casting.actorid
WHERE actor.name = 'Harrison Ford' AND casting.ord > 1;
```

10. List the films together with the leading star for all 1962 films.
```sql
SELECT movie.title, actor.name
FROM movie
JOIN casting ON movie.id = casting.movieid
JOIN actor ON actor.id = casting.actorid
WHERE yr = 1962 AND casting.ord = 1;
```

11. Which were the busiest years for 'Rock Hudson', show the year and the number of movies he made each year for any year in which he made more than 2 movies.
```sql
SELECT yr, COUNT(title) 
FROM movie 
JOIN casting ON movie.id = movieid
JOIN actor ON actorid = actor.id
WHERE name = 'Rock Hudson'
GROUP BY yr
HAVING COUNT(title) > 2;
```

12. List the film title and the leading actor for all of the films 'Julie Andrews' played in.
```sql
SELECT movie.title, actor.name
FROM movie
JOIN casting ON movie.id = casting.movieid
JOIN actor ON casting.actorid = actor.id
WHERE movie.id IN (
    SELECT movieid FROM casting
    JOIN actor ON casting.actorid = actor.id
    WHERE actor.name = 'Julie Andrews'
) 
AND casting.ord = 1;
```

13. Obtain a list, in alphabetical order, of actors who've had at least 15 starring roles.
```sql
SELECT name
FROM actor
JOIN casting ON casting.actorid = actor.id
WHERE casting.ord = 1
GROUP BY actor.name
HAVING COUNT(casting.ord) > 14
ORDER BY actor.name;
```

14. List the films released in the year 1978 ordered by the number of actors in the cast, then by title.
```sql
SELECT title, COUNT(casting.actorid)
FROM movie
JOIN casting ON casting.movieid = movie.id
WHERE movie.yr = 1978
GROUP BY casting.movieid
ORDER BY COUNT(casting.actorid) DESC, movie.title;
```

15. List all the people who have worked with 'Art Garfunkel'.
```sql
SELECT DISTINCT actor.name
FROM casting
JOIN actor ON casting.actorid = actor.id
WHERE casting.movieid IN (
    SELECT movieid FROM casting 
    JOIN actor ON casting.actorid = actor.id 
    WHERE actor.name = 'Art Garfunkel'
)
AND actor.name <> 'Art Garfunkel';
```