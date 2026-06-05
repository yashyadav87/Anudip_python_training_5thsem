Wap to calculate employee payroll and display grade

emp_name=input("Enter employee name: ")

basic_salary=float(input("Enter basic salary: "))
#validate basic salary
if(basic_salary<=0):
    exit("Basic salary should be positive")

#---------------------------------------------------
#calculating salary components
hra=basic_salary*20/100
da=basic_salary*10/100
pf=basic_salary*12/100

#---------------------------------------------------
#gross salary calculation
gross_salary=basic_salary+hra+da

#---------------------------------------------------
#net salary calculation
net_salary=gross_salary-pf

#---------------------------------------------------
#determining employee grade
if(net_salary>50000):
    grade="Senior Grade"
elif(net_salary>30000):
    grade="Mid Grade"
else:
    grade="Junior Grade"

#---------------------------------------------------
#displaying results
print("Employee Name =",emp_name)
print("Gross Salary =",gross_salary)
print("Net Salary =",net_salary)
print("Grade =",grade)
