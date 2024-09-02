def say_hello (name, age) :
    return f"Hello {name}. Your age is {age}"

print (say_hello ("Huzeyfe", 31))
print (say_hello.__name__)
print (type(say_hello))


print ("#"*50)
hello = lambda name, age : f"Hello {name}. Your age is {age}"


print (hello ("Ali", 32))




print (hello.__name__)
print (type(hello))

