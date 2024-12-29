try:
    age=int(input("Enter Age:"))
    print("Your age is:",age)
except ValueError:
    print("Hey!!! you little Goblin alien guy numbers only got it I'm watching!!!...")

if age%2==0:
    print("Your age is an even number!!!")
else:
    print("Your age is an odd number!!!")