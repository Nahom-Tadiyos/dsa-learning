class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, x):
        self.stack.append(x)

    def top(self):
        if len(self.stack) == 0:
            raise IndexError("top from empty stack")
        return self.stack[-1]
    
    def pop(self):
        if len(self.stack) == 0:
            raise IndexError("pop from empty stack")
        self.stack.pop()

    def __repr__(self):
        return str(self.stack) 

    def __len__(self):
        return len(self.stack)   

class SuperStack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def top(self):
        self.stack[-1]
    
    def pop(self):
        self.stack.pop()

    def push_many(self, x, k):
        for i in range(k):
            self.push(x)

    def __repr__(self):
        return str(self.stack) 

    def __len__(self):
        return len(self.stack)  

class Mode:
    def __init__(self):
        self.count = {}
        self.status = (0, 0)
        
    def add(self, x):
        if x not in self.count:
            self.count[x] = 0
        self.count[x] += 1
        self.status = max(self.status, (self.count[x], x))

    def mode(self):
        return self.status[1]


s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.top()) # 3
print(s.top()) # 3
s.pop()
print(s.top()) # 2
print(s)
print(len(s))

a = SuperStack()
a.push_many(3, 8)
a.push(4)
a.push_many(2, 5)

print(a)

b = Mode()
b.add(3)
b.add(3)
b.add(2)
print(b.mode())