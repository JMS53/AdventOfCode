#! /usr/bin python3
import math

def isPrime(num):
    """
    Runs a quick test to verify if a number is prime, returns 1 if num is
    prime. 0 otherwise
    """	
    if num <= 1:
        return 0
    if (num == 2) or (num == 3):
	    return 1
    if ((num +1) % 6 != 0) and ((num -1) % 6 != 0):
	    return 0
    lim = math.ceil(math.sqrt(num)) + 1
    for i in range(2,lim):
        if num % i == 0:
            return 0
    return 1

def isPalindrome(num):
    num = str(num)
    if num == num[::-1]:
        return 1
    return 0

def funct(a,b):
	n = 0
	counter = 0
	while (isPrime(n**2 + a*n + b)):
		n += 1
		counter += 1
	return counter

def day27():
	# define num of primes to test against
	primes = []
	for b in range(1001):
		if isPrime(b):
			primes.append(b)
	
	maxP = 0
	prod = 0
	for a in range(-1000,1001):
	    for b in primes:
	        c = funct(a,b)
	        if c > maxP:
	            maxP = c
	            prod = a*b
	            print(a,b,prod)

def translate(num):
	# takes a number and returns a rotation. i.e. 123 -> 231, 231 -> 312
	num = str(num)
	k = num[0]
	num.pop(0)
	num.append(k)
	return int(num)

def problem30():
	a = 0
	circular = {}
	while a < 1000000:
		if isPrime(a):
			print(a)
			if len(str(a)) == 1:
				circular[a] = 1
				#single digit numbers are circular
			
			#Convert number into string and test rotations
			
				
			
		
		a += 1 

def problem31():
    #check if a number in dec is palindrome
    #convert to binary and repeat check
    s=0
    for i in range(1000000):
        if isPalindrome(i):
            j = str(bin(i))[2:] #binary repr starts as 0bxxyy
            if isPalindrome(j):
                s+= i
    print(s)


# Problem 37
# Truncate left & right functions

def trunc(num, dir=0):
    # takes a number, converts to string
    # if dir = 0: returns num[1:]
    # if dir = 1: returns num[:-1]
    k = str(num)
    if len(k) == 1:
        return k
    if dir == 0:
        return k[1:]
    return k[:-1]

def testP(num):
    k = num
    print(k)
    if (isPrime(k) == False):
        return 0
    if (k > 9):
        j = int(trunc(k))
        i = int(trunc(k, 1))
        return testP(i) and testP(j)
    return isPrime(num)

print(testP(3797))

def problem37():
    primes = []
    for i in range(10,1000):
        # check if the number is prime, then trunctate until false 
        if isPrime(i):
            print(testP(i))
    
#problem37()
