import os
from datetime import date

#functions
def mainMenu():
    print (":::Main menu:::")
    print ("[1]Register a new user")
    print ("[2]List all users")
    print ("[3]Search user")
    print ("[4]Delete user")
    print ("[5]Update user")
    print ("[6]Show active uses")
    print ("[7]Show inactive users")
    print ("[8]Exit")


ids=[]    
firtsnames=[]
lastnames=[]
mobile_phones=[]
emails=[]
statuses=[]
genders=[]

ages=[]
salarys=[]

created_at=[]
#Main


while True:
    os.system('clear')
    mainMenu()
    opt=input("Press any option [1-8]: ")

    match opt:
        case '1':
            os.system('clear')
            print("::: Register form :::")

            while True:
                id=input("identification number: ")
                count = 0
                i=0
                while i< len(ids):
                    if id == ids[i]:
                        print("identification number already exists! \n Try Again:::")
                        count+=1
                        break
                    i+=1
                if count==0:
                    break


            firtsname=input("Firstname: ")
            lastname=input("Lastname: ")
            mobile_phone=input("Mobile Phone: ")
            email=input("E-mail: ")
            gender=input("Gender [M/F/O]: ")

            age=input("age: ")
            salary=input("salary: ")


            ids.append(id)
            firtsnames.append(firtsname)
            lastnames.append(lastname)
            mobile_phones.append(mobile_phone)
            emails.append(email)
            statuses.append(True)
            genders.append(gender)

            ages.append(age)
            salarys.append(salary)


            created_at.append(date.today())
            print("User has been created successfully !!")
            any_key = input ("Press any key to back to main menu")



        case '2':
            while True:
                os.system('clear')
                print(":::List all registered users:::")
                print("[1] Sort in ascending order by identification")
                print("[2] Sort in descending order by identification")
                print("[3] Sort in ascending order by lastname")
                print("[4] Sort in descending order by lastname")
                print("[5] Exit")
                sub_opt = input("Select an option [1-5]: ")

                if sub_opt == '5':
                    break

                if len(ids) == 0:
                    any_key = input("No registered users found! Press any key to back...")
                    break

                indices = list(range(len(ids)))

                if sub_opt == '1':
                    indices.sort(key=lambda x: ids[x])
                elif sub_opt == '2':
                    indices.sort(key=lambda x: ids[x], reverse=True)
                elif sub_opt == '3':
                    indices.sort(key=lambda x: lastnames[x])
                elif sub_opt == '4':
                    indices.sort(key=lambda x: lastnames[x], reverse=True)
                else:
                    any_key = input("Invalid option. Press any key to try again...")
                    continue

                os.system('clear')
                print(":::List all registered users:::")

                print ('-'*163)
                print (f"| {'id':<15} | {'Firsname':<15} | {'Lastname':<15} | {'Mobile Phone':<15} | {'Emails':<15} | {'Genders':<15} | {'Ages':<15} | {'Salarys':<15} | {'Created':<15} |")
                print ('-'*163)

                i=0
                while i < len(indices):
                    idx = indices[i]
                    print(f'| {ids[idx]:<15} | {firtsnames[idx]:<15} | {lastnames[idx]:<15} | {mobile_phones[idx]:<15} | {emails[idx]:<15} | {genders[idx]:<15} |  {ages[idx]:<15}| {salarys[idx]:<15} | {created_at[idx]}      |')
                    print ('-'*163)
                    i += 1

                any_key = input ("Press any key to back to list menu")

            #print(f"IDs: {ids}")
            #print(f"Firsnames: {firtsname}")
            #print(f"Lasnames: {lastname}")
            #print(f"Mobile Phones: {mobile_phone}")
            #print(f"Emails: {email}")
            #print(f"Genders: {gender}")
            #print(f"Created_at: {created_at}")

            any_key = input ("Press any key to back to main menu")



        case '8': 
            any_key=input("bye bye. press any key... ")
            break
        case _ :
            any_key=input("Invalid option. press any key to try again")