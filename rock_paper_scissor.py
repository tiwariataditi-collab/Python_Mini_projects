import random
while True:
 emojis = {"r": "🪨" , "p" : "📃" , "s" : "✂️"}
 choices =("r", "p", "s")

 user_choice= input("rock, paper,  or scissor?(r/p/s:)")
 if user_choice not in choices:
    print("invalid choice!")
 computer_choice= random.choice(choices)

 print(f"you chose {emojis[user_choice]}")
 print(f"computer chose {emojis[computer_choice]}")

 if user_choice == computer_choice:
   print("tie")
 elif user_choice == "r" and computer_choice =="s" or\
      (user_choice == "s" and computer_choice == "p") or \
      (user_choice == "p" and computer_choice == "r"):
      print("you win")   
 else:
      print("you lose")

 ask = input ("do you want to continue? (y/n):")
 if ask == "y":
    continue
 else:
      ask == "n"
      print("thanks for playing")
      break
 
