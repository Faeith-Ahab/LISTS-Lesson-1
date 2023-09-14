#   Example
student_marks = [100, 90, 85, 95]
print(student_marks)

#   Print the type of the list
print(type(student_marks))

#   List items are indexed, the first item has index [0], the second item has index [1] and so on...
print(student_marks[0])

#   There is positive indexing and positive indexing
#Generally we index positively, when negative indexing, 
#you start from the last chararter in the list 
#counting from negative one i.e. -1
#    Positive indexing
print(student_marks[-1])
#    Negative indexing
print(student_marks[3])

#    Slicing
#Selecting a particular range of items from a list
print(student_marks[0:2])


#   Checking if item exists
if 100 in student_marks:
    print("yes, 100 is in the list")
else:
    print("no, 100 is not on the list")

    
