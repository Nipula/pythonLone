import os
import time

#for console font color change 
def color(x):
    os.system(x)

#change console font color to green
color("color 02")

#for clear all in console
def clear_cmd():
    os.system('cls' if os.name == 'nt' else 'clear')

# funtion for start animation
def loading(width=70, message="BIT BUSTERS SOLUTIONS", t=0.05):
    # Calculate padding for message placement
    padding = (width - len(message)) // 2
    # Create frames for the loading animation
    frames = ['$' * i + '*' * (width - i) for i in range(width + 1)]
    for frame in frames:
        clear_cmd()
        # Print the current frame (loading bar) above and below the message
        print(frame)
        print('*' * padding + message + '*' * padding)
        print(frame)
        time.sleep(t)

# funtion for goodbye animation
def ending(width=70, message="GOOD BYEEE!!!!", t=0.05):
    # Calculate padding for message placement
    padding = (width - len(message)) // 2
    # Create frames for the loading animation
    frames = ['$' * i + '*' * (width - i) for i in range(width + 1)]
    for frame in frames:
        clear_cmd()
        # Print the current frame (loading bar) above and below the message
        print(frame)
        print('*' * padding + message + '*' * padding)
        print(frame)
        time.sleep(t)

# funtion for true conditon font color change
def c_true():
    #change font color to blue becourse conditon is true
    color("color 01")
    #wait 0.5 seconds
    time.sleep(0.5)
    #change font color to green
    color("color 02")

# funtion for false conditon font color change
def c_false():
    #change font color to red becourse conditon is false
    color("color 04")
    #wait 0.5 seconds
    time.sleep(0.5)
    #change font color to green
    color("color 02")

#funtion for ending
def code_end():
    input("Press any button to end this program")
    ending()

#funtion for loan calculation
def loan_cal():
    
    print("This will check your ability to get a loan")
    print("In this, you need to enter your NIC number and loan amount, etc.")
    # percentage 
    p = 0
    #create an empty dictonary for store nic1.txt file 
    nic_data = {}

    #importent !!!
    #if code have erros change the file path to your file destination
    #like "C:\Users\administretor\Desktop\python competiton\nic.txt"

    with open(r"C:\Users\A.A.N.Nuwanjith\Desktop\New folder (2)\python competiton\nic.txt", "r") as f1:
            for i in f1:
                x = i.strip().split(",")
                nic = x[0].strip()
                name = x[1].strip()
                age = 2023 - int(nic[0:4])
                status = x[3].strip()
                income = float(x[4].strip())
                loan_have = x[-2].strip()
                #dictoonary key is nic and values is nic, name, age, status, income, loan_have
                nic_data[nic] = (nic, name, age, status, income, loan_have)

#Repeat until the correct National ID number is entered
    while True:
        nic = input('Enter your National Identity Number: ')
        #Checking that the National Identity Card number is of the correct length and consists it only numbers or not
        if nic.isdigit() and len(nic) == 12:
            c_true()
            break
        else:
            print('The National ID number you entered is not valid. Please re-enter')
            c_false()

#get input for lone amount
    loan_amount = int(input('Enter the loan amount you wish to take: '))

#check nic number is in the nic data dictonary (for validation)
    if nic in nic_data:
        data = list(nic_data[nic])

        if data[0] == nic:
            #Checking the status of police reports on the customer
            if data[3] == 'VeryGood':
                p += 100
            elif data[3] == 'Good':
                p += 75
            elif data[3] == 'Bad':
                p += 55
            elif data[3] == 'VeryBad':
                p -= 10

#Scoring according to age
            age=data[2]    
            if age > 19 and age < 25:
                p += 50
            if age > 25 and age <= 50:
                p += 100
            if age > 50 and age <= 75:
                p += 40
            if age >= 80:
                p -= 10

#Comparing loan repayments with monthly income
            mp = float(data[4])
            if (mp / loan_amount) * 100 > 35:
                p += 100
            elif (mp / loan_amount) * 100 > 5:
                p += 55
            else:
                p += 15

# Check whether other loans have been taken during this period
            if data[5] == 'no':
                p += 100
            else:
                p += 40

