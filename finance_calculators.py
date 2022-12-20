import math
# Program to calculate total investment returns with interest or bond loan repayment
print("Choose either 'investment' or 'bond' from the menu below to proceed:\n")
# \n and \t newline to organise user readable output
print("investment \t- to calculate the amount of interest you'll earn on your investment")
print("bond \t\t- to calculate the amount you'll have to pay on a  home loan\n")

# Create variable 'option' to store user inputted string
option = input("Please choose: bond/investment ")

# (1)
# While loop to prompt user to choose either bond or investment
# While variable does not equal the strings do else statement otherwise execute code
# of 'if-elif' statements if conditions are met
while option != "bond" or "investment":
    if option.lower() == "bond":
        break
    elif option.lower() == "investment":
        break
    else:
        print("Invalid input")
        option = input("Please choose: bond/investment ")

# (2)
# If while loop conditions are met then run this 'if' statement if 'investment' is chosen
if option.lower() == "investment":
    # Create variables to store user inputted float values
    deposit = float(input("The amount you will deposit: "))
    interest_rate = float(input("The interest rate (%): "))/100
    years = int(input("The number of years you plan to invest: "))
    interest = input("Would you like simple or compound? ")
    # Nested if-elif statement to prompt user to choose simple or compound interest
    if interest.lower() == "simple":
        total = deposit*(1+interest_rate*years)
    elif interest == "compound":
        total = deposit*math.pow((1+interest_rate), years)
        print(total)

# elif statement if user chooses bond option
elif option.lower() == "bond":
    house_value = float(input("What is value of house? "))
    anl_int_rate = float(input("The interest rate (%): "))/100
    mnthly_int_rate = anl_int_rate/12
    repayment = int(input("The number of months they plan to take to repay the bond: "))
    # Monthly repayment formula
    monthly_payment = (mnthly_int_rate * house_value)/ (1 - (1 + mnthly_int_rate) ** (-repayment))
    print(f"The monthly repayment will be: {round(monthly_payment, 2)}")
