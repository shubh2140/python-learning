studentMarks = int(input("Enter the marks : "))

if(studentMarks > 90):
    print("Grade A")
elif(studentMarks > 80 and studentMarks <= 90):
    print("Grade B")
elif(studentMarks > 70 and studentMarks <= 80):
    print("Grade C")
else:
    print("Grade D")
