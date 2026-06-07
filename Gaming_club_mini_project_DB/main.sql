create database gaming_club;
use gaming_club;

CREATE TABLE members (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(64) NOT NULL,
    balance float NOT NULL DEFAULT 0 check(balance >= 0 and balance <= 10000),
    phone VARCHAR(10) NOT NULL UNIQUE);
    	
CREATE TABLE games (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(20) NOT NULL UNIQUE,
    price float NOT NULL,
    description VARCHAR(100)
);
	
CREATE TABLE recharges (
    id INT AUTO_INCREMENT PRIMARY KEY,
    member_id INT NOT NULL,
    amount float NOT NULL CHECK (amount >= 100 and amount <= 1000),
    recharge_datetime DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (member_id) REFERENCES members(id) ON UPDATE CASCADE ON DELETE CASCADE);
  
CREATE TABLE transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    member_id INT NOT NULL,
    game_id INT NOT NULL,
    amount float NOT NULL CHECK (amount > 0),
    transaction_date date  DEFAULT (CURDATE()),
    foreign key(member_id) references members(id) on update cascade on delete cascade,foreign key(game_id) references games(id));
    
CREATE TABLE collections (
    id INT AUTO_INCREMENT PRIMARY KEY,
    amount float NOT NULL,
    date DATE DEFAULT (CURDATE()) unique);
    
SELECT table_name, engine FROM information_schema.tables WHERE table_schema = 'gaming_club';
select * from members;
select * from recharges;
select * from collections;
insert into games(name, description, price) values('chess', 'two players are allowed to play this game. Maximum one hour is allowed', 400);

insert into games(name, description, price) values('tennis', '4 players are allowed to play this game. Maximum two hours is allowed', 1000);

insert into games(name, description, price) values('bowling', 'a maximum of 5 players are allowed to play this game. Maximum one hour is allowed', 1500);
select LAST_INSERT_ID();
select * from games;
select * from members;
select * from recharges;
select * from collections;
select * from transactions;

CALL add_member('arun', 400, '8899889900');
-- drop table transactions;
-- drop table games;
-- drop table recharges;
-- drop table members;
-- drop table collections;
CALL add_member('vaishu', 580,'8096425614');
CALL recharge_wallet(2,300);
select * from games;
select * from members;
select * from recharges;
select * from collections;
select * from transactions;
CALL playgame(2,1,1);
select * from games;
select * from members;
select * from recharges;
select * from collections;
select * from transactions;