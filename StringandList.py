print "Find and Replace"
words = "It's thanksgiving day. It's my birthday, too!"
print words
print words.find('day')
print words.replace('day','month')

print"Min and Max"
x = [2,54,-2,7,12,98]
print min(x)
print max(x)

print"First and Last"
x = ["hello",2,54,-2,7,12,98,"world"]
print x[0]
print x[len(x) - 1]
y = []
y.append(x[0])
y.append(x[len(x)-1])
print y

print"New List"
x = [19,2,54,-2,7,12,98,32,10,-3,6]
print x
y = sorted(x)
print y
b = y[:len(y)/2]
a = y[len(y)/2:]
a.insert(0, b)
print a
