num_of_small_bricks = int(input("Enter the number of small bricks: "))
num_of_large_bricks = int(input("Enter the number of large bricks: "))
goal = int(input("Enter the goal: "))
inches = num_of_small_bricks * 1 + num_of_large_bricks * 5
if goal > inches:
    print("You don't have enough bricks.")
else:
    large_needed = goal // 5
    small_needed = goal % 5
    print(f"You need {large_needed} large bricks and {small_needed} small bricks.")
