print("Welcome to tip calculator")
totalBill = float(input("What was the total bill $"))
tipPercentage = int(input("What percentage tip would you like to give? 10, 12 or 15  "))
no_of_people = int(input("How many people to split the bill? "))
bill_per_person = (totalBill + (totalBill*tipPercentage/100))/no_of_people
#final_amount = round(bill_per_person,2)
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: {final_amount}")