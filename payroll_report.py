# * Class: CS3A
# * Description: The objective of this assignment is to display a weekly payroll report.
# * Due date: Monday, July 13, 2020
# * Name: Priya Jain
# * File name: payroll_report.py

total_gross = 0
total_state = 0
total_federal = 0
total_fica = 0
total_net = 0

print("Enter the following information:\n")

employee_num = int(input('Employee Number (0 to quit): '))
while employee_num < 0:
    print("Error: Employee number may not be less than zero. \n")
    employee_num = int(input('Re-enter employee number (0 to quit): '))
while employee_num != 0:
    gross_pay = float(input('Gross Pay: '))
    while gross_pay < 0:
        print("Gross pay may not be less than zero.")
        gross_pay = float(input('Re-enter gross pay: '))
    state_tax = float(input('State Tax: '))
    while state_tax < 0 or state_tax > gross_pay:
        print("Error: State tax may not be negative or greater than gross pay.")
        state_tax = float(input('Re-enter state tax: '))
    federal_tax = float(input('Federal Tax: '))
    while federal_tax < 0 or federal_tax > gross_pay:
        print("Error: Federal tax may not be negative or greater than gross pay.")
        federal_tax = float(input('Re-enter federal tax: '))
    fica_withold = float(input('FICA Witholdings: '))
    while fica_withold < 0 or fica_withold > gross_pay:
        print("Error: FICA witholding may not be negative or greater than gross pay.")
        fica_withold = float(input('Re-enter FICA witholdings: '))
    if state_tax + federal_tax + fica_withold > gross_pay:
        print("Error: Witholdings cannot exceed gross pay. \n")
        print("Please re-enter the data for this employee. \n")
    
    print("Processing the next employee.")
    employee_num = int(input('Employee Number (0 to quit): '))

    total_gross += gross_pay
    total_state += state_tax
    total_federal += federal_tax
    total_fica += fica_withold
    total_net += gross_pay - state_tax - federal_tax - fica_withold
    
    if employee_num == 0:
        print('Total gross pay:', total_gross)
        print('Total state tax:', total_state)
        print('Total federal tax:', total_federal)
        print('Total FICA witholdings:', total_fica)
        print('Total net pay:', total_net)

# Enter the following information:

# Employee Number (0 to quit): 1008
# Gross Pay: 100
# State Tax: 10
# Federal Tax: 20
# FICA Witholdings: 30
# Processing the next employee.
# Employee Number (0 to quit): 1234
# Gross Pay: 200
# State Tax: 20
# Federal Tax: 40
# FICA Witholdings: 60
# Processing the next employee.
# Employee Number (0 to quit): 2002
# Gross Pay: 300
# State Tax: 30
# Federal Tax: 60
# FICA Witholdings: 90
# Processing the next employee.
# Employee Number (0 to quit): 0
# Total gross pay: 600.0
# Total state tax: 60.0
# Total federal tax: 120.0
# Total FICA witholdings: 180.0
# Total net pay: 240.0
