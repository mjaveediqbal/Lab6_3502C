'''
UF online Spring 2023 Programming Fundamentals 1 (10811)
3/6/2023
Javeed Iqbal,Muhammad Jawwad
Lab 6
'''

#Muhammad Jawwad Javeed Iqbal
#Iterates through string password and stores the value in new_password
def encode(password):
    new_password=""
    for i in range(0,len(password)):
        x=int(password[i:i+1])
        x+=3
        #Checks if x>=7 and if so, loops it back to 0.
        if x>=7:
            x=x%10

        #stores value of x
        new_password=new_password+str(x)

    return new_password

#Prints menu options
def menu_print():
    print(
'''
Menu
-------------
1. Encode
2. Decode
3. Quit

'''
)

#Main function
def main():
    new_password=0
    menu_option=1
    #Exits function when user specifies a value greater than or equal to 3 or less than or equal to 0
    while menu_option<=2 and menu_option>0:
        menu_print()

        menu_option=int(input("Please enter an option: "))

        if menu_option==1:
            #Stores encoded password 
            password=input("Please enter your password to encode: ")
            new_password=encode(password)
            print("Your password has been encoded and stored!")
        #Checks if there was a encoded password, and if so, prints out encoded password and decoded password
        if menu_option==2:
            if new_password==0:
                print("No password has been encoded yet")
            else:
                print(f"The encoded password is {new_password}, and the original password is .")#add decode function

if __name__=='__main__':
    main()