#Create a dictionaries of student marks
#1.create a dictionaries where student names are key and their marks are values.
#2.ask the user to input  a student name.
#3.Retrieves and display the corresponding marks.
#4.if the student's name is not found, display an appropriate message.
Student_marks={
    'max':30,
    'rehan':33,
    'shahid':33,
}

user_input=input("Enter a student name : ")

if user_input in Student_marks:
   print(f"{user_input} Mark's {Student_marks[user_input]}")
else:
    print("Student is not found.")








