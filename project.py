import random

characters='''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-=_+[]\}{|;':",./<>?'''

while True:
    password_len=int(input(print('What length password do you need::')))
    no_of_passwords=int(input(print('how many passwords do you need::')))
    for i in range(0,no_of_passwords):
        password=''
        print(i)
        #for j in range(0,password_len):
        password=random.choices(characters,k=password_len)
        print('Here is your password::',password)
