# Inserting rows 

When inserting data into a database, we need to use an **INSERT** statement, which declares which table to write into, the columns of data that we are filling, and one or more rows of data to insert. In general, each row of data you insert should contain values for every corresponding column in the table. You can insert multiple rows at a time by just listing them sequentially.  
```sql
INSERT INTO mytable
VALUES (value_or_expr, another_value_or_expr, …),
       (value_or_expr_2, another_value_or_expr_2, …),
       …;
```
In some cases, if you have incomplete data and the table contains columns that support default values, you can insert rows with only the columns of data you have by specifying them explicitly.
```sql
INSERT INTO mytable (column, another_column, …)
VALUES (value_or_expr, another_value_or_expr, …),
      (value_or_expr_2, another_value_or_expr_2, …),
      …;
```
In these cases, the number of values need to match the number of columns specified. Despite this being a more verbose statement to write, inserting values this way has the benefit of being forward compatible. For example, if you add a new column to the table with a default value, no hardcoded INSERT statements will have to change as a result to accommodate that change.  

```sql
movies(id, title, director, year, length_minutes)
```
```sql
boxoffice (movie_id, rating, domestic_sales, international_sales)
```

1. Add the studio's new production, Toy Story 4 to the list of movies (you can use any director).
```sql
INSERT INTO Movies (Title)
VALUES ('Toy Story 4');
```

2. Toy Story 4 has been released to critical acclaim! It had a rating of 8.7, and made 340 million domestically and 270 million internationally. Add the record to the BoxOffice table.
```sql
INSERT INTO Boxoffice
VALUES (15, 8.7, 340000000, 270000000);
```

# Updating rows
  
In addition to adding new data, a common task is to update existing data, which can be done using an **UPDATE** statement. Similar to the **INSERT** statement, you have to specify exactly which table, columns, and rows to update. In addition, the data you are updating has to match the data type of the columns in the table schema.
```sql
UPDATE mytable
SET column = value_or_expr, 
    other_column = another_value_or_expr, 
    …
WHERE condition;
```
  
The statement works by taking multiple column/value pairs, and applying those changes to each and every row that satisfies the constraint in the **WHERE** clause.  
  
*Taking care*  
Most people working with SQL will make mistakes updating data at one point or another. Whether it's updating the wrong set of rows in a production database, or accidentally leaving out the **WHERE** clause (which causes the update to apply to all rows), you need to be extra careful when constructing **UPDATE** statements.  
  
One helpful tip is to always write the constraint first and test it in a **SELECT** query to make sure you are updating the right rows, and only then writing the column/value pairs to update.  
  
```sql
movies(id, title, director, year, length_minutes)
```

1. The director for A Bug's Life is incorrect, it was actually directed by John Lasseter.
```sql
UPDATE Movies
SET Director = 'John Lasseter'
WHERE Title = "A Bug's Life";
```
  
2. The year that Toy Story 2 was released is incorrect, it was actually released in 1999.
```sql
UPDATE Movies
SET Year = 1999
WHERE Title = 'Toy Story 2';
```

3. Both the title and director for Toy Story 8 is incorrect! The title should be "Toy Story 3" and it was directed by Lee Unkrich.
```sql
UPDATE Movies
SET Title = 'Toy Story 3', Director = 'Lee Unkrich'
WHERE Title = 'Toy Story 8';
```

# Deleting rows  
  
When you need to delete data from a table in the database, you can use a DELETE statement, which describes the table to act on, and the rows of the table to delete through the WHERE clause.  
  
```sql
DELETE FROM mytable
WHERE condition;
```
  
If you decide to leave out the **WHERE** constraint, then all rows are removed, which is a quick and easy way to clear out a table completely (if intentional).  
  
*Taking extra care*  
Like the **UPDATE** statement from last lesson, it's recommended that you run the constraint in a **SELECT** query first to ensure that you are removing the right rows. Without a proper backup or test database, it is downright easy to irrevocably remove data, so always read your **DELETE** statements twice and execute once.  
  
```sql
movies(id, title, director, year, length_minutes)
```

1. This database is getting too big, lets remove all movies that were released before 2005.
```sql
DELETE FROM Movies
WHERE Year < 2005;
```

2. Andrew Stanton has also left the studio, so please remove all movies directed by him.
```sql
DELETE FROM Movies
WHERE Director = 'Andrew Stanton';
```