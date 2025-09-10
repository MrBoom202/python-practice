list_of_students = [{'student':'petrovych1','rating':1},{'student':'petrovych2','rating':2},{'student':'petrovych4','rating':4},{'student':'petrovych3','rating':3}]

list_of_students.sort(key=lambda student: student['rating'],reverse=True)
print(list_of_students)

printPattern = "Place {index} - {studentname} {rating}!"
for index, concreteStudent in enumerate(list_of_students[0:3]):
    print('Place #'+str(index)+' :'+str(concreteStudent['student'])+ ' '+str(concreteStudent['rating']))