weight = float(input("Weight: "))


weightType = input("(K)g or (L)bs: ")

# weightType = weightType.lower()
# print(weightType)

if weightType.lower() == 'k' :
  print(f"You are {weight / 0.45}Lbs")
elif weightType.lower() == 'l':
  print(f"You are {weight * 0.45}Kg")