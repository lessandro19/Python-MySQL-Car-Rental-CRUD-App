create schema rentalservice;
use rentalservice;

CREATE TABLE CUSTOMER
(CustID				smallint		NOT NULL,
 `Name`				varchar(30) 	NOT NULL,
 Phone				varchar(20) 	NOT NULL,
 PRIMARY KEY (CustIcustomerD)
); 
CREATE TABLE Vehicle
(
VehicleID	char(17)	NOT NULL,
`Description`	varchar(40)		NOT NULL,
`Year`	int,
`Type`	int,
Category int,
PRIMARY KEY	 (VehicleID)
);


CREATE TABLE RENTAL
(
CustID				smallint		not null,
VehicleID			char(17)	not null,
StartDate		    DATE    not null,
OrderDate			DATE	not null,
RentalType			int		not null,
Qty					int		not null,
ReturnDate			DATE	not null,
TotalAmount			int		not null,
PaymentDate			DATE,
PRIMARY KEY (CustID,VehicleID,StartDATE),
FOREIGN KEY (CustID) REFERENCES CUSTOMER(CustID),
FOREIGN KEY (VehicleID) REFERENCES Vehicle(VehicleID)
);

CREATE TABLE Rate
(`Type`	int	NOT NULL,
Category	int	NOT NULL,
Weekly	double,
Daily	double,
PRIMARY KEY	 (`Type`,Category,Weekly,Daily)
);

#Part 1 
INSERT INTO CUSTOMER
VALUES ("402","SP", "499-200-0700");


UPDATE CUSTOMER
SET Phone = "(837) 721-8965"
WHERE CustID ="02034433";

#Part 3
UPDATE Rate
SET Daily = Daily + (Daily * .05)
WHERE Category = 1;



#Part 4a
INSERT INTO Vehicle
VALUES("5FNRL6H58KB133711","Honda Odyssey 2019",NULL,NULL,NULL);


#Part 4b
INSERT INTO Rate
VALUES("5","1","900.00","150.00");

INSERT INTO Rate
Values("6","1","800.00","135.00");

#PART 5
SELECT DISTINCT Vehicle.VehicleID as VIN, Vehicle.`Description` , Vehicle.`Year`, Vehicle.`Type`, NULL as DaysRented
FROM (VEHICLE LEFT OUTER JOIN RENTAL on Rental.VehicleID = Vehicle.VehicleID)
WHERE (Vehicle.`Type` = 1 OR Vehicle.`Type`=2) AND ((Rental.StartDate is NULL or Rental.ReturnDate is NULL) or (Vehicle.VehicleID) not in(SELECT Vehicle.VehicleID																																										
																							FROM VEHICLE JOIN RENTAL on Rental.VehicleID = Vehicle.VehicleID                       
																							WHERE (Rental.StartDate > "2019-05-31" and Rental.StartDate < "2019-06-21") OR (Rental.ReturnDate > "2019-05-31" and Rental.ReturnDate < "2019-06-21")));



#PART 6
SELECT Customer.`Name`,Rental.TotalAmount as Balance
FROM CUSTOMER JOIN RENTAL on Customer.CustID=Rental.CustID
WHERE Rental.CustID=221 and PaymentDate is NULL;


#PART 7
create view vw_Vehicles as  SELECT V.VehicleID,V.`Description`,V.`Year`,   
	CASE    
		WHEN V.`Type` = 1 THEN "Compact" 
        WHEN V.`Type` = 2 THEN "Medium"
        WHEN V.`Type` = 3 THEN "Large"
        WHEN V.`Type` = 4 THEN "SUV"
        WHEN V.`Type` = 5 THEN "Truck" 
        WHEN V.`Type` = 6 THEN "Van"
        END, 

	CASE     
		WHEN V.`Category` = 0 THEN "Basic"     
        WHEN V.`Category` = 1 THEN "Luxury"    
        END,        R.Weekly,R.Daily 
FROM Vehicle as V JOIN Rate as R on V.`Type`=R.`Type`
ORDER BY V.`Category`;
SELECT * FROM vw_Vehicles;

#Part 8
SELECT SUM(Rental.TotalAmount) as TotalPayed
FROM Rental;

#Part 9a
create view vw_JBrown as SELECT V.`Description`,V.`Year`,	CASE    
		WHEN V.`Type` = 1 THEN "Compact" 
        WHEN V.`Type` = 2 THEN "Medium"
        WHEN V.`Type` = 3 THEN "Large"
        WHEN V.`Type` = 4 THEN "SUV"
        WHEN V.`Type` = 5 THEN "Truck" 
        WHEN V.`Type` = 6 THEN "Van"
        END, 

	CASE     
		WHEN V.`Category` = 0 THEN "Basic"     
        WHEN V.`Category` = 1 THEN "Luxury"    
        END,V.Category in Select(,










