#Practical problem 1
price_item1 = int(input("Enter the price of item 1:"))
price_item2 = int(input("Enter the price of item 2:"))
quantity_item1 = int(input("Enter the quantity of item 1:"))
quantity_item2 = int(input("Enter the quantity of item 2:"))
total_cost = (price_item1*quantity_item1+price_item2*quantity_item2)
if total_cost>1000:
    total_cost*=0.9
print("The total cost of your purchase is: $",total_cost)
	
#Practical problem2

temperature = int(input("Enter your temperature in celcius:"))
if temperature < 20:
	print("you should have to wear a jacket")
else:
	print("you dont have to wear jacket")

#Practical Problem 3


side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

if side1 == side2 == side3:
    print("It is equilateral triangle!")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("It is isosceles triangle!")
else:
    print("It is scalene triangle!")

#Practical problem 4
pin = 8745
balance = 12000
user_pin = int(input("Enter your PIN:"))
if user_pin == pin:
    withdraw_money = int(input("Enter amount to withdraw:"))
    if withdraw_money <= balance:
        print("Withdrawal successful")
    else:
        print("Sorry! Your balance is insufficient")
else:
    print("Invalid PIN! Try again")

#Practical problem 5
month = int(input("Enter the month number:"))

if month== 1:
    print("January has 31 days.")
elif month== 2:
    print("February has 28 or 29 days")
elif month == 3:
    print("March has 31 days.")
elif month== 4:
    print("April has 30 days.")
elif month== 5:
    print("May has 31 days.")
elif month== 6:
    print("June has 30 days.")
elif month== 7:
    print("July has 31 days.")
elif month== 8:
    print("August has 31 days.")
elif month == 9:
    print("September has 30 days.")
elif month == 10:
    print("October has 31 days.")
elif month == 11:
    print("November has 30 days.")
elif month == 12:
    print("December has 31 days.")
else:
    print("Invalid month number. Please try again.")

#Practical problem 6
year = int(input("Enter the year: "))
month = int(input("Enter the month: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    leap_year = True
else:
    leap_year = False

if month == 1:
    num_days = 31
elif month == 2:
    if leap_year:
        num_days = 29
    else:
        num_days = 28
elif month == 3:
    num_days = 31
elif month == 4:
    num_days = 30
elif month == 5:
    num_days = 31
elif month == 6:
    num_days = 30
elif month == 7:
    num_days = 31
elif month == 8:
    num_days = 31
elif month == 9:
    num_days = 30
elif month == 10:
    num_days = 31
elif month == 11:
    num_days = 30
elif month == 12:
    num_days = 31

print("The month", month, "in the year", year, "has", num_days, "days.")
