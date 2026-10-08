# and, or, not

print(0 and "Hello")  # Output: 0 (0 is falsy, short-circuits)
print("Apple" or "Banana") # Output: Apple ("Apple" is truthy, short-circuits)
print("" or "Default")     # Output: Default (empty string is falsy, returns y)


score = 50

isPass = True if score >= 50 else False