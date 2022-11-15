#!/bin/python3

import math
import os
import random
import re
import sys

def actions(n):
    if (n%2 == 0):
        if (2<=n <= 5 ):
            print('Not Weird')
        elif (5<=n<=20 ):
            print('Weird')
        elif (20<=n<=100):
            print('Not Weird')
        else: 
            print('Enter the number between 1 to 100')
        
    else :
        print('Weird') 
            

if __name__ == '__main__':
    n = int(input().strip())
    actions(n)
