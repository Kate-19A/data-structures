print ("Hello. Welcome to data structures class !!!")

number1 = 10
print(f"Var number1 is: {type(number1)}")
gravity = 9.8
print(f"Var gravity is: {type(gravity)}")
numberx = 8j
print(f"Var numberx is: {type(numberx)}")

#String Data Types

'''
This is a scope comment
'''

my_name = "Tatiana"
full_name = "Tatiana Yaqueline"
description = '''
Hello, how's it going?
This is amazing !!!
'''
print(f"Var my_name is: {type(my_name)}")
print(f"Var full_name is: {type(full_name)}")
print(f"Var description is: {type(description)}")

week_days = []
print(f"Var week_days is: {type(week_days)}")

fruits = []
print(f"Var fruits is: {type(fruits)}")

months = ()
print(f"Var months is: {type(months)}")

#Lists
personal_info = ['Kate', 
                'Barrera', 
                18, 
                True, 
                '3182755944', 
                'Pasto',
                ['Angela', 17]
]
print(personal_info)
#Show Kate age and city
print(f"Kate age: {personal_info[2]}")
print(f"Kate city: ", personal_info[5])
#Show Angela name and age
print(f"Angela name: {personal_info[6][0]}")
print(f"Angela age: ", personal_info[6][1])
#update Kate age
#new_age = input("Please, type the new Kate age: ")
personal_info[2] = new_age
print (f"New Kate age id: {personal_info[2]}")
#Add new information
personal_info.append('Malala')
print(personal_info)

#Tuple
user_data = ('Benazir', 'Butto', 35)
print(user_data)
print(user_data[0])
new_age = 40
#user_data[2] = new_age

#Dictionaries
countries_info = {
    'country_name' : 'Colombia',
    'Capital' : 'Bogotá'
    'Abbrev' : 'CO',
    "Code" : 123456
}
print(countries_info[country_name])