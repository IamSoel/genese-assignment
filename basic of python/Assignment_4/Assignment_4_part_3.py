def prime_number():
    for num in range(1,101):
        if num>1:
            for i in range(2,num):
                if num % i==0:
                    break
            else:
                print(num)

def palindrome_checker():
    string=input('Enter a String. ')
    new_str=string[::-1]
    if string==new_str:
        print('{} is a palindrome string.'.format(string))
    else:
        print('{} is not a palindrome string.'.format(string))


def character_counter():
    string=input('Enter a String.')
    letter_count={}
    for i in string:
        count=0
        for j in range(len(string)):
            if i==string[j]:
                count+=1
        letter_count[i]=count      

    print(letter_count)


def main():
    while (1):
        print('1. Print the prime numbers from 1 to number')
        print('2. Check palindrome or not.')
        print('3. count the number of character in string')
        print('4. Exit')
        num=int(input('Enter a choice: '))
        if num==1:
            prime_number()
       
        elif num==2:
            palindrome_checker()
       
        elif num==3:
            character_counter()            
       
        elif num==4:
            break

        else:
            print('*** Invalid Choice ***') 

if __name__=='__main__':
    main()