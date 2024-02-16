n = int(input())

student_answers = []
correct_answers = []

for i in range(n):
    student_answers.append(input())

for i in range(n):
    correct_answers.append(input())

answered_correctly = 0
for i in range(n):
    if student_answers[i] == correct_answers[i]:
        answered_correctly += 1

print(answered_correctly)