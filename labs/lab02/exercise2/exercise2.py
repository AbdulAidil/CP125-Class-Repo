# Lab 02 Exercise 2: Camping Logistics
# Write your code below:

import math

def calculate_event_cost(participants, tent_capacity, tent_price, meal_price):
    # TODO: Implement this function
    # Calculate total cost for tents and meals pass

    tents_needed = math.ceil(participants / tent_capacity)
    
    # Calculate total tent cost
    tent_cost = tents_needed * tent_price
    
    # Calculate total meal cost
    meal_cost = participants * meal_price
    
    # Total event cost
    total_cost = tent_cost + meal_cost
    return total_cost

# Test your code here
print("Testing Camping Logistics...")
print(calculate_event_cost(57, 6, 120, 15))