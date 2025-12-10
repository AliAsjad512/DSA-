d = {'cat': 'cute', 'dog': 'furry'}
print(d['cat'])  # Output: cute
print('cat' in d)  # Output: True

mydict={ 'ali' :1, 'asjad' :2, 'abbas':3}
print("A VALUE :%d" % mydict['asjad'])
mydict['a']=11
print("A VAUE: %d" %mydict['ali'])
print("keys.%s" %mydict.keys())
print("VALUE:%s" %mydict.values())
for key in mydict.keys():
    print(mydict[key])