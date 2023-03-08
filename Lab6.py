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
