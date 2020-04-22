psql -U ah8140 -d ah8140 -h pgserver.mah.se

\c ah8140
drop database if exists akademigastrologi;
create database akademigastrologi;

drop table if EXISTS users;
drop table if EXISTS recipes;
drop table if EXISTS ingredients;

\c akademigastrologi;

create table users(
 userID serial UNIQUE,
 recipeID int,
 firstname varchar(20),
 lastname varchar(30),
 username varchar(20),
 email varchar(30),
 password varchar(20),
 primary key (userID),
 foreign key (recipeID) references recipes (recipeID)
 );

create table recipes(
 recipeID serial UNIQUE,
 userID int,
 title varchar(30),
 ingress varchar(250),
 instructions text,
 primary key (recipeID, userID),
 foreign key (userID) references users (userID)
 ); 

 create table ingredients(
 recipeID int,
 ingridient_name varchar(30),
 quantity int,
 measurement varchar(10),
 primary key (recipeID),
 foreign key (recipeID) references users (recipeID)
 );

 insert into users values
 (DEFAULT, DEFAULT);

insert into recipes values
 (DEFAULT, );

insert into ingredients values
 ();

