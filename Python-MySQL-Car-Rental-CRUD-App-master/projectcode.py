


import MySQLdb
import datetime
db = MySQLdb.connect(
        host = "",
        user = "",
        passwd = "/",
        database=""
 )
mycursor = db.cursor()

def days_between(d1, d2):
    d1 = datetime.datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)






def formatprint(attributes,list1):
    print(', '.join(attributes))
    for item in list1:
        print(*item)
    
def return_vehiclerentals():
    choice=int(input("\nAlright, would you like to search by:\n1.VIN\n2.Description\n3.Enter a 'like' description\n4.See all rented vehicles\nChoice: "))
    if choice == 1:
        VIN=input("Please enter the VIN: ")
        mycursor.execute("""SELECT V.VehicleID,V.`Description`, R.StartDate,R.ReturnDate,R.TotalAmount\
                            FROM Vehicle as V left outer join Rental as R on V.VehicleID=R.VehicleID\
                            WHERE V.VehicleID = %s""", (VIN,))
        vehicles = mycursor.fetchall()
        
        attributes=["VIN","Description","Start Date","Return Date", "Total Amount"]
        formatprint(attributes,vehicles)
        
        
        
    elif choice == 2:
        Description=input("Please enter the Description ")
        mycursor.execute("""SELECT V.VehicleID,V.`Description`,R.StartDate,R.ReturnDate,R.TotalAmount\
                            FROM Vehicle as V left outer join Rental as R on V.VehicleID=R.VehicleID\
                            WHERE V.`Description` = %s""", (Description,))
        
        vehicles = mycursor.fetchall()
        attributes=["VIN","Description","Start Date","Return Date", "Total Amount"]
        formatprint(attributes,vehicles)
        
        
    elif choice == 3:
        Description=input("Please enter the 'like' description: ")
        mycursor.execute("""SELECT V.VehicleID,V.`Description`,R.StartDate,R.ReturnDate,R.TotalAmount\
                            FROM Vehicle as V left outer join Rental as R on V.VehicleID=R.VehicleID\
                            WHERE V.`Description` like '%%s%'""",(Description,))
        vehicles = mycursor.fetchall()
        attributes=["VIN","Description","Start Date","Return Date", "Total Amount"]
        formatprint(attributes,vehicles)

    else:
        mycursor.execute("""SELECT V.VehicleID,V.`Description`,R.StartDate,R.ReturnDate,R.TotalAmount\
                            FROM Vehicle as V inner join Rental as R on V.VehicleID=R.VehicleID""")
        vehicles = mycursor.fetchall()
        attributes=["VIN","Description","Start Date","Return Date", "Total Amount"]
        formatprint(attributes,vehicles)


def return_customerrentals():
    choice=int(input("\nAlright, would you like to search by:\n1.Name?\n2.Customer ID?\n3.See all customers that have rented a vehicle\nChoice:"))
    if choice == 1:
        CName=input("Please enter the customer name: ")
        mycursor.execute("""
                         SELECT C.`Name`,R.CustID, R.VehicleID, R.StartDate, R.OrderDate, R.RentalType,R.Qty,R.ReturnDate,R.TotalAmount,R.PaymentDate \
                         FROM   Rental as R inner join Vehicle as V on V.VehicleID=R.VehicleID inner join Customer as C on C.CustID=R.CustID \
                         Where  C.`Name` = %s""", (CName,))
        customers = mycursor.fetchall()
        for x,y in enumerate(customers):
            print(x,y)
        
            
    if choice == 2:
        CustID=input("Please enter your customer ID: ")
        mycursor.execute("""
                         SELECT R.CustID,C.`Name`, R.VehicleID, R.StartDate, R.OrderDate, R.RentalType,R.Qty,R.ReturnDate,R.TotalAmount,R.PaymentDate \
                         FROM   Rental as R inner join Vehicle as V on V.VehicleID=R.VehicleID inner join Customer as C on C.CustID=R.CustID \
                         Where  R.CustID = %s""", (CustID,))
        customers = mycursor.fetchall()
        for x,y in enumerate(customers):
            print(x,y)
        
    elif choice ==3:
        mycursor.execute("""
                         SELECT R.CustID,C.`Name`,R.VehicleID, R.StartDate, R.OrderDate, R.RentalType,R.Qty,R.ReturnDate,R.TotalAmount,R.PaymentDate \
                         FROM   Rental as R inner join Vehicle as V on V.VehicleID=R.VehicleID inner join Customer as C on C.CustID=R.CustID \
                         """)
        customers = mycursor.fetchall()
        for x,y in enumerate(customers):
            print(x,y)
        
             
           

def return_car():
    CName=input("Please enter the customer name: ")
    mycursor.execute("""
                         SELECT C.`Name`,R.CustID, R.VehicleID, R.StartDate, R.OrderDate, R.RentalType,R.Qty,R.ReturnDate,R.TotalAmount,R.PaymentDate,R.Returned \
                         FROM   Rental as R inner join Vehicle as V on V.VehicleID=R.VehicleID inner join Customer as C on C.CustID=R.CustID \
                         Where  C.`Name` = %s AND R.Returned = 0""", (CName,))
    customers = mycursor.fetchall()
    for x,y in enumerate(customers,1):
            print(x,y)
    customerchoice=int(input("Please choose the number of the rental you wish to return: "))
    customerchoice=customerchoice-1
    
    customerrental=customers[customerchoice] #get the specified customer rental that the customer chose
    CustID=customerrental[0]
    CName=customerrental[1]
    VehicleID=customerrental[2]
    ReturnDate=customerrental[3]
    TotalAmount=customerrental[4]
    PaymentDate=customerrental[5]
    
    mycursor.execute=("""
                      UPDATE Rental\
                      Set PaymentDate=GETDATE() AND Rental as R R.Returned = 1
                      Where PaymentDate is not NULL AND R.CustID=%s AND R.VehicleID=%s AND R.ReturnDate=%s""",(CustID,VehicleID,ReturnDate))
    
    
