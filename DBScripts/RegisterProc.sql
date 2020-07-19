create procedure Register(in InputUsername varchar(200), in InputEmail varchar(200), in InputPassword varchar(200),
in InputAddress varchar(200))
begin
    declare UserExists int;
    declare EmailExists int;
    select UserExists = Id
    from Users
    where UserName = InputUsername;
    select EmailExists = Id
    from Users
    where InputEmail = Email;
    if UserExists IS NOT NULL then
        signal sqlstate '55555' set message_text = 'Username exists';
    end if;
    if EmailExists IS NOT NULL then
        signal sqlstate '66666' set message_text = 'Email exists';
    end if;
    insert into Users(username, email, password, address) VALUES
    (
     InputUsername, InputEmail, InputPassword, InputAddress
    );
end;
