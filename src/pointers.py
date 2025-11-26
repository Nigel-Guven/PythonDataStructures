num1 = 11
num2 = num1

print("Before")

print(id(num1))
print(num1)
print(id(num2))
print(num2)


num2 = 22

print("After")

print(id(num1))
print(num1)
print(id(num2))
print(num2)

print("Before")

dictionary1 = { 'value': 16}

print(id(dictionary1))
print(dictionary1)
dictionary2 = dictionary1
print(id(dictionary2))
print(dictionary2)


dictionary2['value'] = 26

print("After")
print(id(dictionary1))
print(dictionary1)
print(id(dictionary2))
print(dictionary2)