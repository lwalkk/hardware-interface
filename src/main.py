import DbMan
#import rp_interface as rp
import time

#pi = rp.Connecter() 
database = DbMan.Connecter()

while(True):
    # triggers the 'sign-in' procedure
    char = input("input '*' to sign in, or '#' to sign out.") 

    if char == '*':
        
      response = input('First time? (y/n)  ')

      #if yes - request phone number, today's location
      if response == 'y':
        phone_num = input('Please enter your phone number: ')
        company = input('Please enter your company name: ')
        location = input('Where are you headed on site today? ')
        database.insert_new(phone_num, location, company)
        # if no - get name, phone number, company, today's location
      elif response == 'n':
        phone_num = input('phone# : ')
        location = input('location: ')
        database.insert_recurring(phone_num, location)

    elif char == '#':
        print('Sign out ...')
        phone_num = input('phone: ')
        database.remove(phone_num)
    else:
      print('invalid response, please try again.')
      time.sleep(2)



        
