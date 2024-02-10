#Logical Problem 1
number = int(input("Enter a number:"))
if number > 0:
	print("Number is Positive")
elif number <0:
	print("Number is Negative")
else:
	print("Number is Zero")

# Logical Problem 2
age = int(input("Enter your Age:"))
if age < 13:
	print("You are a child")
elif age > 12 and age < 19:
	print("You are teenager")
else:
	print("You are an adult")

#Logical Problem 3
num1 = int(input("Enter a number 1:"))
num2 = int(input("Enter a number 2:"))
if num1 > num2:
	print(num1,"is largest number.")
else:
	print(num2,"is largest number.")

#Logical Problem 4
year = int(input("Enter year:"))
if year % 4 ==0:
	print(year,"is a leap year.")
elif year %400 ==0:
	print(year,"is a leap year.")
elif year %100 ==0:
	print(year,"is not a leap year.")
else:
	print(year,"is not a leap year")

#Logical Problem 5
num1 = int(input("Enter the Number 1:"))
num2 = int(input("Enter the Number 2:"))
num3 = int(input("Enter the Number 3:"))

maximum = num1
minimum = num1

if num2 > maximum:
    maximum = num2
elif num2 < minimum:
    minimum = num2

if num3 > maximum:
    maximum = num3
elif num3 < minimum:
    minimum= num3

print("The maximum number is:",maximum)
print("The minimum number is:",minimum)

#Logical Problem 6

score = int(input("Enter your Exam Score:"))
if score >= 90 and score <=100:
	grade = "A"
elif score >=80 and score <=89:
	grade = "B"
elif score >=70 and score <=79:
	grade = "C"
elif score>=60 and score <=69:
	grade = "D"
else: 
    grade ="F"
print("your grade is",grade)
