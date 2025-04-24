#Activity : You are given the test scores of 5 students across 3 subjects in a 2D NumPy array. 
#Each row represents a student, and each column a subject.

#1.Calculate and print the average score for each student.
#2.Calculate and print the average score for each subject.
#3.Identify the student (row index) with the highest total score.
#4.Add 5 bonus points to the third subject for all students.

import numpy as np 
#Activity : You are given the test scores of 5 students across 3 subjects in a 2D NumPy array. 
#Each row represents a student, and each column a subject.
scores = np.array([
    [78, 85, 90],
    [88, 79, 92],
    [84, 76, 88],
    [90, 93, 94],
    [75, 80, 70]
])
print("The test scores of 5 students across 3 subjects in a 2D :\n", scores)
for i, student_scores in enumerate(scores, start=1):
    print(f"Student {i}: First subject = {student_scores[0]}, Second subject = {student_scores[1]}, Third subject = {student_scores[2]}")

#the average score for each student.
student_average = np.mean(scores, axis=1)
print("\nThe average score for each student:")
for i, avg in enumerate(student_average, start=1):
    print(f"  Student {i}: {avg:.2f}")

#the average score for each subject.
subject_average = np.mean(scores,axis=0)
print("\nThe average score for each subject :")
for i, avg in enumerate(subject_average, start=1):
    print(f"  Subject {i}: {avg:.2f}")

#Identify the student (row index) with the highest total score.
student_totalscore = np.sum(scores,axis=1)
highest_studentscore= np.argmax(student_totalscore)
print("\nStudent with the highest total score (row index):",highest_studentscore)
print("\nStudent",highest_studentscore+1, "got the highest total score")
student_scores = scores[highest_studentscore]
print(f"First subject = {student_scores[0]}, Second subject = {student_scores[1]}, Third subject = {student_scores[2]}")
print("Their total score :", student_totalscore[highest_studentscore])

#Add 5 bonus points to the third subject for all students.
scores[:,2] += 5
print("\nScore after adding bonus 5 points to the third subject: ")
for i, student_scores in enumerate(scores, start=1):
    print(f"Studunt {i}: First subject = {student_scores[0]}, Second subject = {student_scores[1]}, Third subject = {student_scores[2]}")
