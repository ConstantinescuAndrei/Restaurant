create proc Register @Username varchar(200), @Email varchar(200), @Password varchar(200), @Address varchar(200)
as
    begin
        declare @UserExists int, @EmailExists int
        select @UserExists = Id
        from Users
        where UserName = @Username
        select @EmailExists = Id
        from Users
        where Email = @Email
        if(@UserExists is not null)
        begin
            throw 55000, 'Username exists', 1
        end
        if(@EmailExists is not null)
        begin
            throw 55000, 'Email exists', 1
        end
        insert into Users(UserName, Email, Password, Address) values
        (
         @Username, @Email, @Password, @Address
        )
        select top 1 * from Users order by Id  DESC
    end
