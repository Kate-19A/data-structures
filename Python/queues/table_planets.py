planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
gravity = [3.7, 8.8, 9.8, 3.7, 24.7, 10.4, 8.6, 11.1]

#print (type(gravity)) #class List
print (planets)
print (len(planets)) #8 rows ->Elements

print ('-'*31)
print (f"| {'planet name':<15} | {'Gravity':<9} |")
print ('-'*31)
i=0
while i<len(planets):
    print(f'| {planets[i]:<15} | {gravity[i]:<9} |')
    print('-'*39)
    i+=1