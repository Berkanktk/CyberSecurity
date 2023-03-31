# Databases and SQL

1. [What is a Database?](#what-is-a-database)
   1. [Columns](#columns)
   2. [Rows](#rows)
   3. [Relational Vs Non-Relational Databases](#relational-vs-non-relational-databases)
2. [What is SQL?](#what-is-sql)
   1. [Select](#select)
   2. [Insert](#insert)
   3. [Update](#update)
   4. [Delete](#delete)
   5. [Create](#create)
   6. [Drop](#drop)
   7. [Alter](#alter)
   8. [Union](#union)

## What is a Database?
A database is a way of electronically storing collections of data in an organised manner. A database is controlled by a DBMS which is an acronym for  Database Management System, DBMS's fall into two camps Relational or Non-Relational, the focus of this room will be on Relational databases,  some common one's you'll come across are MySQL, Microsoft SQL Server, Access, PostgreSQL and SQLite. 

Databases consist of columns and rows.

### Columns
Each column, better referred to as a field has a unique name per table. When creating a column, you also set the type of data it will contain, common ones being integer (numbers), strings (standard text) or dates. Some databases can contain much more complex data, such as geospatial, which contains location information. 

Setting the data type also ensures that incorrect information isn't stored, such as the string "hello world" being stored in a column meant for dates. If this happens, the database server will usually produce an error message. 

A column containing an integer can also have an auto-increment feature enabled; this gives each row of data a unique number that grows (increments) with each subsequent row, doing so creates what is called a key field, a key field has to be unique for every row of data which can be used to find that exact row in SQL queries.

### Rows
Rows or records are what contains the individual lines of data. When you add data to the table, a new row/record is created, and when you delete data, a row/record is removed.

### Relational Vs Non-Relational Databases:

**A relational database**, stores information in tables and often the tables have shared information between them, they use columns to specify and define the data being stored and rows to actually store the data. The tables will often contain a column that has a unique ID (primary key) which will then be used in other tables to reference it and cause a relationship between the tables, hence the name relational database.


**Non-relational databases** sometimes called NoSQL on the other hand is any sort of database that doesn't use tables, columns and rows to store the data, a specific database layout doesn't need to be constructed so each row of data can contain different information which can give more flexibility over a relational database.  Some popular databases of this type are MongoDB, Cassandra and ElasticSearch.

## What is SQL?
SQL (Structured Query Language) is a feature-rich language used for querying databases, these SQL queries are better referred to as statements.

### Select
The most common SQL statement is the SELECT statement, this statement is used to retrieve data from a database. The SELECT statement is used to retrieve data from a database. The data is returned in a table-like structure called a result set.

```sql
SELECT * FROM users;
```
This statement will select all the columns from the users table and return the result set. 

More spefic queries can be made by specifying the columns you want to select, for example:
```sql
SELECT username, password FROM users;
```
This statement will select the username and password columns from the users table and return the result set.

Other common Select statements are:
```sql
SELECT * FROM users LIMIT 1;
SELECT * FROM users WHERE username='admin';
SELECT * FROM users WHERE username != 'admin';
SELECT * FROM users WHERE username='admin' OR username='jon';
SELECT * FROM users WHERE username='admin' AND password='p4ssword';
SELECT * FROM users WHERE username LIKE 'a%'; -- Begins with a
SELECT * FROM users WHERE username LIKE '%a'; -- Ends with a
```

### Insert
The INSERT statement is used to insert new data into a database. The INSERT statement is used to insert new data into a database. The data is inserted into a table.

```sql
INSERT INTO users (username, password) VALUES ('admin', 'password');
```

This statement will insert a new row into the users table with the username and password columns set to admin and password respectively.

### Update
The UPDATE statement is used to update existing data within a database. The UPDATE statement is used to update existing data within a database. The data is updated within a table.

```sql
UPDATE users SET password='newpassword' WHERE username='admin';
```

This statement will update the password column in the users table where the username column is set to admin.

### Delete
The DELETE statement is used to delete existing data within a database. The DELETE statement is used to delete existing data within a database. The data is deleted from a table.

```sql
DELETE FROM users WHERE username='admin';
DELETE FROM users; -- Deletes all rows
```

This statement will delete the row from the users table where the username column is set to admin.

### Create
The CREATE statement is used to create new tables or databases within a database. The CREATE statement is used to create new tables or databases within a database. The data is created within a table.

```sql
CREATE TABLE users (id INT NOT NULL AUTO_INCREMENT, username VARCHAR(255), password VARCHAR(255), PRIMARY KEY (id));
```

This statement will create a new table called users with the columns id, username and password.

### Drop
The DROP statement is used to delete existing tables or databases within a database. The DROP statement is used to delete existing tables or databases within a database. The data is deleted from a table.

```sql
DROP TABLE users;
```

This statement will delete the users table.

### Alter
The ALTER statement is used to alter existing tables or databases within a database. The ALTER statement is used to alter existing tables or databases within a database. The data is altered within a table.

```sql
ALTER TABLE users ADD COLUMN email VARCHAR(255);
```

This statement will add a new column called email to the users table.

### Union
The UNION statement is used to combine the result-set of two or more SELECT statements from either a single or multiple tables. The data is combined within a table.

The rules to this query are that the UNION statement must retrieve the same number of columns in each SELECT statement, the columns have to be of a similar data type and the column order has to be the same. 

```sql
SELECT username FROM users UNION SELECT username FROM admins;
```

This statement will select the username column from the users table and the username column from the admins table and return the result set.
