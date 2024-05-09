# Welcome message
print("Welcome to the Prime Checker!")

while True:
  try:
    #Get a number from the user
    number = int(input("Please enter a whole number: "))
    
    #Check if the number is prime
    if number<2:
      prime = False
    else:
      prime = True
      divisor = 2
      while divisor * divisor <= number:
        if number % divisor == 0:
          prime = False
          break
        divisor += 1

      # Show the Result
      if prime:
          print(f"{number} is a prime number.")
      else:
          print(f"{number} is not a prime number.")
      break

  # Handel error
  except ValueError:
    print("That's not a number. Please enter a whole number.")
