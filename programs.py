#HEALTHY LIFESTYLE
# Calorie Counter
age = int(input("Enter your Age:"))
weight = float(input("Enter your weight in kg:"))
activity_level = input("Enter your activity level.(low, moderate, high):")

if age <= 3:
    calories = 1000
elif age <= 8:
    calories = 1400
elif age <= 13:
    calories = 1800
elif age <= 18:
    calories = 2200
else:
    calories = 2000

if activity_level == "low":
    calorie_goal = calories * 1.2
elif activity_level == "moderate":
    calorie_goal = calories * 1.5
elif activity_level == "high":
    calorie_goal = calories * 1.8
else:
    calorie_goal = calories

print("Your calorie goal is:", calorie_goal, "calories.")

# Hydration Helper
weight = int(input("Enter your weight: "))
exercise_level = input("Enter your exercise level (light, moderate, intense): ")

if exercise_level == "light":
    water_intake = weight * 0.03
    print("To stay hydrated, you should drink", water_intake, "liters of water per day.")
elif exercise_level == "moderate":
    water_intake = weight * 0.04
    print("To stay hydrated, you should drink ", water_intake, "liters of water per day.")
elif exercise_level == "intense":
    water_intake = weight * 0.05
    print("To stay hydrated, you should drink", water_intake, "liters of water per day.")
else:
    print("Invalid exercise level. Please try again.")


# TIME MANAGEMENT PROGRAMS
    #To-Do List

task = input("Enter a task: ")
due_date = input("Enter the due date: ")
priority = input("Enter the priority (urgent, important, less important): ")

category = ""

if due_date == "today" or priority == "urgent":
    category = "Urgent"
elif due_date == "this week" or priority == "important":
    category = "Important"
else:
    category = "Less Important"

print("Your task has been added to to do list")
print("Task:",task)
print("Due date:",due_date)
print("priority:",priority)
print("category:",category)

# Pomodor Timer

import time

work_time = 25 * 60 
break_time = 5 * 60  

while True:
    print("Work for 25 minutes!")
    remaining_time = work_time
    while remaining_time > 0:
        time.sleep(1)
        remaining_time -= 1

    print("Time's up! Take a 5-minute break.")
    remaining_time = break_time
    while remaining_time > 0:
        time.sleep(1)
        remaining_time -= 1

    print("Break's over! Let's get back to work.")




# Meeting Scheduler


user1_calendar = "9:00 AM, 10:30 AM, 2:00 PM, 3:30 PM"
user2_calendar = "9:30 AM, 11:00 AM, 1:30 PM, 4:00 PM"
user3_calendar = "10:00 AM, 12:00 PM, 3:00 PM, 4:30 PM"

common_times = ""

for time_slot in user1_calendar.split(", "):
    if time_slot in user2_calendar and time_slot in user3_calendar:
        common_times += time_slot + ", "

if common_times != "":
    print("These times are available for a meeting: " + common_times[:-2])
else:
    print("No common meeting times found")