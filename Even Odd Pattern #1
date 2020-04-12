#Write a function that takes an array/list of numbers and returns a number.

#See the examples and try to guess the pattern:

#even_odd([1,2,6,1,6,3,1,9,6]) => 393
#even_odd([1,2,3]) => 5
#even_odd([0,2,3]) => 3
#even_odd([1,0,3]) => 3
#even_odd([3,2])   => 6


# My solution
def even_odd(arr):
    c = arr[0]
    for i in range(1, len(arr)):
        if i % 2 == 0:
            c += arr[i]
        else:
            c *= arr[i]
    return c
