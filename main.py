print("Welcome to TipCalc!")

bill = float(input("What was total bill? $"))
tip = float(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? $"))

tip_percent = tip / 100
tip_value = bill*tip_percent
bill_with_tip = bill+tip_value

bill_per_person = bill_with_tip/people
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_amount}")