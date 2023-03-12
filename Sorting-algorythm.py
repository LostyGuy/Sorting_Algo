import random
import time as t
import os

arr = [2,6,5,8,9,1,3]
marr = [4,3,2,6,5,9,8,7,1]

# len and range definition

def buuble_sort():
    x = []
    c = 0

    for i in range(0,30):
        r = random.randint(1,100) 
#this function allows me to have basic random number generator
        x.append(r)
#function "append" add to variable 'x' value of 'r'
        c = c + 1
        if c == 30:
            print(x)
    list = len(x)

    for i in range(list):
        already_sorted = True
        for j in range(list - i - 1):
            if x[j] > x[j + 1]:
                x[j], x[j + 1] = x[j + 1], x[j]
                already_sorted = False
        if already_sorted:
            break
    
    print(x)

def insertion_sort(arr):

    for i in range(1, len(arr)):
        j = i
        while arr[j - 1] > arr[j] and j > 0:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1

    print(arr)

def imerge_sort(marr):
  
    i = 0
    j = 0
    k = 0

    if len(marr) > 1:
        left_arr = marr[:len(marr)//2]
        right_arr = marr[len(marr)//2:]
        imerge_sort(left_arr)
        imerge_sort(right_arr)

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                marr[k] = left_arr[i]
                i += 1
            else:
                marr[k] = right_arr[j]
                j += 1
            k += 1
    
        while i < len(left_arr):
            marr[k] = left_arr[i]
            i += 1
            k += 1
    
        while j < len(right_arr):
            marr[k] = right_arr[j]
            j += 1
            k += 1

        print(marr)
        
def conti():
  
    print("\nWould you want to contunue?")
    con = input('\nType "Yes" or "No"\n').lower()
    if con == 'yes':
        os.system('cls')
        menu()
    elif con == 'no':
        print('See you later')
        exit()
    else:
        conti()
               
def menu():
    print("HI")
    print('Select option: ')
    print('1. Bubble Sorting \n2. Insertion Sorting \n3. Merge Sorting \n4. Exit')
    user = input()
    
    if user == '1':
        buuble_sort()
        t.sleep(2)
        conti()
    elif user == '2':
        insertion_sort(arr)
        t.sleep(2)
        conti()
    elif user == '3':
        imerge_sort(marr)
        t.sleep(2)
        conti()
    elif user == '4':
        exit()
    else:
        menu()    
  
menu()

# nie wiem
