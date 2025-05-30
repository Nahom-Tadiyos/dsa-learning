#Indexing - elements can be accesed and modifed using []
numbers = [4, 3, 7, 3, 2]
print(numbers[2]) # 7
numbers[2] = 5
print(numbers[2]) # 5

#List size - use len to tell how many elemnents in the list
numbers = [4, 3, 7, 3, 2]
print(len(numbers)) # 5

#Searching
numbers = [4, 3, 7, 3, 2]

print(3 in numbers) # True
print(8 in numbers) # False

print(numbers.index(3)) # 1 - What index is it on
print(numbers.count(3)) # 2 - How many occurances

#Adding an element
numbers = [1, 2, 3, 4]

numbers.append(5)
print(numbers) # [1, 2, 3, 4, 5]

numbers.insert(1, 6)
print(numbers) # [1, 6, 2, 3, 4, 5]

#Removing an element
numbers = [1, 2, 3, 4, 5, 6]

numbers.pop()
print(numbers) # [1, 2, 3, 4, 5]

numbers.pop(1)
print(numbers) # [1, 3, 4, 5]

numbers = [1, 2, 3, 1, 2, 3]

numbers.remove(3)
print(numbers) # [1, 2, 1, 2, 3]