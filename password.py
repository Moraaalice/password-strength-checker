import string  
#String is for accessing the String module for string constants
import getpass
#Get pass module for getting user input
def check_password_strength():
   password = getpass.getpass('Enter the password: ')
   #The line prompts the user to enter a password securely without displaying the input on the sscreen
   strength = 0
   remarks = ''
   lower_count = upper_count = num_count = wspace_count = special_count = 0
   for char in list(password):
       #Iterating over each password and converting it to a list
       if char in string.ascii_lowercase:
           lower_count += 1
       elif char in string.ascii_uppercase:
           upper_count += 1
       elif char in string.digits:
           num_count += 1
       elif char == ' ':
           wspace_count += 1
       else:
           special_count += 1
           #This section checks each character in the password and increament the corresponding counter variables based
           #on characters category ,uppercase,lowercase,digits


   if lower_count >= 1:
       strength += 1
   if upper_count >= 1:
       strength += 1
   if num_count >= 1:
       strength += 1
   if wspace_count >= 1:
       strength += 1
   if special_count >= 1:
       strength += 1  
       
       #These lines increment the strength variable based on the presence of different character types in the password.
       # Each character type found in the password increments the strength by 1.
       
       
   if strength == 1: 
       remarks = ('That\'s not a good password.'
           ' Change it as soon as possible.')
   elif strength == 2:
       remarks = ('That\'s a weak password.'
           ' You should consider using a tougher password.')
   elif strength == 3:
       remarks = 'Your password is okay, but it can be improved.'
   elif strength == 4:
       remarks = ('Your password is hard to guess.'
           ' But you could make it even more secure.')
   elif strength == 5:
       remarks = ('Now that\'s one hell of a strong password!!!'
           ' Hackers don\'t have a chance guessing that password!')



#These lines assign the appropriate remark based on the strength of the password, determined by the value of the 
# strength variable.

   print('Your password has:-')
   print(f'{lower_count} lowercase letters')
   print(f'{upper_count} uppercase letters')
   print(f'{num_count} digits')
   print(f'{wspace_count} whitespaces')
   print(f'{special_count} special characters')
   print(f'Password Score: {strength / 5}')
   print(f'Remarks: {remarks}') 
   
def check_pwd(another_pw=False):
       valid = False
       if another_pw:
           choice = input(
           'Do you want to check another password\'s strength (y/n) : ')
       else:
           choice = input(
           'Do you want to check your password\'s strength (y/n) : ')
           while not valid:
               if choice.lower() == 'y':
                   return True
               elif choice.lower() == 'n':
                   print('Exiting...')
               return False
           else:
               print('Invalid input...please try again. \n')


#These lines define a function named check_pwd() which prompts the user to check the strength of another password. 
# The another_pw parameter is used to determine if it's the first password check or a subsequent check. The function 
# returns True if the user wants to check another password, and False otherwise.

if __name__ == '__main__':
   print('===== Welcome to Password Strength Checker =====')
   check_pw = check_pwd()
   while check_pw:
       check_password_strength()
       check_pw = check_pwd(True)
       
       
#These lines are the main entry point of the program. It starts by printing a welcome message. 
# Then, it calls the check_pwd() function to determine if the user wants to check their password strength.
# If the user wants to check, it calls the check_password_strength() function. The loop continues until the user
# no longer wants to check passwords.       
               

   
        
    

