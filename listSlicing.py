numbers=[2,3,4,5]
numbers.append(4)
print(numbers)
numbers.sort()
print(numbers)
numbers.insert(3,9)
print(numbers)
numbers.pop(3)
print(numbers)
numbers[2]=5  # List are mutable
print(numbers)

#tuple
a=9
b=8
a,b=b,a
print(a,b)
num=(1,2)  # Tuple is immutable
print(num)