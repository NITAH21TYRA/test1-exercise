#NUMBER 3 (i)
#question 3
#student_marks = [78,83,90,88,75]
def student_marks(marks):
    sum = 0
    for x in marks:
        sum += x
        return sum
        print(f"The sum of students marks is {student_marks}")
student_marks(78,83,90,88,75)


#(ii)
student_marks = [78,83,90,88,75]
newList=student_marks[0::4]
print(newList)


#(iii)
#Adding 96 to the list
student_marks = [78,83,90,88,75]
new_item = 96
student_marks.append(new_item)
print(student_marks)


#(iv)
#Updating 78 to 87
student_marks = [78,83,90,88,75]
newList=student_marks.index(78)
student_marks[newList] = 87
print(student_marks)

