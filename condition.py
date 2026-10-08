age = int( input("How old are you? : "))


if age <= 16:
  print("You are a teenageer")
elif age >=17 and age < 60:
  print("you are an adult")
elif age == 0:
  print("You are a toodler")
else :
  print("You are an old person")