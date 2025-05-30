a = [1, 2, 3]
print(a)

#Append - Insert element at end of array - On average: O(1)
a.append(5)
# print(a)

#Pop - deleting element at end of array - O(1)
a.pop()
print(a)

#Insert (not at end of array) - O(n)
a.insert(2,5)
print(a)

#Modify an element - O(1)
a[0] = 7
print(a)

#ccesing element given index i - O(1)
print(a[2])

##Strings
#Append to end of string O(n)
s = 'hello'

b = s + "z"
print(b)

#Check if something is in string - O(n)
if 'f' in s:
    print(True)

#Accesing positions
print(s[2]) 

#Reordering an integer in desecnging order
def reorder_integer(n):
    newN = []
    for I in str(n):
        newN.append(I)
        newN.sort(reverse=True)
    
    n = ''.join(map(str, newN))
    print(int(n))


reorder_integer(34327)

def factorial(n):
    if n == 0:  # Base case: factorial of 0 is 1
        return 1
    else:
        return n * factorial(n - 1)  # Recursive case