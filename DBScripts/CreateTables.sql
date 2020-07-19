CREATE DATABASE Restaurant;

USE Restaurant;

CREATE TABLE Items(
	Id int primary key auto_increment,
	Name varchar(200),
	ImageName varchar(200),
	PricePerUnit int
);

CREATE TABLE Users(
	Id int primary key auto_increment,
	UserName varchar(200),
	Email varchar(200),
	Password varchar(200),
	Address varchar(200)
);

CREATE TABLE Cart(
	Id int primary key auto_increment,
	UserId int references Users(Id)
);

CREATE TABLE Content(
	Id int primary key auto_increment,
	ItemId int references Items(Id),
	ItemQuantity int,
	CartId int references Cart(Id)
);
