#1.1
user_input = input("Enter a string with whitespaces: ")
char_list = list(map(lambda x: x.lower(), user_input))

print("Created list is:")
print(char_list)








#1.2
user_input = input("Enter a string with whitespaces: ")
char_list = list(map(lambda x: x.lower(), user_input))

symbol_count = []
for char in char_list:
    found = False
    for item in symbol_count:
        if item[0] == char:
            item = (char, item[1] + 1)
            found = True
            break
    if not found:
        symbol_count.append((char, 1))

print("Code Output:")
print(symbol_count)










#1.3
input_list = [('p', 2), ('u', 1), ('l', 1), (' ', 1), ('f', 1), ('i', 2), ('c', 1), ('t', 1), ('o', 1), ('n', 1)]

# Initialize the three lists
list_vow = []
list_cons = []
list_sym = []


def is_vowel(char):
    vowels = 'aeiou'
    return char in vowels


for item in input_list:
    char, count = item
    if char == ' ':
        list_sym.append(item)
    elif char.isalpha():
        if is_vowel(char):
            list_vow.append(item)
        else:
            list_cons.append(item)
    else:
        list_sym.append(item)


print("list_vow =", list_vow)
print("list_cons =", list_cons)
print("list_sym =", list_sym)










#1.4
list_A = [1, 5, 8, 7, 9, 6, 7, 5, 8, 3, 9, 10, 2, 1, 3, 4]  # 16 elements, divisible by 4


list_A.sort()


total_elements = len(list_A)
q1_boundary = total_elements // 4
q2_boundary = 2 * q1_boundary
q3_boundary = 3 * q1_boundary


q1 = list_A[:q1_boundary] + [0] * (q1_boundary - total_elements % 4)  # Add 0s if necessary
q2 = list_A[q1_boundary:q2_boundary]
q3 = list_A[q2_boundary:q3_boundary]
q4 = list_A[q3_boundary:]


print("q1 =", q1)
print("q2 =", q2)
print("q3 =", q3)
print("q4 =", q4)












#2.1
student_name = input("Enter student name: ")
assignment_scores = input("Enter student's scores for assignments (comma-separated): ").split(',')
lab_scores = input("Enter student's scores for labs (comma-separated): ").split(',')
test_scores = input("Enter student's scores for tests (comma-separated): ").split(',')


assignment_scores = [int(score) for score in assignment_scores]
lab_scores = [float(score) for score in lab_scores]
test_scores = [int(score) for score in test_scores]

student = {
    'name': student_name,
    'assignment': assignment_scores,
    'test': test_scores,
    'lab': lab_scores
}

print("Code Output:")
print(student)













#2.2
student = {'name': 'Adam', 'assignment': [82, 56, 44, 30], 'test': [78, 77], 'lab': [78.2, 77.2]}


submission_check = {
    student['name']: 0  # Initialize the submission count
}


if len(student['assignment']) == 4:
    submission_check[student['name']] += 4


if len(student['lab']) == 2:
    submission_check[student['name']] += 2


if len(student['test']) == 2:
    submission_check[student['name']] += 2

print("Sample Output:")
print(submission_check)











#2.3
student = {'name': 'Adam', 'assignment': [82, 56, 44, 30], 'test': [78, 77], 'lab': [78.2, 77.2]}
submission_rate = {'Adam': 6}


if student['name'] in submission_rate and submission_rate[student['name']] >= 4:
    assignment_avg = sum(student['assignment']) / len(student['assignment'])
    lab_avg = sum(student['lab']) / len(student['lab'])
    test_avg = sum(student['test']) / len(student['test'])
    final_grade = 0.3 * assignment_avg + 0.5 * lab_avg + 0.2 * test_avg
    student['final_grade'] = final_grade
else:
    student['final_grade'] = 0


print("Sample Output 1:")
print(student)


student2 = {'name': 'Kevin', 'assignment': [82, 30], 'test': [], 'lab': [78.2]}
submission_rate = {'Adam': 6, 'Kevin': 3}


if student2['name'] in submission_rate and submission_rate[student2['name']] >= 4:
    assignment_avg = sum(student2['assignment']) / len(student2['assignment'])
    lab_avg = sum(student2['lab']) / len(student2['lab'])
    test_avg = sum(student2['test']) / len(student2['test'])
    final_grade = 0.3 * assignment_avg + 0.5 * lab_avg + 0.2 * test_avg
    student2['final_grade'] = final_grade
else:
    student2['final_grade'] = 0


print("\nSample Output 2:")
print(student2)











#2.4
student1 = {'name': 'Adam', 'assignment': [82, 56, 44, 30], 'test': [78, 77], 'lab': [78.2, 77.2], 'final_grade': 70.25}
student2 = {'name': 'Kevin', 'assignment': [82, 30], 'test': [], 'lab': [78.2], 'final_grade': 0}


students_list = [student1, student2]


students = {student['name']: {key: value for key, value in student.items() if key != 'name'} for student in students_list}


print("Sample Output:")
print(students)









#3.1
transactions = [(1001, 2), (1001, 1), (1003, 2), (1005, 2), (1001, 3), (1007, 1), (1007, 2), (1100, 2), (1003, 2),
                (1001, 1)]


stats = {}


for user_id, transaction_type in transactions:
    if user_id not in stats:
        stats[user_id] = {1: 0, 2: 0, 3: 0, 'mft': 0, 'lft': 0}

    stats[user_id][transaction_type] += 1


for user_id, user_stats in stats.items():
    max_transaction = max(user_stats, key=lambda k: user_stats[k] if k != 'mft' and k != 'lft' else 0)
    min_transaction = min(user_stats, key=lambda k: user_stats[k] if k != 'mft' and k != 'lft' else float('inf'))
    user_stats['mft'] = max_transaction
    user_stats['lft'] = min_transaction


print("Code Output 1:")
print(stats)





