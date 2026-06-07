CREATE DEFINER=`root`@`localhost` PROCEDURE `playgame`(
	IN member_id int,
    IN game_id int,
    IN no_of_players int)
BEGIN
		declare game_price float;
        declare transaction_amount float;
        declare member_balance float;
        start transaction;
SELECT 
    price
INTO game_price FROM
    games
WHERE
    id = game_id;
        set transaction_amount=game_price*no_of_players;
SELECT 
    balance
INTO member_balance FROM
    members
WHERE
    id = member_id;
        if transaction_amount<=member_balance
        then
        insert into transactions(member_id,game_id,amount)values(member_id,game_id,transaction_amount);
        update members set balance=balance-transaction_amount where id=member_id;
        else
        select "Insufficient Balance" as "Error Message";
        END IF;
        commit;
	END