# Ask the user for their name and age.
# If they are less than 18 or are named Darth print:
# “You are not eligible to vote.”
# If they are 18 or over and not named Darth print:
# “You are eligible to vote.!”


name = input("Enter your name: ")
age = int(input("Enter your age: "))
if age < 18 or name == "Darth":
    print("You are not eligible to vote.")
else:
    print("You are eligible to vote.!")
