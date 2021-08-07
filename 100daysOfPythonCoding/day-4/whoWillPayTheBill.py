import random
print("******Who will pay the bill********")
print("Few friends went to party and at the time of bill payment,")
print("They decided to randomly pick a name and then that person will pay the bill.")
print("THis programm will help to pick a random name from list of name.")
print("*************************************************************************")
names = input("Enter friends name seperated by comma : ")

#Method 1
list_of_names = names.split(',')
random_number_generator = random.randint(0,len(list_of_names)-1)
bill_will_be_paid_by = list_of_names[random_number_generator]

#Method 2
bill_will_be_paid_by1 = random.choice(list_of_names)
print("Method 1 ---- Bill will be paid by " + bill_will_be_paid_by)
print("Method 2 ---- Bill will be paid by " + bill_will_be_paid_by1)