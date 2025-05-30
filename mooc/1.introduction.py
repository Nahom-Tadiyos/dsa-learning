#Find the max difference:
import random
import time

def max_diff(numbers):
    return max(numbers) - min(numbers)

n = 1000
print("n: ", n)
random.seed(1337)
numbers = [random.randint(1, 10**6) for i in range(n)]

start_time = time.time()
result = max_diff(numbers)
end_time = time.time()

print("result: ", result)
print("time:", round(end_time - start_time, 2), "s")


#Constant Time - if the algorigthm has no loops and executes the same steps independent of the input, it is O(1)
def middle(numbers):
    n = len(numbers)
    return numbers[n//2]

#Single Loop - if the algorithm cotains a single loop that goes through all elements of the input, it is O(n)
def calc_sum(numbers):
    result = 0
    for x in numbers:
        result += x
    print(result)

calc_sum([1, 2, 3])

#Nested loops - if the algorithm cotains a loop inside a loop, each of which goes through all elements of the input, it is O(n^2)
def has_sum(numbers, x):
    for a in numbers:
        for b in numbers:
            if a + b == x:
                return True
    return False

#Sequential code segments - if the algorithm consists of multiple code segments in sequence, the time complexity is the maximum of the segment time complexities
def count_min(numbers):
    #stage 1
    min_value = numbers[0]
    for x in numbers:
        if x < min_value:
            min_value = x
    
    #stage 2
    result = 0
    for x in numbers:
        if x == min_value:
            result += 1
    
    return result