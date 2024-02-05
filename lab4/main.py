import math

radius_of_sphere = float(input("Enter the radius of the sphere: "))
surface_area = 4 * math.pi * radius_of_sphere**2
volume = 4 / 3 * math.pi * radius_of_sphere**3

print(
    f"The surface area of a sphere with radius {radius_of_sphere:.2f} is {surface_area:.2f}."
)
print(f"The volume of a sphere with radius {radius_of_sphere:.2f} is {volume:.2f}.")
