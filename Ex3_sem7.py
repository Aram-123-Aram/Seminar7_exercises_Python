'''
на входе такой список a = [4, 3, -10, 1, 7, 12], получить такой [4, -10, 12, 3, 1, 7]
'''
a = [4, 3, -10, 1, 7, 12]
'''
#variant1
b = []
c = []
for x in a:
    if x%2==0:
        b.append(x)
    else:
        c.append(x)
print(b, c)
for x in c:
    b.append(x)
print(b)
'''
'''
#variant2
b = [x for x in a if x%2==0]
c = [x for x in a if x%2!=0]

print(b)
print(c)
b.extend(c)
print(b)
'''
a.sort(key=lambda x: x%2)
print(a)