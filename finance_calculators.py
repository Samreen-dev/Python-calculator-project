# This program allows the user to access two different financial calculators: an investment calculator and a home loan repayment calculator.

# If user chooses investment, user is asked to enter  amount of money for investment, rate and years of investment.

# User is also given option to choose if they want simple or compound interest. 

# The final amount the user will receive  after chosen number of years is rounded off to two decimal places and  printed.

# If user chooses home repayment, they are asked to enter current home value, interest rate and 

# the number of months they plan to take to repay the bond.

# Monthly repayment is calculated, rounded off to two decimal places and printed. 

import math

print("investment - to calculate the amount of interest")

print("bond - to calculate the amount you'll have to pay on a home loan \n")

user_choice = input("Enter either 'investment' or 'bond' from the menu above to proceed:")

print("\n")

choice = user_choice.lower()  #converts all the letters in user_choice to lower case.

if choice == "investment":

    principal = float(input("Please enter the amount of money you would like to invest £"))

    print("\n") # prints blank line
    
    user_rate = float(input("Please enter the The interest rate (as a percentage). Only the number of the interest rate should be entered "))

    rate = user_rate / 100

    print("\n") # prints blank line

    time = float(input("Please input the number of years you plan to invest "))

    print("\n")

    interest = input("Please enter'simple' if you want simple interest or 'compound'if you want compound interest ").lower()

    print("\n")

    if interest == "simple":

        amount = principal * (1 + rate * time)

        amount = round(amount, 2)

        print(f"If you invest £{principal} on simple interest you would get £{amount} amount after {time} years")

    elif interest == "compound":
        
        amount = principal * math.pow((1 + rate), time) 

        amount = round(amount, 2)

        print(f"If you invest £{principal} on compound interest you would get £{amount} amount after {time} years")

    else:
        
        print("You have not entered any valid option")

elif choice == "bond":

    value_house = float(input("Please enter the current value of house £"))

    print("\n")
    
    user_rate = float(input("Please enter the the interest rate(as percent). Only enter the number "))

    print("\n")

    rate = user_rate / 100

    rate = rate /12

    time = int(input("Please enter the number of months you plan to take to repay the bond "))

    print("\n")

    repayment = (rate * value_house)/(1 - (1 + rate)**(-time))

    repayment = round(repayment, 2)

    print(f"You will have to make monthly payment of £{repayment}")

else:
    
    print("You have not entered any valid option")



    




    




               
