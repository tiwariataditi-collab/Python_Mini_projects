print("welcome to the pizza hut! ")
print("order your pizza here 😋🤩")

size = input("what size of piuzza do you want to order ? S, M or L  :")
pepperoni = input ("do you want extra pepperoni? YES or NO")
cheese = input("do you want extra cheese? YES or NO")

bill = 0
if size == "S":
   bill+= 120
   print(bill)

elif size == "M" :
     bill += 200
     print(bill)

else:
    bill = 300

if pepperoni == "YES":
   bill += 10
   print(f" YOUR FINAL AMOUNT IS {bill}")

if cheese == "YES":
    bill+= 10
    print(f" YOUR FINAL AMOUNT IS {bill}")
 