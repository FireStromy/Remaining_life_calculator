#Remaining Life Calculator

#Problem
''' Calculate remaining life of user considering he will live for 90 years '''
#Solution

print("*** Welcome to life calculator ***\n")

#Asking user age
age = input("What is your current age?\n Enter Age in years: ")
age_int = int(age)

#Calculating his remaining life
remaing_years = (90 - age_int)
t_days_left = remaing_years*365
t_weeks_left = remaing_years*52
t_months_left = remaing_years*12
print()
#printing result
print (f"You have {t_days_left} days, {t_weeks_left} weeks, and {t_months_left} months left.")

print()
print(" This is just for fun if you follow Healthy habits you will live more :)")
print()
print("*** Thank you ***")