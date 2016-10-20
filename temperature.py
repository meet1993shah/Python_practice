fahrenheit = 0.0
print "Fahrenheit Celsius"
while fahrenheit <= 250:
	celsius = (fahrenheit - 32.0) / 1.8
	print "%5.1f %7.2f" % (fahrenheit, celsius)
	fahrenheit = fahrenheit + 25

###
a, b = 45, 54
print a, b
a, b = b, a
print a, b	

###
data = ("Meet Shah", "USA", "Python")
name, country, language = data
print name
print country
print language