# Name: Lindsay Caudle
#   Prog Purpose: This Fresh Food Marketplace Employee Weekly Pay will allow
#   you to see how much an employee makes at this job.
#   You will be able to see the gross pay, deductions, and net pay for an employee.
#
#   Category codes and hourly pay rates:
#       C   Cashier         $16.50
#       S   Stocker         $15.75
#       J   Janitor         $15.75
#       M   Maintenance     $19.50
#
#   Deduction rates:
#       Federal income tax rate     12%
#       State income tax rate       3%
#       Social Security tax rate    6.2%
#       Medicare tax rate           1.45%

import datetime

#define global variables
job_code = 0
hours_worked = 0
gross_pay = 0
federal_tax = 0
state_tax = 0
social_secturity_tax = 0
medicare_tax = 0
total_deductions = 0
net_pay = 0

#define hourly pay rates tuple
hourly_pay_rates = (16.50, 15.75, 15.75, 19.50)

#define deductions rate tuple
deduction_rates = (0.12, 0.03, 0.062, 0.0145)

######## define program functions ########
def main():
    another_employee = True
    while another_employee:
        get_user_data()
        perform_calculations()
        display_results()
        yesno = input("\nWould you like to calculate data for another employee? (Y/N): ")
        if yesno.upper() !="Y":
                another_employee = False

# Collect job category cose and number of hours worked from the user
def get_user_data():
    global job_code, hours_worked
    job_code = input("Enter employee job category code (C,S,J,M): ")
    hours_worked = int(input("Total number of hours the employee worked: "))

# Gross pay, deductions, and net pay calculations (PER EMPLOYEE)
def perform_calculations():
    global job_code, hours_worked, gross_pay, federal_tax, state_tax, social_security_tax, medicare_tax, total_deductions, net_pay
    if job_code.upper() == "C":
        gross_pay = hours_worked * hourly_pay_rates[0]
    elif job_code.upper() == "S":
        gross_pay = hours_worked * hourly_pay_rates[1]
    elif job_code.upper() == "J":
        gross_pay = hours_worked * hourly_pay_rates[2]
    elif job_code.upper() == "M":
        gross_pay = hours_worked * hourly_pay_rates[3]
    else:
        print("\nCode entry not valid, please retype a valid code.")
    federal_tax = gross_pay * deduction_rates[0]
    state_tax = gross_pay * deduction_rates[1]
    social_security_tax = gross_pay * deduction_rates[2]
    medicare_tax = gross_pay * deduction_rates[3]
    total_deductions = federal_tax + state_tax + social_security_tax + medicare_tax
    net_pay = gross_pay - total_deductions

def display_results():
    print('\n-------------------------------')
    print('##### Fesh Food Marketplace #####')
    print('###### Employee Weekly Pay ######')
    print('---------------------------------')
    print('Job Code:                  ', job_code)
    print('Hours Worked:              ', hours_worked)
    print('Gross Pay                  $ ' + format(gross_pay, '10,.2f'))
    print('Federal Income Tax         $ ' + format(federal_tax, '10,.2f'))
    print('State Income Tax           $ ' + format(state_tax, '10,.2f'))
    print('Social Security Tax        $ ' + format(social_security_tax, '10,.2f'))
    print('Medicare Tax               $ ' + format(medicare_tax, '10,.2f'))
    print('Total Deductions           $ ' + format(total_deductions, '10,.2f'))
    print('Net Pay                    $ ' + format(net_pay, '10,.2f'))
    print('---------------------------------')
    print(str(datetime.datetime.now()))

########## call on main program to execute ##########
main()
