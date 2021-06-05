from Classes import user

def locker():

    var User1 = user("Dejan", "password")
    
    choice = input("Type 'login' to Login: ")
    choice = choice.lower()
    
    if choice == "login":

        # login 
        var userNameInput = str(input("Enter user name: "))
        var passwordInput = str(input("Enter password: "))

        if userNameInput == User1.userName and passwordInput == User1.password:
            

        else:
            print("UserName or Password is incorrect")

    else:
        


