import random

characters='''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-=_+[]\}{|;':",./<>?'''

while True:
    
    password_len=int(input('What length password do you need::'))
    no_of_passwords=int(input('how many passwords do you need::'))
    for i in range(0,no_of_passwords):
        final_password=''
        print(i)
        #for j in range(0,password_len):
        password=random.choices(characters,k=password_len)
        for j in password:
            final_password+=j
        print('Here is your password::',final_password)
    choice=input("Do you want to continue?\n(y/n)::")
    if choice=='n':
        break
    else:
        continue