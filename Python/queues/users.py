import os

#functions
def mainMenu():
    print(":::Main menu:::")
    print("[1]. Register a new user")
    print("[2]. List all users")
    print("[3]. Search user")
    print("[4]. Delete user")
    print("[5]. Update user")
    print("[6]. Show active users")
    print("[7]. Show inactive users")
    print("[8]. Exit")

#Main
while True:
    os.system('Clear')
    mainMenu()
    opt = input('Press any option: ')

match opt:
    case '1':
        os.system('clear')
        print(":::Register user form:::")
        id = input("Ident. number: ")
        firstname = input("Firstname: ")
        lastname = input("Lastname: ")
        mobile_phone = input("Mobile phone: ")
        email = input("Email: ")
        gender = input("Gender [M/F/O]: ")

        ids.append(id)
        firstnames.append(firstname)
        lastnames.append(lastname)
        mobile_phones.append(mobile_phone)
        emails.append(email)
        statuses.append('True')
        genders.append(gender)
        created_at.append(date.today())
        print("User has been created successfully!")
        any_key = input("Press any key to buck to Main Menu")

    case '2':
        print ("List all registered users...")
        
        print ()