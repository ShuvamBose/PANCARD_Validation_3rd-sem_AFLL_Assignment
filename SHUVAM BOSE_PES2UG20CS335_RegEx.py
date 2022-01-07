import string

def D():        #s0 is the Dead state
    print("\nDo you want to cont ?: ")
    aa=input()
    if aa == "Yes" :
        my_main()
    else :
        exit()

def s2(x2):     #s0 is the 3rd transition state
    if x2[9] not in list(string.ascii_uppercase) : #to check if in uppercase list
        print("\nInvalid End chars. !")
        D() #calling Dead State
        
    print("\nCongrats Successfully verified !")

def s1(x1):     #s0 is the 2nd transition state
    
    for i in range(5,9): #to check if there are 4 integers
            if x1[i] not in ['0','1','2','3','4','5','6','7','8','9']:
               print("\nInvalid INT Part!\n")
               D() #calling Dead State
               
    s2(x1)
          
def s0(x0):     #s0 is the first transition state
    i=0
    for i in range(0,5):
            
            if x0[i] not in list(string.ascii_uppercase) : #to check if in uppercase list
                print("\nInvalid Initial chars. !")
                D() #calling Dead State
                
    s1(x0)

def my_validator(n):
    if(len(n)==10):
        s0(n)
    else:
        print("\nEntered PAN expression isn't of correct length !")
        my_main()

def my_main():
    print("\nEnter the PAN Card expression to validate: ")
    a=input()   #takes input
    my_validator(a)
    
my_main()  #main func called..