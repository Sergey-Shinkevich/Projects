grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list = sorted(list(students))
dict_students = dict.fromkeys(students_list)
dict_students[students_list[0]] = sum(grades[0])/len(grades[0])
dict_students[students_list[1]] = sum(grades[1])/len(grades[1])
dict_students[students_list[2]] = sum(grades[2])/len(grades[2])
dict_students[students_list[3]] = sum(grades[3])/len(grades[3])
dict_students[students_list[4]] = sum(grades[4])/len(grades[4])
print(dict_students)
