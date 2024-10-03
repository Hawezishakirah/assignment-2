#WITI Academy is processing a Sacco to help students save their money.
#Design a platform that will do the following.
#Welcome to, WITI Academy Sacco.
#1.Desposit Money.
#2.Withdraw Money
#3.Check Balance
#Ensure if the student selects 1, money is deposited and the minimum deposit should be 1000
#If the student selects 2, money should be withdrawn and a minimum withdrawal is 500
#If the student selects 3, the account balance should be displayed

# answers
def sacco_transactions():

    account_balance = 0
    run = 1

    while run == 1:
        print("\nWelcome to, WITI Academy Sacco")

        #menu
        print('1.Deposit Money')
        print('2.Withdraw Money')
        print('3.Check Balance')

        student_choice = int(input("Enter your selection(1,2,3):"))

        #performingthe transactions basing on the selection

    if student_choice ==1:
            print('n\...Processing a deposit yransaction...')
            deposit_amount = int(input( "Enter the amount to be deposited"))

            #check if deposit amount is less than 1000
            if deposit_amount< 1000:
                 
    
                print('\nMinimum deposit is 1000')

            else:
                account_balance += deposit_amount

            print(f'Dear student, you have deposited {deposit_amount,}and your new account balance is{account_balance:,}')

    elif student_choice == 2:
           print('\n...Processing a withdraw transaction...')
           withdraw_amount =int(input("Enter amount to be withdrawn"))

           if account_balance ==0:
              print("Your balance is 0")

    elif withdraw_amount<500:

            print("Minimum withdraw amount is 500")
    elif withdraw_amount > account_balance:
         
         print(f"Withdraw failed, insurficient funds")
    else :
         account_balance-= withdraw_amount 
         print(f"Dear student, you have withdrawn{withdraw_amount:,} and your new account is{account_balance:,}")
         print(f"Your account balance is{account_balance:,}")

