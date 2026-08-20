# Type Casting : int(), flaot(), str(), bool();


name = "Chhay"
numOfGoal = 1
relationShip = None

print(type(name))

name += "1"

print(name)


numOfGoal = float(numOfGoal)
print(numOfGoal)
print(type(numOfGoal))


numOfGoal = str(numOfGoal)
print(type(numOfGoal))

# cannot convet string of floating point directly to float
# numOfGoal = int(numOfGoal)
# print(type(numOfGoal))

print(relationShip)
relationShip = bool(relationShip)
print(relationShip)