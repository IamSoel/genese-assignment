def sum_of_list(num_list):
    total=0
    for i in num_list:
        total=total+i
    print('The sum of numbers of list is',total)

def common_elements():
    a = [1, 1, 3, 5, 7, 9, 9]
    b = [2, 1, 6 ,9, 2, 1, 3, 5]
    c=list(set(a).intersection(set(b)))
    print('\nThe common elements in both a and b are',c)

def string_length():
    input_str=str(input('\nEnter a string '))
    length=0
    for n in input_str:
        length=length+1
    print('The length of {} is {}'.format(input_str,length)) 

def main():
    while (1):
        print('1. Print the sum of elements of the list')
        print('2. Print the common elements of two list.')
        print('3. Print the length of the string')
        print('4. Exit')
        num=int(input('Enter a choice: '))
        if num==1:
            num_list=[]
            n=int(input('Enter number of elements for the list'))  
            for i in range(n):
                list_input=int(input())  
                num_list.append(list_input)            
            
            sum_of_list(num_list)
        
        elif num==2:
            common_elements()

        elif num==3:
            string_length()  

        elif num==4:
            break

        else:
            print('*** Invalid Choice ***')          



if __name__=='__main__':
    main()