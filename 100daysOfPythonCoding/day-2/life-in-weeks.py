print("Welcome - Let's Calculate your remaining Life inDays, week, and months")
print("Note: We assume that you are going to live by 90 years of age.")
print("Let's Start......")
current_age = int(input("enter your current age = "))
days_left = (90-current_age)*365
weeks_left = round(days_left/7)
months_left = round(days_left/30)
print(f"You have remaining {days_left} day, {weeks_left} weeks and {months_left} months")