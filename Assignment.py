import math
price_of_each_cookie = 1.99
tip_for_each_cookie = 0.10
target_amount = 500

cookies_sold_for_hour = float(input("How many cookies sold in one hour?"))
working_hours_per_day = float(input("Number of hours working each day:"))

cookies_sold_in_day = cookies_sold_for_hour * working_hours_per_day
tip_for_each_day = cookies_sold_in_day * tip_for_each_cookie
total_tip = price_of_each_cookie * tip_for_each_cookie
amount_per_day = cookies_sold_in_day *(price_of_each_cookie + total_tip)

total_no_of_days = math.ceil(target_amount / amount_per_day)
print(f'It will be {total_no_of_days} days to earn ${target_amount}')
print(f'you get ${amount_per_day} in one day ')
if ((total_no_of_days + 6) % 7) ==0:
    print("The day we reach the target is Saturday ")
elif((total_no_of_days + 5) % 7) ==0:
    print("The day we reach the target is Sunday ")
elif((total_no_of_days + 4) % 7) == 0:
    print("The day we reach the target is Monday ")
elif((total_no_of_days + 3) % 7) == 0:
    print("The day we reach the target is Tuesday ")
elif((total_no_of_days + 2) % 7)  == 0:
    print("The day we reach the target is Wednesday ")
elif((total_no_of_days + 1) % 7)  == 0:
    print("The day we reach the target is Thursday ")
elif((total_no_of_days % 7) == 0):
    print("The day we reach the target is Friday ")
