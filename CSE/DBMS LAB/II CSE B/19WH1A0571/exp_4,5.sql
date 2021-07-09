  
create database 19WH1A1222l;
use 19WH1A1222l;

create table bus(bus_no int primary key,fromplace varchar(20),toplace varchar(20));
insert into bus values (1,"banglore","hyderabad"),(2,"delhi","pune"),(3,"punjab","hyd");
insert into bus values(4,"mumbai","chennai");
select * from bus;

create table passenger(pno int primary key,name varchar(20),age int,gender varchar(20));
insert into passenger values(100,"meena",26,"female"),(200,"rohith",22,"male"),(300,"sreenidhi",15,"female");
select * from passenger;

create table ticket(tno int primary key,pno int, foreign key(pno) references passenger(pno),journey_date date,bus_fare int);
insert into ticket values(1000,100,"2021-12-16",560),(2000,200,"2021-12-17",480),(3000,300,"2021-12-18",720);
select * from ticket;

show tables;
select * from ticket where bus_fare >=500;
update ticket set journey_date = "2021-12-19";
select * from ticket;

alter table passenger add seat_no int;
update passenger set seat_no = 189;
alter table passenger modify name char(20);
update passenger set age = 32 where pno = 100;
select * from passenger;

alter table passenger drop seat_no;
select * from passenger;

select * from passenger order by age;
select * from passenger order by age desc;

delete from bus where bus_no =3;
select * from bus;

delete from bus;