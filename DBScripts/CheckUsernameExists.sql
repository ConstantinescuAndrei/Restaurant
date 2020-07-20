create function CheckUsernameExists(@Username varchar(200))
returns bit
as begin
    declare @UsernameExists bit;
    declare @UserWithReceivedUsernameId int;
    select @UserWithReceivedUsernameId = Id
    from Users
    where UserName = @Username
    if(@UserWithReceivedUsernameId is not null)
        set @UsernameExists = 1
    else
        set @UsernameExists = 0
    return @UsernameExists
end;
