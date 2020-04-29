# SQLite3 Atomicity example
### Tommy Dougiamas

## How to use
To use it just run `./main.py {user's id} {game's id}`.

Using the sample database, a userid of 210 and gameid of 100 should be True and anything else should be False.

## DB structure
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
