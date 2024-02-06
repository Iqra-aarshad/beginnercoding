#Problem 1
daily_steps = 3000
distance_walked = 2 
calories_burned = 125

average_steps_per_week = daily_steps * 7
total_distance_covered_in_month = distance_walked * 30
print(average_steps_per_week)
print(total_distance_covered_in_month)


#Problem 2
item1 = "Apples"
item2 = "milk"
item3 = "eggs"
quantity1 = 8
quantity2 = 4
quantity3 = 12
price1 = 2.0
price2 = 3.0
price3 = 5.0
total_cost = (quantity1*price1 + quantity2*price2 +quantity3*price3)

budget = 100.00
if total_cost <= budget:
    print("yes! you can buy these all items")
else:
    print("Your budget is not enough to buy all items.")


#Problem 3
flour_amount = 250 
sugar_amount = 150  

desired_servings = 8

adjusted_flour_amount = (flour_amount / 4) * desired_servings
adjusted_sugar_amount = (sugar_amount / 4) * desired_servings

print("For",desired_servings, "servings:")
print("Flour:",adjusted_flour_amount, "grams")
print("Sugar:",adjusted_sugar_amount, "grams")



#Problem 4
user_genre = "action"
user_rating = 7.5
user_release_year = 2010

movie1_genre = "action"
movie1_rating = 8.2
movie1_release_year = 2012

movie2_genre = "comedy"
movie2_rating = 6.9
movie2_release_year = 2011

if user_genre == movie1_genre and user_rating <= movie1_rating and user_release_year <= movie1_release_year:
    print("You will like Movie 1!")

if user_genre == movie2_genre and user_rating <= movie2_rating and user_release_year <= movie2_release_year:
    print("You might like movie 2!")


#Problem 5
task1_name = "reading books"
task1_duration = 30

task2_name = "coding"
task2_duration = 60

task3_name = "Research"
task3_duration = 45

# Calculate total time spent on each task

total_time_spent = task1_duration + task2_duration + task3_duration

print("Total time spent on", task1_name, ":", task1_duration, "minutes")
print("Total time spent on", task2_name, ":", task2_duration, "minutes")
print("Total time spent on", task3_name, ":", task3_duration, "minutes")
print("Total time spent on all tasks:", total_time_spent, "minutes")