myfile = open ("D:\Elzero\codes\huzeyfe.txt")


# print (myfile)
# print (myfile.mode)
# print (myfile.name)
# print (myfile.encoding)

# print (myfile.read())
# print (myfile.readline())
# print (myfile.readlines())

for line in myfile:
    print (line.strip())
    if line.startswith("05"):
        break

myfile.close