# Output to users
answer = input("What is the capital city of England?")

while answer.lower() != "london":
  print("Try again!")
  answer=input("What is the capital city of England?")
print("Well done!")
