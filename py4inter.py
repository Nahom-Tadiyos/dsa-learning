#Variables are dynamically typed
n = 0

#Multiple assigments
n, m = 0, "abc"

#Incrment
n = n + 1
n += 1

#None is null
n = 4
n = None
#If statments dont need parenthess
n = 1
if n > 2:
    n -= 1
elif n == 2:
    n *= 2

#parentheses needed for multi line conditions
# and = &&
# or = ||
n, m = 1, 2
if ((n>2 and n != m) or n == m):
    n += 1

#While loops
n = 0
while n < 5:
    print(n)
    n += 1

#Division is decimal by default
print(5/2)

#Double slash rounds doqwn
print(5//2)

#use decimal division then convert to int
print(int(-3/2))

#Modding 
print(10%3)