#if Do you have a guarantor for the loan amount?
            x = input('Do you have a guarantor for the loan amount? (y/n)')

            if x == 'y':
                z = input('Enter the guarantor\'s name: ')
                while True:
                    y = input('Enter the guarantor\'s National Identification Number: ')
                    if y.isdigit() and len(y) == 12:
                        c_true()
                        p += 100
                        break
                    else:
                        print('Incorrect National ID Number. Re-enter.')
                        c_false()

#Calculation  percentage
    ATP = (p / 500) * 100
    if ATP >= 65:
        years = int(input('Enter years: '))
        bop = (15 / 100)
        for i in range(years):
            #Finding the total amount due at the end and finding the amount due for a month
            loan_amount = loan_amount + (loan_amount * bop)
        monthly_payment = loan_amount / (years * 12)
        print("The percentage you got for getting the loan successfully:", ATP, "%")
        print('The monthly payment of the loan you entered:', monthly_payment, "/=")
        c_true()
        
    else:
        #change font color red becouse you have problem
        color("color 04")
        print("Sorry, you don't have enough assets to repay this loan. So it is difficult to give you loan.")
        print("Because the percentage you got for getting the loan successfully:", ATP, "%")
        #wait 1 second
        time.sleep(1)
        #change font color to green
        color("color 01")
    print('Thank you very much for dealing with BIT BUSTERS SOLUTIONS...')
    time.sleep(2)
    code_end()

def withdraw():
  while True:
    tot = 0
    # Input validation for NIC
    while True:
        nic = input('Enter your National Identity Number (12 digits): ')
        if nic.isdigit() and len(nic) == 12:
            break
        else:
            print('Invalid NIC. Please enter a 12-digit numeric NIC.')

    M = input("Enter the amount of money: ")
    M='-'+M
    
    # Append transaction data to D_Money.txt
    with open("D_Money.txt", "a") as f1:
        f1.write(nic + "," + M + "\n")

    # Calculate total money for the user
    with open("D_Money.txt", "r") as f2:
        for line1 in f2:
            L1 = line1.strip().split(",")
            if L1[0] == nic:
                tot += int(L1[1])

    print("Your total stored value:", tot)

    z = input("Do you want to perform another operation? (y/n): ")
    if z.lower() != 'y':
        break

def deposit():
  while True:
    tot = 0

    # Input validation for NIC
    while True:
        nic = input('Enter your National Identity Number (12 digits): ')
        if nic.isdigit() and len(nic) == 12:
            break
        else:
            print('Invalid NIC. Please enter a 12-digit numeric NIC.')

    M = input("Enter the amount of money: ")
    
    # Append transaction data to D_Money.txt
    with open("D_Money.txt", "a") as f1:
        f1.write(nic + "," + M + "\n")

    # Calculate total money for the user
    with open("D_Money.txt", "r") as f2:
        for line1 in f2:
            L1 = line1.strip().split(",")
            if L1[0] == nic:
                tot += int(L1[1])

    print("Your total stored value:", tot)

    z = input("Do you want to perform another operation? (y/n): ")
    if z.lower() != 'y':
        break
    
# Loading animation call
loading()

# Changing colors :)
color("color 01")
time.sleep(0.2)
color("color 02")
time.sleep(0.2)
color("color 03")
time.sleep(0.2)
color("color 04")
time.sleep(0.2)
color("color 05")
time.sleep(0.2)
color("color 06")
time.sleep(0.2)
color("color 07")
time.sleep(0.2)
color("color 08")
time.sleep(0.2)
color("color 02")

#show details about our application
print("            $$    WELLCOME TO BIT BUSTERS BANK    $$            \n")
print('Select the service you want from us.\n')
print('     Press number -> 1 for loan details.\n')
print('     Press number -> 2 for deposit money.\n')
print('     Press number -> 3 for withdraw money.\n')
print("In loan details you can check Probability of being able to take a loan.")

#getting inputs
while True:
    x = int(input("-> "))
    if x == 1:
        # call loan calculation func
        loan_cal()
    elif x == 2:
        deposit()
    elif x == 3:
        withdraw()
    else:
        print("Please enter a number (1/2/3)")
        c_false()
