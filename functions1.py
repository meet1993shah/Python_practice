def sum(a, b):
	return a + b

res = sum(234234, 34453546464)
print res

def palindrome(s):
	return s == s[::-1]

if __name__ == '__main__':
	s = raw_input("Enter a string: ")
	if palindrome(s):
		print "Yay a palindrome"
	else:
		print "Oh no, not a palindrome"