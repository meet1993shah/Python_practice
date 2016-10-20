fobj = open('tempfile.txt', 'w')
fobj.write('0123456789abcdef')
fobj.close()
fobj = open('tempfile.txt')
print fobj.tell() #tell us the offset position
fobj.seek(5) #Go to 5th byte
print fobj.tell()
print fobj.read(2) #Read 2 bytes
fobj.seek(-3, 2) #Go to 3rd byte from the end
print fobj.read() #Read till the end of the file
