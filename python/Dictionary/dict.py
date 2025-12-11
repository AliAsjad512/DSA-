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



    student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for student, score in student_scores.items():
    print(student)
    if score >= 90:
        student_grades[student] = "Outstanding"
    elif score >= 80:
        student_grades[student] = "Exceeds Expectations"
    elif score >= 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)