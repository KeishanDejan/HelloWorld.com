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
            view_files = str(input("If you want to view files type 'view files'"))
            

        else:
            print("UserName or Password is incorrect")

    else:
        


