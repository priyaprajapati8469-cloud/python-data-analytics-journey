#count the number of students

numofstudents=int(input("enter the number of students:"))


#Data Storage

studentData = []

#inserting data
for i in range(numofstudents):
     print(f"enter the data of student {i+1}")
     name=input("Name ")
     roll_no=int(input("Roll Number "))
     marks=int(input("Marks "))

     if marks > 95:
          grade = "A"
     elif marks > 80:
          grade = "B"
     elif marks > 60:      
          grade = "C"
     elif marks > 35:     
          grade = "D"
     else:    
          grade = "Fail"
     students = {
          "name": name,
          "roll_no": roll_no,
          "marks":marks,
          "grade" : grade

     }  
     studentData .append(students)

#Data Printing
print("\nAll Student Data: \n")

for s in studentData:
    print(f"{s['name']} -roll_no: {s['roll_no']}- marks{s['marks']} - grade{s['grade']}")

#Passed Student
print("students who are passed:")
for s in studentData:
    if s['marks'] >= 35:
        print(f"{s['name']} - marks: {s['marks']}")