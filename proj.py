#Question 1 
num1 = int(input("enter a number:"))
num2 = int(input("enter a number:"))
sum_of_squares = num1*num1 + num2*num2
if num1 and num2 %2 !=0:
    print(sum_of_squares)
else:
    print("sorry, Calculation is not perfomed")

#Question 2
num = int(input("enter a number:"))
if num < 0:
    print("sorry, factorial cannot be calculated for negative numbers.")
else:
    factorial = 1
    for i in range(1, num +1):
        factorial *= i
        print("the factorial of", num, "is:", factorial) 

#Question 3
import random
random_number = random.randint(1,100)
attempts = 5
print("let's play a guessing game!")
print("I have chosen a random number between 1 and 100")
print("you have 5 attempts to guess the number.")
while attempts > 0:
    guess = int(input("take a guess:"))
    if guess< random_number:
        print("Too low!")

    elif guess > random_number:
        print("Too high!") 
    else:
        print("Congratulations!You guessed the number.")
        break
    attempts -=1
    if attempts == 0:
        print("Game Over! You ran out of guesses.")
        print("The number was:", random_number)

#Question 4
# Get user input
num_of_people = int(input("enter the number of people:"))
cost_per_meal = int(input("enter the cost of each meal:"))
sales_tax_percentage = int(input("enter the sales tax percentage;"))
tip_percentage = int(input("enter the tip percentage:"))
# Calculate tottals
total_cost_of_food = num_of_people*cost_per_meal 
total_sales_tax = total_cost_of_food*(sales_tax_percentage/100)
total_tip_amount = total_cost_of_food*(tip_percentage/100)
total_bill_amount_per_person = (total_cost_of_food + total_sales_tax + total_tip_amount)/num_of_people
#print the result
print("total cost of food:Rs", total_cost_of_food)
print("Total sales tax:Rs", total_tip_amount)
print("Total bill amount per person:Rs", total_bill_amount_per_person)
