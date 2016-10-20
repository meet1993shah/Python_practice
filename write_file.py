fobj = open("ircnicks.txt", 'w')
fobj.write('powerpork\n')
fobj.write('indrag\n')
fobj.write('mishti\n')
fobj.write('sankarshan')
fobj.close()

fobj = open('ircnicks.txt')
s = fobj.read()
print s