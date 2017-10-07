#input
working_list = ['magical unicorns',19,'hello',5,'world']

x = working_list
b = []
c = []
for element in x:
    if type(element) is int:
        b.append(element)
    elif type(element) is str:
        c.append(element)
print c
print sum(b)
