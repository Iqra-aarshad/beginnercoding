#exercise 1
#take input from user
number = int(input("enter a number:"))
#check if the number is even or odd
if number % 2 == 0:
    print("even")
else:
    print("odd")
#exercise 2
#take input from user
year = int(input("enter a year:"))
#check if the year is the leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
#exercise 3
# #take input from user
age = int(input("please enter your age:"))
#check if the age is 18 or above
if age >= 18:
    print("you are an adult")
else:
    print("you are a minor")
#exercise 4
# #ask user to enter username and password
username = input("please eneter your username:")
password = input("plaese enter your password:")
#check if the username and password match the values
if username == "admin" and password == "1234":
    print("login successfull")
else:
    print("login failed")
#exercise 5
# #ask user to enter number
number = float(input("please enter a number:"))
#check if the number is positive or negative or zero
if number > 0:
    print("the number is positive")
    if number < 0:
        print("the number is neagtive:")
if number ==  0:
        print("the number is zero")
#exercise 6
#ask the user to enter three numbers
numbers = [1,2,3]
maximum = max(numbers)
print("the maximum number is:",maximum)
#exercise 7
#get the score from user
score = int(input("enter your numeric score:"))
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
    print("your grade is:", grade)
#exercise 8
#take input from user
number = int(input("enter a number:"))
is_prime = True
if number > 1:
    for i in range(2, number):
      if number % i == 0:
       is_prime = False
       break
#print the result
if is_prime:
    print(number, "is a prime number")
else:
    print(number, "is not a prime number")

# exercise 9
#ask the user to enter a first number 
num1 = input("enter te first number:")
num2 = input("enter the second number:")
if num1 > num2:
    print("the larger number is", num1)
elif num2 > num1:
    print("the larger number is", num2)
else:
    print("the numbers are equal")
