def count(a, b, c):
    return c // min(a,b)

if __name__ == "__main__":
    print(count(3, 4, 11))
    print(count(5, 1, 100))
    print(count(2, 3, 1))
    print(count(2, 3, 9))