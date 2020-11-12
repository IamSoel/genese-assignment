def convert_f_to_c(f):
    c=(f-32)*5/9 # now it is converted into celcius
    print(f'{f}°F = {c:.3f}°C')

def time_converter(second):
    m=second//60
    sec=second%60
    print(f'{second} seconds is {m} minutes {sec} seconds')


def list_info(elements):
    print('The length of list is',len(elements))
    print('The first element of list is',elements[0])
    print('The fourth element of list is',elements[3])


def list_operations(elements):

    elements.pop() #removes the last element of the list
    print('Pop operation')
    print(elements)
    elements.insert(0,1) # adds the element in the list in the given index, in this case it add 1 to first index i.e 0
    print('\n Insert operation')   
    print(elements)
    elements.remove(elements[1]) # removes the provided element if it is present in the list
    print('\n Remove operation')    
    print(elements)

def main():
    while(1):
        print('1. Convert Farenheit to Celcius.')
        print('2. Convert Seconds into minutes and seconds')
        print('3. Display the length, first value and fourth value of the list')
        print('4. Perform various list operations')
        print('5. Exit')
        num=int(input('Enter a choice: '))
        if num==1:
            farenheit=float(input('Enter temperature in farenheit: '))
            convert_f_to_c(farenheit)
        elif num==2:    
            time=float(input('Enter time in second: '))
            time_converter(time)
        elif num==3:
            num_list=[]
            n=int(input('Enter number of elements for the list: '))  
            for i in range(n):
                list_input=int(input())  
                num_list.append(list_input)
            list_info(num_list)
        elif num==4:
            num_list=[]
            n=int(input('Enter number of elements for the list: '))  
            for i in range(n):
                list_input=int(input())  
                num_list.append(list_input)
            list_operations(num_list)
        elif num==5:
            break
        else:
            print('Wrong Choice')    

if __name__ == "__main__":
    main()