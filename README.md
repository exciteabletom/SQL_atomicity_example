# SQLite3 Atomicity example
### Tommy Dougiamas

Unfortunately the sample database data doesn't upload to git.   
Here are the schemas for the tables in the database if you want to test this yourself:
```
CREATE TABLE Customers (
ID PRIMARY KEY NOT NULL,
NAME TEXT NOT NULL
);

CREATE TABLE Preorders (
GAMEID NUMBER NOT NULL,
CUSTOMERID NUMBER NOT NULL,
PAYMENT BOOL DEFAULT "0" -- Has customer payed for the game?
);

CREATE TABLE Games (
ID PRIMARY KEY NOT NULL,
NAME TEXT NOT NULL
);
```

To use it just run `main.py {user's id} {game's id}`
