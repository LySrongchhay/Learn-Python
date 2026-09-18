import os 
import subprocess
import math

subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)


money = 0

money = money + 1
money += 1
money *= money

money /= money
money += 1 

money **= 2

modulus = money % 3

print(money)
print(modulus)

x = 3.14
y = -4
z = 5

result = round(x)
print(result)

# abs is abosulute function example |-4| = 4
print(abs(y))

# power
print(pow(2, 3))

print(max(x, y, z))

print(min(x, y, z))


print(math.pi)
print(math.e)
print(math.sqrt(9))
print(math.ceil(1.2))
print(math.floor(1.9))

# # ===============================================================================================================
# # Find the length around a circle (circumference)
# # C = pi * d or C = 2 * pi * r
# radius = float(input('Enter the radius of the circle: '))

# circumference = 2 * math.pi * radius

# print(f"The circumference is: {round(circumference, 2)}cm")


# #===================================================================================================
# # Find the area of the circle

# radius = float(input("Enter the radius: "))

# area = math.pi * pow(radius, 2)
# print(f"The area is: {round(area, 2)} cm²")

# ==========================================================================================
# Find the hypotenuse of the right triangle

a = float(input('Enter side A: '))
b = float(input("Enter side B: "))
c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f'Side C is { round(c, 2)}cm')