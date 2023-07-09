#!/usr/bin/env python3

def print_fibonacci(length):
       my_list=[]
       first = 0
       second = 1
       tmp = 0
       for i in range(length):
        if i in {0,1}: 
           my_list.append(i)
        else:
            my_list.append( first + second) 
            tmp=second
            second=first + second
            first=tmp
            
       print(my_list)  