CREATE TABLE Items(
	Id int primary key identity,
	Name varchar(200),
	ImageName varchar(200),
	PricePerUnit int
);

CREATE TABLE Users(
	Id int primary key identity,
	UserName varchar(200),
	Email varchar(200),
	Password varchar(200),
	Address varchar(200)
);

CREATE TABLE Cart(
	Id int primary key identity,
	UserId int references Users(Id)
); 

CREATE TABLE Content(
	Id int primary key identity,
	ItemId int references Items(Id),
	ItemQuantity int,
	CartId int references Cart(Id)
);

ALTER TABLE Users WITH CHECK
	ADD CONSTRAINT UQ_Users_Email UNIQUE (Email)
	
	
ALTER TABLE Users WITH CHECK
	ADD CONSTRAINT UQ_Users_UserName UNIQUE (UserName)

