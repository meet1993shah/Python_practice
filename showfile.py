name = raw_input("Enter name of the file: ")
fobj = open(name)
print fobj.read()
fobj.close()
