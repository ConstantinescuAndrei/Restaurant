create function Login(@Username varchar(200), @Password varchar(200))
returns bit
as
    begin
        declare @UserId int;
        declare @UserExists bit;
        select @UserId = Id
        from Users
        where UserName = @Username and Password = @Password
        if(@UserId is null)
            set @UserExists = 0
        else
            set @UserExists = 1
        return @UserExists
    end
