import random

computer = random.choice(['T','H']) 
you = input("Enter your choice i.e ( H or T): ").upper()
print(f"Computer choose {computer} ")
if(computer == you):
    print("You won!")
else:
    print("You loose")    
