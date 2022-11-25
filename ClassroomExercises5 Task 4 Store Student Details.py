print("Welcome to the Student Database Program") 

#creates an empty dictionary for the course list 

course_list = {} 

#creates a student details dictionary 

student = { 

    "name" : "Amy Harrison", 

    "course" : "BIT", 

    "Year" : 1  

    } 

  

course_list.update({"10101010" : student}) #used to update the list 

  

student = { 

    "name" : "Alexander Moore", 

    "course" : "Computer Science", 

    "Year" : 1 

    } 

  

course_list.update({"01010101" : student}) 

  

student = { 

    "name" : "Jason Marshall", 

    "course" : "CIT", 

    "Year" : 2 

    } 

  

course_list.update({"01110111" : student}) #updating the list 

  

student = { 

    "name" : "Seren Hussain", 

    "course" : "BIT", 

    "Year" : 2 

    } 

  

course_list.update({"01001110" : student}) #updating the list 

  

student_id = input("Enter student ID> ") 

  

if student_id in course_list.keys(): #check the dictionary keys for student ID

    print(f"Found student with id {student_id}") 

    student = course_list[student_id] #displays details if it is in the list 

    print(f"Student name: {student['name']}") 

    print(f"Course name: {student['course']}") 

    print(f"Year: {student['Year']}") 

else: #if not present then show this message 

    print(f"Student ID {student_id} not recognised") 