numbers = [4, 2, 1, 2]
numbers.sort()
print(numbers)

#The time complexity of both the method sort and the function sorted is O(n log n)
#Smallest Difference
def min_diff(numbers):
    numbers = sorted(numbers) #Used sorted() instead of sort() becayse it will affect the list outside the function

    result = numbers[1] - numbers[0]
    for i in range(2, len(numbers)):
        result = min(result, numbers[i] - numbers[i-1])
    
    return result

#Hashing vs Sorting
def count_distinct(numbers): #-- Hashing
    seen = set()
    
    for x in numbers:
        seen.add(x)
    
    return len(seen)

def count_distinct(numbers):
    numbers = sorted(numbers)
   
    result = 1
    for i in range(1, len(numbers)):
        if numbers[i] != numbers[i - 1]:
            result += 1

    return result

#Sorting into reverse order
numbers = [2, 4, 3, 5, 6, 1, 8, 7]
numbers.sort(reverse=True)
print(numbers) # [8, 7, 6, 5, 4, 3, 2, 1]

#Multipart elements
pairs = [(3, 5), (1, 3), (1, 2), (2, 4)]
pairs.sort()
print(pairs) # [(1, 2), (1, 3), (2, 4), (3, 5)]

#Element comparisons
numbers = [4, -1, 6, 2, -7, 8, 3, -5]
numbers.sort(key=abs)
print(numbers) # [-1, 2, 3, 4, -5, 6, -7, 8]

