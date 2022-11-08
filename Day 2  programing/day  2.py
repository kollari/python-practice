# print a massage to welcom the user
print("welcome to calculator ")
# get the total bill 
total_bill = float(input("enter the total bill : $"))
# get the tip percentage
tip_percentage = int(input("enter the tip percentage 10 , 12 or 15  "))
# get people number 
people_number = int(input("how many people to split the bill "))
# print each person's bill
total = total_bill + tip_percentage * total_bill/100
bill_preson = total / people_number
print(f"each person should pay {bill_preson} ")