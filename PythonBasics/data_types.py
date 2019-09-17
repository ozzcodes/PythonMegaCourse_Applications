# type attributes
student_grades = [9.1, 8.8, 7.5]

my_sum = sum(student_grades)
length = len(student_grades)
mean = my_sum / length
print(mean)

# Dictionaries
student_grades = {'Mary': 9.1, 'Sam': 8.8, 'John': 7.5}
my_sum = sum(student_grades.values())
length = len(student_grades)
mean = my_sum / length
print(mean)

# Tuples (Immutable)
monday_temps = (1, 4, 5)
print(monday_temps)

# noinspection PyListCreation
monday_temps2 = [1, 4, 5]
monday_temps2.append(6)
print(monday_temps2)
