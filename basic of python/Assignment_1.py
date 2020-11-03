# Exercise 1
print('Exercise 1')
width=17
height=12.0
delimeter='.'
print(f'1. width/2 = {width/2} and type is {type(width/2)} ')
print(f'2. width/2.0 = {width/2.0} and type is {type(width/2.0)} ')
print(f'3. height/3 = {height/3} and type is {type(height/3)} ')
print(f'4. 1+2*5 = {1+2*5} and type is {type(1+2*5)}')
print(f'5. delimiter*5 = {delimeter*5} and type is {type(delimeter*5)}')


# Exercise 2
print('\nExercise 2')
f=104 # this value is in fahrenheit
c=(f-32)*5/9 # now it is converted into celcius
print(f'{f}°F = {c}°C')


# Excercise 3
print('\nExercise 3')
s=150 # this value is in seconds
m=s//60
sec=s%60
print(f'{s} seconds is {m} minutes {sec} seconds')


# Excercise 4
print('\nExercise 4')
elements=[10,20,30,40,50,7,2,12]
print('The length of list is',len(elements))
print('The first element of list is',elements[0])
print('The fourth element of list is',elements[3])


# Excercise 5
print('\nExercise 5')
elements=[10,20,30,40,50,7,2,12]
elements.pop() #removes the last element of the list
print(elements)
elements.insert(0,1) # adds the element in the list in the given index, in this case it add 1 to first index i.e 0
print(elements)
elements.remove(10) # removes the provided element if it is present in the list
print(elements)
