# All variables needed to calculate the employee wages
wages = 0.0
normal_hours = 0
overtime_hours = 0
commission = 0.0

print("Python stores employee Wage Calculator Program")
print()

# inputs for the number of hours and sales the employees did
num_hours = int(input("please enter the number of hours worked by employee"))
sales = float(input("please enter the amount of sales for employee £"))

# calculations for the employee hours and commissions
if num_hours <= 40: 
    normal_hours = num_hours

if num_hours > 40:
    normal_hours = 40
    overtime_hours = num_hours - 40

if sales > 1.00 and sales < 99.99:
    commission = sales + 5 / 100.0
              
if sales > 300.0:
    commission = sales * 15 / 100.0

wages = normal_hours * 9.50 + overtime_hours * (9.50 * 1.5) + commission

# outputs for the employee hours and comissions
print()
print('Number of hours worked @ normal rate = ',normal_hours, ' x $', (9.50))
print('Number of hours worked @ overtime rate = ',overtime_hours, ' x $', (9.50 * 1.5))
print('Commission earend = $', commission)

print('total wage = $', wages)