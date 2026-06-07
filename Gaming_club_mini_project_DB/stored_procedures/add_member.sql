CREATE DEFINER=`root`@`localhost` PROCEDURE `add_member`(
	IN member_name VARCHAR(100),
    IN initial_recharge_amount FLOAT,
	IN phone_number varchar(15)
)
BEGIN
DECLARE member_id INT;
-- DECLARE EXIT HANDLER FOR SQLEXCEPTION
	BEGIN
        ROLLBACK;
    END;
    START TRANSACTION;
        INSERT INTO members (name, phone) 
        VALUES (member_name, phone_number);

        -- 2. get just now inserted id of member
        SET member_id = LAST_INSERT_ID();

        -- 3. insert into recharges
        INSERT INTO recharges (member_id, amount) 
        VALUES (member_id, initial_recharge_amount);

        -- 4. update balance in members
        UPDATE members SET balance =initial_recharge_amount WHERE id = member_id;

        -- 5. insert/update collections
        IF (SELECT COUNT(*) FROM collections 
            WHERE DATE(date) = CURDATE()) = 0 THEN

            INSERT INTO collections (amount, date) 
            VALUES (initial_recharge_amount, NOW());

        ELSE
            UPDATE collections SET amount = amount + initial_recharge_amount WHERE date = CURDATE();
        END IF;
    COMMIT;
END