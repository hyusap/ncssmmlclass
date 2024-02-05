width = float(input("What is the width of the room in feet? "))
length = float(input("What is the length of the room in feet? "))
feet_to_meters = 0.3048
area = width * length
area_meters = area * feet_to_meters**2

print(f"The area of the room is {area:.2f} square feet.")
print(f"The area of the room is {area_meters:.2f} square meters.")
