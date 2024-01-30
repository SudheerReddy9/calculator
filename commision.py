commision_rate = 0.10
salesman = 0 
while salesman < 3 :
    sales = float(input("Enter the amount of my sales. "))
    commission = sales * commision_rate
    print("The commission is $", commission)