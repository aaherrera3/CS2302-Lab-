# Lab 8
# Programmed by Anthony Herrera
# Last modified May 9, 2019
import random
import mpmath as mp
from math import *

def equal(F):                                           #Using a nested loop to test each equation with it self and the others
    results = []                                        # Then is saves the results in a List of List
    t = random.randint(int(-pi),int(pi))
    print('t=',t)
    for f in range(len(F)):
        for y in range(len(F)):
            y1 = eval(F[f])
            y2 = eval(F[y])
            if y1 == y2:
                results.append([F[f], F[y], True])
            else:
                results.append([F[f], F[y], False])
    return results
            # print(F[f],F[y])
            # print(y1,y2)

def FindPartion(L,i):           #Test the list to make sure its possible to have two subsets equal to one another (Even sum)
    sum = 0                     # Then calls method to split the list
    for x in range(0,i):
        sum += L[x]

    if sum % 2 != 0:
        return False, None
    return SubsetSum(L)


def SubsetSum(L):               #Creates two sets to store the values of L the List
    A = set()                   #Using a for loop we check the sum of both sets and add the value from the list into the corresponding set
    B = set()
    for n in L:
        if sum(A) < sum(B):
            A.add(n)
        else:
            B.add(n)
    return A,B

#List of functions
F = ['sin(t)','cos(t)','tan(t)','mp.sec(t)','-sin(t)','-cos(t)','-tan(t)','sin(-t)','cos(-t)','tan(-t)','sin(t)/cos(t)','2*sin(t/2)','sin(t)*sin(t)','1-cos(t)*cos(t)','(1-cos(t))/2','1/cos(t)']

results = equal(F)

for x in results:
    print(x)


List = [3, 1, 5, 9, 12] # List for subset sum
length = len(List)
print(List)

print(FindPartion(List, length))
