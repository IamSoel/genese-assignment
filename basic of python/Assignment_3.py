#1. Write a program to display all prime numbers from 1 to 100.
for num in range(1,101):
    if num>1:
        for i in range(2,num):
            if num % i==0:
                break
        else:
            print(num)
    

#2. Ask the user for a string and print out whether this string is a palindrome or not.
#(A palindrome is a string that reads the same forwards and backwards.)
string=input('Enter a String. ')
new_str=string[::-1]
if string==new_str:
    print('{} is a palindrome string.'.format(string))
else:
    print('{} is not a palindrome string.'.format(string))


#3. Given a string, count all lower case, upper case, digits and special symbols.
string=input('Enter a string. ')
lower=0
upper=0
digit=0
symbols=0
for s in string:
    if s.islower():
        lower=lower+1
    if s.isupper():
        upper=upper+1
    if s.isdigit():
        digit+=1
    if not s.isalnum():
        symbols+=1

print(f'The number of lower case is {lower}. \nThe number of uppercase is {upper}. \nThe number of digits is {digit}. \nThe number of special symbols is {symbols}.')


#4. Write a program to display the n terms of harmonic series and their sum.
#1 + 1/2 + 1/3 + 1/4 + 1/5 ... 1/n
number=int(input('Enter a number. '))
sum=0
series=' 1 '

for i in range(1,number+1):
    if i!=1:
        series=series+ ' + ' +'1'+'/'+str(i)
    
    sum=sum+(1/i)
print(series)
print(f'The sum of the harmonic series is {sum:.3f}')


#5. Write a program to display the following pattern. Check also with different number of
#rows.
#     *
#    **
#   ***
#  ****
# *****
number=int(input('Enter a number.'))
for i in range(1,number+1):
    print(end=' '*(number-i))
    print('*'*i)


# 6. Create a dictionary that has a key value pair of letters and the number of occurrences of
# that letter in a string.
# Given a string “pineapple”. The result should be as:
# {“p”:3, “i”:1, “n”:1, “e”:2, “a”:1, “l”:1}
# Don’t worry about the order of occurrence of letters.
string=input('Enter a String.')
letter_count={}
for i in string:
    count=0
    for j in range(len(string)):
        if i==string[j]:
            count+=1
    letter_count[i]=count      

print(letter_count)