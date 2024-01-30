

import math
# on which day in the week we are going to reach the target
def day_reaching_target():
    if ((days_to_reach_target + 6) % 7) ==0:
        return "saturday"
    elif((days_to_reach_target + 5) % 7) ==0:
        return "sunday"
    elif((days_to_reach_target + 4) % 7) == 0:
        return "Monday"
    elif((days_to_reach_target + 3) % 7) == 0:
        return "Tuesday"
    elif((days_to_reach_target + 2) % 7)  == 0:
        return "Wednesday"
    elif((days_to_reach_target + 1) % 7)  == 0:
        return "Thursday"
    elif((days_to_reach_target % 7) == 0):
        return "Friday"
        

price_of_cookies = 1.99
percentage_of_tip = 0.10
target_funds = 500

# Total Number of cookies sold in an hour
cookies_per_hour = int(input("How many cookies will be sold in an hour?:"))

# Hours of work for each day
hours_per_day = int(input("How many hours each day they work?:"))

# Number of cookies sold per day
Cookies_sold_per_day = cookies_per_hour * hours_per_day

# Percentage of tip per cookies
tip_percentage = price_of_cookies * percentage_of_tip

# amount tip per day
tip_amount = Cookies_sold_per_day * tip_percentage


daily_funds = Cookies_sold_per_day *(price_of_cookies + tip_percentage)
days_to_reach_target = math.ceil(target_funds / daily_funds)
if days_to_reach_target > 1 :
    print(f'It will take {days_to_reach_target} days to earn ${target_funds} while selling {Cookies_sold_per_day} cookies per day.')
else:
    print(f'It will take {days_to_reach_target} day to earn ${target_funds} while selling {Cookies_sold_per_day} cookies per day.')
print(f'you will make ${daily_funds} in a day which also includes tip amount ${tip_amount:,.2f} per day.')
sud = day_reaching_target()
print(f'It will be {sud} on the day you reach your goal of ${target_funds}.')