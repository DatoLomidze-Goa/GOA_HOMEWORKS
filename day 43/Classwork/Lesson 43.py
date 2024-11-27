#Codewars

#1: Write a function that accepts an integer n and a string s as parameters, and returns a string of s repeated exactly n times.

#Examples (input -> output)
#6, "I"     -> "IIIIII"
#5, "Hello" -> "HelloHelloHelloHelloHello"


#def repeat_str(repeat, string):
    #return repeat * string

#2: Given an array of integers your solution should find the smallest integer.

#For example:

#Given [34, 15, 88, 2] your solution will return 2
#Given [34, -345, -1, 100] your solution will return -345
#You can assume, for the purpose of this kata, that the supplied array will not be empty.

#def find_smallest_int(arr):
    #return min(arr)


#3: Complete the square sum function so that it squares each number passed into it and then sums the results together.

#For example, for [1, 2, 2] it should return 9 because 

#def square_sum(numbers):
   #return sum(x ** 2 for x in numbers)