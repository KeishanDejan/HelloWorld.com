from Classes import user

def locker():

    User1 = user("Dejan", "password")
    
    choice = input("Type 'login' to Login: ")
    choice = choice.lower()

    players = open("players.txt", "r")
    students = open("students.txt", "r")

    files = ["players.txt", "students.txt"]
    
    if choice == "login":

        # login 
        userNameInput = str(input("Enter user name: "))
        passwordInput = str(input("Enter password: "))

        if userNameInput == User1.userName and passwordInput == User1.password:

            while True:

                view_files = str(input("If you want to view files type 'view files' If you want to leave type 'stop': "))
                view_files = view_files.lower()

                if view_files == "view files":

                    print(files)
                    wanted_files = str(input("Which files is want to view: "))
                    wanted_files = wanted_files.lower()

                    if wanted_files == "players.txt":
                        print(players.readlines())
                    elif wanted_files == "students.txt":
                        print(students.readlines())
                    else:
                        print("Check your spelling")

                elif view_files == "stop":

                    break

                else:
                    print("Check your spelling")

                
        else:
            print("UserName or Password is incorrect")

    else:
        print("Check your spelling")

try:
    print(locker())

except ValueError as err:
    print(err)

else:
    print("Nothing went wrong")