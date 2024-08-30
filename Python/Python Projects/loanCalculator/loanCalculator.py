from matplotlib import pyplot

def get_loan_info():
    """ Display Load details"""
    loan = {}
    # get loan information from the user
    loan['principal'] = float(input("Enter the loan amount: "))
    loan['rate'] = float(input("Enter the interest rate: "))/100
    loan['monthlyPayment'] = float(input("Enter your monthly payment: "))
    loan['moneyPaid'] = 0
    return loan


def show_loan_info(loan, monthNumber):
    """Display the basic information of a loan
    """
    print(f"\n---Loan Information after {monthNumber} months\n")
    for key, value in loan.items():
        print(f"{key.title()} : {value}")


def collect_interest(loan):
    """ Update loan for each interest payment"""
    loan['principal'] = loan['principal'] + loan['principal']*loan['rate'] / 12
    
     

def make_monthly_payment(loan):
    """ Simulate making a monthly payment"""
    loan['principal'] = loan['principal'] - loan['monthlyPayment']
    # you are requuired to make a full payment
    if loan['principal'] > 0:
        loan['moneyPaid'] += loan['monthlyPayment']
    # not required to make full payment, loan is paid off
    else:
        # loan principal will be negative to run it
        loan['moneyPaid'] += loan['monthlyPayment'] + loan['principal']
        loan['principal'] = 0
    






def summarize_loan(loan, number, initial_principal):
    """ Display the final details of the loan"""
    print(f"\nCongraulations! You paid off your loan in {number} months ({round(number / 12, 2)} years).")
    print(f"\nYour Initial loan was ${initial_principal} at the rate of {loan['rate']*100}%.")
    print(f"Your monthly payment was  {loan['monthlyPayment']}.")
    print(f"You spent ${round(loan['moneyPaid'],2)} in total.")

    interest = round(loan['moneyPaid'] - initial_principal, 2)
    print(f"Your total interest payment is ${interest}.")
    




def create_loan_graph(data, loan):
    """ Create a graph of the payments"""
    x_value = []        # month numbers
    y_value = []        # principal value in month
    # point is a tuple. point[0] is month and point[1] is principal value
    for point in data:
        x_value.append(point[0])
        y_value.append(point[1])

    # plotting on x and y values
    pyplot.plot(x_value, y_value)
    pyplot.title(f"{100*loan['rate']}% Interest with ${loan['monthlyPayment']} monthly payment")
    pyplot.xlabel("Month Number")
    pyplot.ylabel("Principal of Loan")

    pyplot.show()


# Main function
print("\n Welcome to the Loan Calculator App \n")
# initalize variables
month_number = 0
my_loan = get_loan_info()
starting_principal = my_loan['principal']
data_to_plot = []

show_loan_info(my_loan, month_number)
input("Please press 'Enter' to begin ")

while my_loan['principal'] > 0:
    if my_loan['principal'] > starting_principal:
        
        break
    # processing the loan by call above functions
    month_number += 1
    collect_interest(my_loan)
    make_monthly_payment(my_loan)
    data_to_plot.append((month_number, my_loan['principal']))
    show_loan_info(my_loan, month_number)

    if my_loan['principal'] <= 0:
        summarize_loan(my_loan, month_number, starting_principal)
        create_loan_graph(data_to_plot, my_loan)
    else:
        print("Calculations shows you may never pay back your loan!!!")
        print("Either increase interest rate or payment")






