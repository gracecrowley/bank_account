
def withdraws(bal,withdraw_list):
  withdraw_amnt = float(input("How much would you like to withdraw?\n"))
  bal = bal - withdraw_amnt
  withdraw_list.append(withdraw_amnt)
  return bal

def deposits(bal,deposits_lists):
  deposit_amnt = float(input("How much would you like to deposit?\n"))
  bal = bal + deposit_amnt
  deposit_list.append(deposit_amnt)
  return bal

def interest(bal):
  interest_earned = bal + bal * .015
  return interest_earned


name = input("Please enter your name:\n")
bal = float(input("Please enter the starting balance of your account:\n"))


withdraw_list =[]
deposit_list = []

loop = True
while loop == True:
  print()
  print(f"Hi, {name}")
  command = input("Please choose from the menu:\nwithdraw\ndeposit\ninterest\ntransactions\nexit\n")
  if command == "withdraw":
    bal = withdraws(bal,withdraw_list)
    print("Your updated balance is: ",bal)
    print("you made the following withdrawal transactions: ", withdraw_list)
  elif command == "deposit":
    bal = deposits(bal,deposit_list)
    print("Your updated balance is: ",bal)
    print("you made the following deposit transactions: ", deposit_list)
  elif command =="interest":
    print("Your interest in 1 year will be: ", interest(bal))
  elif command =="transactions":
    print("your list of withdrawals is: ", withdraw_list)
    print("your lift of deposits is: ",deposit_list)
  elif command == "exit":
    print("Goodbye")
    loop = False
  else:
    print("Command not understood!")




