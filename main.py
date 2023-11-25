#using a for loop to print number from 1 to 10
for num in range(1,11):
    print(num)

#get input from user 
number = int(input("enter a number:"))
#use a loop to print a multiplication table
for i in range(1,11):
    print(f"{number}x{i} = {number*i}")
    
#get the number from user
num = int(input("enter a number:"))
#intialize variables
sum = 0
#use a while loop to calculate the sum
while num > 0:
    sum += num
    num-=1
#print the sum
    print("the sum of natural number upto",num,"is", sum)
#define a list of names
names = ["iqra", "urwa", "dua", "aisha"]
#use for loop to iterate through each name in list
for name in names:
#print each name
    print(name)

#get user input for the number
number = int(input("enter a number:"))

#intialize variables
factorial = 1
current = 1

#calculate factorial using a while loop
while current <= number:
    factorial *= current
    current += 1

#print the factorial
print("the factorial of",number, "is:", factorial)
#get the number of terms from user 
terms = int(input("enter the number of terms:"))
#intialize first two terms
first_term = 0
second_term = 1
#print the series using loop
for i in range(terms):
    print(first_term,end="")
    temp = first_term + second_term
    first_term = second_termsecond_term = temp
#get the number from user 
number = int(input("enter a number:"))
#initialize variables 
reversed_number = 0
#reversed the number using a while loop 
while number > 0:
    digit = number%10
    reversed_number = (reversed_number * 10)+ digit
    number = number//10
#print the reversed number
print("reversed number:", reversed_number)

#get the string from user 
string = input("enter a string:")
#initialize the vowel
vowel_count = 0
#iterate through the sring using for a loop
for char in string:
    if char.lower() in "aeiou":
     vowel_count += 1
#print the vowel count
    print("number of vowels:", vowel_count)
#get the number from user
number = int(input("enter a number:"))
#store a copy of number
original_number = number
reversed_number = 0
#reverse the number using while loop
while number > 0:
    digit = number % 10
    reversed_number = (reversed_number *10) + digit
    number = number//10
    if original_number == reversed_number:
        print("the number is a palidrome.")
    else:
        print("the number is not a palidrome.")

#initialize the sum variables
sum_of_squares = 0
#iterate through the numbers from 1 to 5 using for loop
for num in range(1,6):
    sum_of_squares += num**2
print("the sum of squares of the numbers from 1 to 5 is:", sum_of_squares)




