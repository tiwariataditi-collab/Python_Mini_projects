input("Welcome to the tip calculator!")
bill = float(input("what was the total bill? $"))

tip = int(input("what percentage of tip would you like to give? 10, 12 or 15"))

people = int(input("how many people are there?"))

bill_to_pay = tip/ 100 * bill + bill
print(bill_to_pay)

bill_per_person = (bill_to_pay)/people
final_amount = round(bill_per_person, 2)
print(f" each person will pay {final_amount}")