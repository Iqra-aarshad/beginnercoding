#Movie Ticket Prices
def calculate_ticket_price(age, day, num_of_tickets):
    ticket_price = 0
    
    if age == "adult" and day == "weekday":
        ticket_price = 12.0
    elif age == "child" and day == "weekday":
        ticket_price = 8.0
    elif age == "senior" and day == "weekday":
        ticket_price = 10.0
    else:
        ticket_price = 15.

    total_price = ticket_price * num_of_tickets

    # Apply discounts for family more than 4
    if num_of_tickets >= 4:
        discount_for_family = 1.0
        total_price -=discount_for_family*ticket_price

    return total_price

num_of_tickets = int(input("Enter the number of tickets: "))
age = input("Enter age (child/adult/senior): ")
day = input("Enter the day (weekday/weekend): ")
total_price = calculate_ticket_price(age, day, num_of_tickets)
print("The total price for", num_of_tickets, age, "tickets on", day, "is: $", total_price)

#Social Media Post Analyzer
def analyze_social_media_post(post_text):
    # Sentiment Analysis
    positive_words = ["happy", "excited", "love", "awesome"]
    negative_words = ["sad", "disappointed", "hate", "awful"]

    sentiment_score = sum(post_text.lower().count(word) for word in positive_words) - sum(
        post_text.lower().count(word) for word in negative_words)

    if sentiment_score > 0:
        sentiment = "Positive"
    elif sentiment_score < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    # Keyword Analysis
    words = [word.strip('.,?!') for word in post_text.lower().split()]
    keywords = [word for word in set(words) if len(word) > 3]

    # Emoji Analysis
    emojis = [char for char in post_text if char in ["🔥", "😄", '😐']]  # Use a list for emoji characters

    # Potential Trends (using hashtags as an example)
    hashtags = [word[1:] for word in words if word.startswith("#")]

    analysis_result = {
        "sentiment": sentiment,
        "keywords": keywords,
        "emojis": emojis,
        "hashtags": hashtags
    }

    return analysis_result

social_media_post = input("Enter your social media post:")
result = analyze_social_media_post(social_media_post)
print(result)


#Travel Cost Estimator
def estimate_travel_cost(destination, travel_style, duration):
    transportation_cost = 0
    accommodation_cost = 0
    activities_cost = 0

    # Transportation
    if travel_style == "budget":
        transportation_cost = 500  
    elif travel_style == "luxury":
        transportation_cost = 2000  

    # Accommodation
    if travel_style == "budget":
        accommodation_cost = 100 * duration
    elif  travel_style == "luxury":
        accommodation_cost = 500 * duration 

    # Activities
    if travel_style == "budget":
        activities_cost = 50 * duration  
    elif travel_style == "luxury":
        activities_cost = 200 * duration  

    total_cost = transportation_cost + accommodation_cost + activities_cost
    return total_cost

destination = input("Enter your destination:")
travel_style = input("Enter you travel style (budget/luxury):")
duration = int(input("Enter your duration"))

estimated_cost = estimate_travel_cost(destination, travel_style, duration)
print("The estimated travel cost for a", duration, "day", travel_style, "trip to", destination, "is $", estimated_cost)

#Restaurant Bill calculator
def calculate_total_bill(items, quantities, prices, discount=0, tax=0, num_friends=1):
    total_amount = 0
    for i in range(len(items)):
        item_total = quantities[i] * prices[i]
        total_amount += item_total

    total_amount -= discount  
    total_amount += total_amount * tax  

    if num_friends > 1:
        total_amount /= num_friends 


    return total_amount

items = ["Item 1", "Item 2", "Item 3"]
quantities = [2, 3, 1]
prices = [10, 15, 5]
discount = 5
tax = 0.1
num_friends = 2

total_bill = calculate_total_bill(items, quantities, prices, discount, tax, num_friends)
print("The total bill amount is: $", total_bill)
