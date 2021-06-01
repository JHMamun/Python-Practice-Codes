students_count = 1000
students_count: int
print(type(students_count))

age: int = 20
age = "Python"
print(age)
# mutable types
x = 1
print(id(x))

x = x + 1
print(id(x))

# immutable types
x = [1, 2, 3]
print(id(x))
x.append(4)
print(id(x))

course = "Python Programming"
print(len(course))