def add_customer():
    question = "In order to add a customer please provide the name and a phone number.\n"
    name = input("Enter the customer name: ")
    phone = input("Enter the customer phone: ")
    sql = "INSERT INTO customer (name,phone) VALUES (%s,%s)"
    val = (name,phone)
    mycursor.execute(sql,val)
    db.commit()


def add_vehicle():
    question ="In order to add a vehicle please provide the VIN, Description, Year, Type, and Category for the database.\n"
    VIN = input("Enter the VIN: ")
    Description = input("Enter the description: ")
    Year = input("Enter the year: ")
    Type = input("Enter the type: ")
    Category = input("Enter the category: ")
    sql="INSERT INTO vehicle (VehicleID,Description,Year,Type,Category) VALUES (%s,%s,%s,%s,%s)"
    val = (VIN,Description,Year,Type,Category)
    mycursor.execute(sql,val)

    db.commit()
    
def rent_vehicle():
    question="Please enter the dates you wish to rent a vehicle on using the format year-month-day\n"
    print(question)
    startdate=input("Enter the start date: ")
    startdatestr=startdate
    startdate=startdate.split("-")              #tokenize input to separe the year, month, and day
    startdate= [int(i) for i in startdate]      #cast every string in the list to an int
    startdate=datetime.date(startdate[0],startdate[1],startdate[2]) #create a date object to made up of the year, day, and month
    returndate=input("Enter the return date: ")
    returndatestr=returndate
    returndate=returndate.split("-")              #tokenize input to separe the year, month, and day
    returndate= [int(i) for i in returndate]      #cast every string in the list to an int
    returndate=datetime.date(returndate[0],returndate[1],returndate[2]) #create a date object to made up of the year, day, and month
    print("*The following vehicles are available to rent*\n")
    mycursor.execute("""
                     SELECT  V.VehicleID,V.`Description`,V.`Year`,V.`Type`,V.Category \
                     FROM Vehicle as V LEFT OUTER JOIN RENTAL  as R on V.VehicleID = R.VehicleID \
                     WHERE (R.StartDate is null and R.ReturnDate is null) OR (%s >R.StartDate AND %s> R.ReturnDate)""", (startdate,returndate,))
    carsavailable = mycursor.fetchall()
    attributes=["VIN","Description","Year","Type","Category"]
    print(', '.join(attributes))
    for x,y in enumerate(carsavailable,1):
        print(x, y)
    carchoice=int(input(("Which car number would you like?: "))) #gets the customers vehicle choice from the list of available vehicles
    carchoice=carsavailable[carchoice-1] #subtract one from the choice since python iterators start at 0
    vin=carchoice[0]             #get the VIN 
    vehicletype=carchoice[3]     #gets the type of vehicle 
    vehiclecategory=carchoice[4]      #gets the category of the vehicle    
    vehicleqty= days_between(startdatestr,returndatestr)                #get quantity for vehicle
    orderdate=datetime.datetime.today()
    returnstatus=0 #represents whether the car has been returned or not
    mycursor.execute("""
                                SELECT  R.Daily \
                                FROM Rate as R inner join Vehicle as V on R.Category=V.Category\
                                Where R.`Type` = %s AND R.Category = %s""",(vehicletype,vehiclecategory,))
    payment=mycursor.fetchall()
    payment=list(dict.fromkeys(payment))
    singlepayment=[x[0] for x in payment]
    singlepayment=singlepayment[0]
    payment = singlepayment * days_between(startdatestr, returndatestr) #find the total amount the person will have to pay for the duration of the rental
    payment = "%.2f" % payment
    print("The price will be: ","$",payment) #print the amount
    print("Are you going to pay today?yes/no\n") #ask user if they will pay now or later
    paymentflag=input() #get the user choice
    if (paymentflag == "yes"): #if the user chooses to pay right now then
        paymentdate=datetime.datetime.today()
        
        CustID=input("Enter your customer ID: ")
        mycursor.execute(""" INSERT INTO Rental \
                              VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",(CustID,vin,startdate,orderdate,vehicletype,vehicleqty,returndate,payment,paymentdate,returnstatus,))
        db.commit()
    elif (paymentflag == "no"):
        paymentdate=None
        CustID=input("Enter your customer ID: ")
        mycursor.execute(""" INSERT INTO Rental \
                              VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",(CustID,vin,startdate,orderdate,vehicletype,vehicleqty,returndate,payment,paymentdate,returnstatus,))
        db.commit()
    
    

status = 1 
print("Welcome to our Rental Service.\n\nWhat would you like to do?")
while(status == 1):
  partA="1:Add a new customer\n"
  partB="2:Add a new vehicle\n"
  partC="3:Rent a vehicle\n"
  partD="4:Return a car\n"
  partE="5:Search all rentals by customers\n"
  partF="6.Search all rentals by vehicles\nChoice:  "
  choice=int(input(partA+partB+partC+partD+partE+partF))
  if choice == 1:
      add_customer()
  elif choice == 2:
      add_vehicle()
  elif choice == 3:
      rent_vehicle()
  elif choice == 4:
      return_car()
  elif choice==5:
      return_customerrentals()
  elif choice==6:
      return_vehiclerentals()
  else:
      status = 0
      print("Have a nice day!\n")
     
