dict1={'city':'Moscow', 'temp':-1, 'wind':'south'}
dict2={'city':'Sochi', 'temp':20, 'wind':'east'}
dict3={'city':'Magadan', 'temp':12, 'wind':'west'}
mydict={'marina':dict1, 'alex':dict2, 'vasya':dict3}
#print(mydict)
aa = input('enter  name: ')
a = aa.lower()
print(a)
if a in mydict:
    print(mydict[a])
else:
    print('wrong name')

x=0
while x<10:
    print(x):
