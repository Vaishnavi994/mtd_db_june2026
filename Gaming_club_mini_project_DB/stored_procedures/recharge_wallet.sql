CREATE DEFINER=`root`@`localhost` PROCEDURE `recharge_wallet`(
	IN member_id INT,
    IN recharge_amount FLOAT
)
BEGIN
	BEGIN
        ROLLBACK;
    END;
    START TRANSACTION;
	INSERT INTO recharges(member_id, amount) values(member_id, recharge_amount);
    
    UPDATE members SET balance = balance + recharge_amount WHERE id = member_id;
    IF 
		( SELECT COUNT(*) FROM collections WHERE date = curdate() ) = 0
	THEN
		INSERT INTO collections(amount) VALUES(recharge_amount);
	ELSE
		update collections SET amount = amount + recharge_amount WHERE date = curdate();
	END IF;
    COMMIT;
END