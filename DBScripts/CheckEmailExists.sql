create function CheckEmailExists(@Email varchar(200))
returns bit
as begin
    declare @EmailExists bit;
    declare @UserWithReceivedEmailId int;
    select @UserWithReceivedEmailId = Id
    from Users
    where Email = @Email
    if(@UserWithReceivedEmailId is not null)
        set @EmailExists = 1
    else
        set @EmailExists = 0
    return @EmailExists
end;
