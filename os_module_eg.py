import os
# print os.getuid()
print os.getpid()
# print os.getppid()
# print os.uname()
print os.getcwd()
os.chdir('C:/Users/Meet/Desktop/')
print os.getcwd()

##
print '\n'
def view_dir(path='.'):
	"""
	This function prints all files and directories in the given directory.
	:args path: Path to the directory, default is current directory.
	"""
	names = os.listdir(path)
	names.sort()
	for name in names:
		print name,


view_dir('/')		