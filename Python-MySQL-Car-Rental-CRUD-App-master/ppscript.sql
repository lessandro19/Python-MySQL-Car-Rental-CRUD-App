create schema rentalservice;
use rentalservice;

CREATE TABLE CUSTOMER
(CustID				int		NOT NULL,
 Name				varchar(30) 	NOT NULL,
 Phone				varchar(20) 	NOT NULL,
 PRIMARY KEY (CustID),
 UNIQUE (CustID)
); 
CREATE TABLE Vehicle
(VehicleID	int	NOT NULL,
Description	int	NOT NULL,
Weekly	double,
Daily	double,
PRIMARY KEY	 (VehicleID)
);

CREATE TABLE RENTAL
(VehicleID			int	not null,
StartDate		    DATE    not null,
EndDate				DATE	not null,
RentalType			int		not null,
Qty					int		not null,
ReturnDate			DATE	not null,
TotalAmmount		int		not null,
PaymentDate			DATE,
CustID				int		not null,
PRIMARY KEY (StartDate,EndDate,RentalQty,ReturnDate,TotalAmount),
FOREIGN KEY (CustID) REFERENCES CUSTOMER(CustID),
FOREIGN KEY (VehicleID) REFERENCES Vehicle(VehicleID)
);

CREATE TABLE Rate
(Type	int	NOT NULL,
Category	int	NOT NULL,
Weekly	double,
Daily	double,
PRIMARY KEY	 (Type,Category)
);

#Part 1 
INSERT INTO CUSTOMER
VALUES ("02034433", "S", "499-200-0700");

#Part 2
UPDATE CUSTOMER
SET Phone = "(837) 721-8965"
WHERE CustID ="02034433";

#Part 3
UPDATE Rate
SET DailyRate = DailyRate + (DailyRate * .05)
WHERE Catergory = 1;

#Part 4a
INSERT INTO Vehicle
VALUES("5FNRL6H58KB133711","Honda Odyssey 2019");


#Part 4b
INSERT INTO Rate
VALUES("5","1","900.00","150.00");

INSERT INTO Rate
Values("6","1","800.00","135.00");







