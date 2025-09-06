#To generate multiple passwords at once.

import random
import string

def generatePassword(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

print("=" * 50)
print("CORNELIUS-SNOWHYT;s Advaned Password Geneator ")
print("=" * 50)

while True:
      try:
          #Ask for password length
          userInput = input("Enter password length (default = 12): ").strip()
          length = 12 if userInput == "" else int(userInput)

          if length <= 0:
            print("Please enter a number greater than 0.")
            continue

        #Ask for password length
          userInput2 = input("How many passwords do you want? (default = 1): ").strip()
          count = 1 if userInput == "" else int(userInput2)

          if count <= 0:
            print("Please enter a number greater than 0: ")
            continue

         
          print("Generated Password(s):")
          for i in range(1, count + 1):
            password = generatePassword(length)
            print(f"{i}. {password}")

          print("\nThank you for using CORNELIUS-SNOWHYT's Password Generator!\n")
          break
      except ValueError:
         print("Invalid input! Please enter a number only.\n")

           


    

