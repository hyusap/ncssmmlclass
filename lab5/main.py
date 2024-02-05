distance = float(input("what is the distance travelled in km? "))
time = float(input("what is the time taken in hours? "))
speed = distance / time
print(
    f"It takes {time:.2f} hours to travel {distance:.2f} km at a speed of {speed:.2f} km/h."
)

distance = float(input("what is the distance travelled in km? "))
speed = float(input("what is the speed in km/h? "))
time = distance / speed
print(
    f"It takes {time:.2f} hours to travel {distance:.2f} km at a speed of {speed:.2f} km/h."
)


time = float(input("what is the time taken in hours? "))
speed = float(input("what is the speed in km/h? "))
distance = time * speed
print(
    f"It takes {time:.2f} hours to travel {distance:.2f} km at a speed of {speed:.2f} km/h."
)
