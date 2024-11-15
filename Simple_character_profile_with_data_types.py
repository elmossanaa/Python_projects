'''Create a simple Python program that displays a fictional character's
profile, including their name, age, height, and a boolean value indicating
if they are a student.

Requirements:
1. Define the following variables:
   - A string for for the character's name.
   - An integer for the characters age.
   a float for the characters height.

2. Use the type() function to check and display the data type of
each variable.

3. Use the print() statements to display the following information:
   - character's name
   - characters age
   - characters height
   - whether the character is a student

4. Display the data type of each variable to ensure that each is
the correct data type.'''


character_name = "Blair Waldorf"
age = 16
height = 64.5
is_student = True

print("Data type for name: " + str(type(character_name)))
print("Data type for age: " + str(type(age)))
print("Data type for height: " + str(type(height)))
print("Data type for proof of being a student: " + str(type(is_student)))


print("character's name: " + character_name)
print("characters age: " + str(age))
print("characters height: " + str(height))
print("whether the character is a student: " + str(is_student))
