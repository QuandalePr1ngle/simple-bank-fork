#
# Darbības ar masīviem - https://www.w3schools.com/python/python_arrays.asp
# Datu tipi, mekle float - https://www.w3schools.com/python/python_datatypes.asp
# Pārbaudēm izmanto if...else - https://www.w3schools.com/python/python_conditions.asp
# Cipari https://www.w3schools.com/python/python_numbers.asp
#

balance = 0

while True:
  print("\nBanking Options:")
  print("1. Deposit")
  print("2. Withdraw")
  print("3. Check Balance")
  print("4. Exit")

  choice = input("Enter your choice (1-4): ")

  if choice == '1':
    print("if you want to exit, enter 0")
    deposit = float(input("Enter the amount to deposit: "))
    if deposit < 0:
      print(f"Invalid amount: {deposit}")
    elif deposit == 0:
      print("Exiting...")
      pass
    else:
      balance = balance + deposit
  elif choice == '2':
    print("if you want to exit, enter 0")
    withdraw = float(input("Enter the amount to withdraw: "))
    if withdraw > balance:
      print("You tried to withdraw more than you have!")
    elif withdraw < 0:
      print(f"Invalid amount: {withdraw}")
    elif withdraw == 0:
      print("Exiting...")
      pass
    else:
      balance = balance - withdraw
    pass
  elif choice == '3':
    print("Your balance is: ", balance)
    pass
  elif choice == '4':
    print("Exiting the banking system. Thank you!")
    break
  else:
    print("Invalid choice. Please enter a number between 1 and 4.")
