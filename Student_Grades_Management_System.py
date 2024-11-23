'''Create a program that manages a list of students and their grades, and
calculates the average grade for each student manually.

Requirements:

1. List: store student names in a list.

2. Tuple: Store each student's grades in a tuple (You can store multiple grades
per student).

3. Calculate the average grade for each student manually.

4. Print the name of each student and their average grade.

'''


students = ["Serena", "Blair", "Nate"]
grades = (90,100,82), (96,100,92), (89,94,90)

#calculate average for each student
Serena_avrg = sum(grades[0]) / len(grades[0])
print(students[0] + "'s average grade: " + str(Serena_avrg))

Blair_avrg = sum(grades[1]) /len(grades[1])
print(students[1] + "'s average grade: " + str(Blair_avrg))

Nate_avrg = sum(grades[2]) / len(grades[2])
print(students[2] + "'s average grade: " + str(Nate_avrg))

