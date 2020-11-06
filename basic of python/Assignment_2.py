# Assignment 2

'''
1. Choose a list of your choice and find the sum of all elements of that list. For example, the
sum of [6,9,7,5,4] is 31.
Note: You cannot use sum () function here
'''
num_list=[10,20,30,40]
total=0
for i in num_list:
    total=total+i
print('The sum of numbers of list is',total)


'''
2. Write a program that returns a list which contains common elements from two lists. Avoid
the duplicate elements from lists.
For example
a = [1, 1, 3, 5, 7, 9, 9]
b = [2, 1, 6 ,9, 2, 1, 3, 5]
The result should be [1, 3, 5, 9]
Note: You cannot use if-else statement here.
'''
a = [1, 1, 3, 5, 7, 9, 9]
b = [2, 1, 6 ,9, 2, 1, 3, 5]
c=list(set(a).intersection(set(b)))
print('\nThe common elements in both a and b are',c)


'''
3. Suppose you have a list [1, 5, 7, 12 ,15]
Print each number using loop. Also, print the square of each number using loop.
'''
new_list=[1,5,7,12,15]
for num in new_list:
    print(f'The number is {num} and its square is {num*num}')


'''
4. Write a code to ask an input from the user which is a string and display the string along
with its length.
Note: You cannot use len () function here.
'''
input_str=str(input('\nEnter a string '))
length=0
for n in input_str:
    length=length+1
print('The length of {} is {}'.format(input_str,length))    


'''
5. Write a code to ask an input from the user which is a string and convert it to uppercase
and lowercase.
'''
input_str=str(input('\nEnter a string '))
print(f'The upper case of {input_str} is {input_str.upper()} and lower case is {input_str.lower()}')