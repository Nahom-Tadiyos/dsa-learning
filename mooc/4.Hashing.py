numbers = set()

numbers.add(1)
numbers.add(2)
numbers.add(3)

print(numbers) # {1, 2, 3}

#You can also creat a set from a list
numbers = set([1, 2, 3])

print(numbers) # {1, 2, 3}

#If an element is in the set
print(3 in numbers) # True
print(4 in numbers) # False

#Remove an element
print(numbers) # {1, 2, 3}
numbers.remove(2)
print(numbers) # {1, 3}

#How many numbers does it contain - O(n^2)
def count_distinct(numbers):
    seen = []
    for x in numbers:
        if x not in seen:
            seen.append(x)
    return len(seen)

#Faster version
def count_distinct(numbers):
    return len(set(numbers))

#Dictionary
weights = {}

weights["apina"] = 100
weights["banaani"] = 1
weights["cembalo"] = 500

#The same thing can be created as
weights = {"apina": 100, "banaani": 1, "cembalo": 500}

#Hass an element occured
seen = {}
for x in seen:
    seen[x] = True

#Example find the mode
def find_mode(numbers):
    count = {}
    mode = numbers[0]

    for x in numbers:
        if x not in count:
            count[x] = 0
        count[x] += 1

        if count[x] > count[mode]:
            mode = x
    
    return mode

#hashing for your own class
class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):#return the hash value of the object
        return hash((self.x, self.y))
    
    def __eg__(self, other):#compares if two objects have identical content
        return (self.x, self.y) == (other.x, other.y)

locations = set()
locations.add(Location(1, 2))
locations.add(Location(3, -5))
locations.add(Location(1, 4))



