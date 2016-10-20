from collections import Counter
import re
# path = '/usr/share/doc/python-2.7.3/LICENSE'
# words = re.findall('\w+', open(path).read().lower())
# Counter(words).most_common(10)

##
print '\n'
c = Counter(a=4, b=2, c=0, d=-2)
print list(c.elements())
x = 'abracadabra'
print Counter(x).most_common()
print Counter(x).most_common(3)