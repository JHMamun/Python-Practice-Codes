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

# strings are immutable
course = "Python Programming"
print(len(course))
print(course[0])
print(course[-1])
print(course[-2])

print(course[0:3])  # slicing Pyt from Python Programming
print(course[:3])
print(course[0:])  # returns entire string
print(course[:])  # returns entire string

print(id(course))
print(id(course[0]))


# escape character
message = 'Python "Programming'
print(message)
message = "Python \"Programming"
print(message)
message = "Python \nProgramming"
print(message)

# use of triple quote
message = """
Python
Programming
"""
print(message)
