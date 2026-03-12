create database SE;
use SE;

-- oue - 1-- 
create table Student(rollno int primary key,
				name varchar(50),
                branch varchar(50));

insert into Student values (1,'Devanshi','Computer Science'),
(2,'Tisha','Electronic and Com'),
(3,'Nilay','Electronic and Com');

 select * from Student;


create table Exam(rollno int,
			Scode varchar(10),
            marks int,
            Pcode varchar(10),
            foreign key (rollno) references Student(rollno));
            
insert into Exam values(1,'CS11',50,'CS'),
(2,'EC101',66,'EC'),
(2,'EC102',70,'EC'),
(3,'EC101',45,'EC'),
(3,'EC102',50,'EC');

select * from Exam;

-- Oue - 2 --  
create table People(first_name varchar(50),
			last_name varchar(50),
            address varchar(50),
            city varchar(50),
            age int);

insert into People values('Mickey','Mouse','123 Fantasy Way','Anaheim',73),
('Bat','Man','321 Cavern Ave','Gotham',54),
('Wonder','Woman','987 Truth Way','Paradise',39),
('Donald','Duck','555 Quack Street','Mallard',65),
('Bugs','Bunny','567 Carrot Street','Rascal',58),
('Wiley','Coyote','999 Acme Way','Canyon',61),
('Cat','Woman','234 Purrfect Street','Hairball',32),
('Tweety','Bird','543','Itottlaw',28);

SELECT * FROM People;


-- Que - 3 --
create table Employee (emp_id int primary key,
				first_name varchar(50),
                last_name varchar(50),
                salary int,
                join_date datetime,
                department varchar(50));
                
insert into Employee values (1,'Devanshi','lad',1000000,'2013-01-01 00:00:00','Banking'),
(2,'Tisha','patel',800000,'2013-01-01 00:00:00','Insurance'),
(3,'nilay','lad',700000,'2013-02-01 00:00:00','Banking'),
(4,'zinal','mistry',600000,'2013-02-01 00:00:00','Insurance'),
(5,'vivek','rathod',650000,'2013-02-01 00:00:00','Insurance'),
(6,'hetal','devare',750000,'2013-01-01 00:00:00','Services'),
(7,'param ','lad',650000,'2013-01-01 00:00:00','Services'),
(8,'zeel','rajput',600000,'2013-02-01 00:00:00','Insurance');

select * from Employee;

create table Incentive (emp_id int,
				Incentive_date date,
                Incentive_amount INT, foreign key (emp_id) references Employee(emp_id));
                
insert into Incentive values (1,'2013-02-01',5000),
(2,'2013-02-01',3000),
(3,'2013-02-01',4000),
(1,'2013-01-01',4500),
(2,'2013-01-01',3500);

select * from Incentive;

select first_name from Employee where first_name = "zinal";
select first_name , join_date, salary from Employee;
select * from Employee order by first_name asc , salary desc;
select * from Employee where first_name like 'h%';
select department,max(salary) from Employee group by department order by max(salary) asc;
select f.first_name , i.Incentive_amount from Employee f join Incentive i on f.emp_id = i.emp_id where i.Incentive_amount >3000;
create table Employee_log(emp_id int,
				first_name varchar(50),
                action_date datetime);

DELIMITER $$
CREATE TRIGGER after_employee_insert
AFTER INSERT ON Employee
FOR EACH ROW
BEGIN
INSERT INTO Employee_Log
VALUES(NEW.emp_id, NEW.first_name, NOW());
END$$
DELIMITER ;

INSERT INTO Employee VALUES
(9,'David','Lee',700000,'2013-03-01','Banking');
select * from Employee;


-- Que - 4 -- 
create table  Salesperson(Sno int primary key,
					Sname varchar(50),
                    city varchar(50),
                    comm decimal(4,2));
                    
insert into  Salesperson values (1001,'Devanshi','London',0.12),
(1002,'Tisha','San Jose',0.13),
(1004,'Nilay','London',0.11),
(1007,'Hetal','Barcelona',0.15),
(1003,'Sonu','New York',0.10);

select * from Salesperson;

create table Customer (Cnm int primary key,
				Cname varchar(50),
                city varchar(50),
                rating int,
                Sno int, foreign key (Sno) references Salesperson(Sno));
                
insert into Customer values (201,'param','London',100,1001),
(202,'zinal','Roe',200,1003),
(203,'hetu','San Jose',300,1002),
(204,'parth','Barcelona',100,1002),
(206,'mansi','London',300,1007),
(207,'mitali','Roe',100,1004);

select * from Customer;

-- table in orders details not given so that not show --  
select * from orders where amt > 1000;

select Sname,city from Salesperson where city = "London" and comm > 0.12;
select * from Salesperson where city = "Barcelona" or city = "London";
select * from Salesperson where comm > 0.10 and comm < 0.12;
select * from Customer where rating > 100 or city = "Roe";