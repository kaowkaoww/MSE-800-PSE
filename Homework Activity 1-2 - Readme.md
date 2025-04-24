# Activity : You are given the test scores of 5 students across 3 subjects in a 2D NumPy array 
Each row represents a student, and each column represents a subject.

## Description
This activity demonstrates how to analyze student test scores using NumPy with a 2D array.  
Each row in the array represents a student, and each column represents a subject.

This activity helped me practice basic data analysis using Python and NumPy, especially working with arrays and understanding how to manipulate data without using loops everywhere.

## What I Learned

1. Calculates and prints the average score for each student by using np.mean() to find averages across rows (per student) and columns (per subject)
2. Calculates and prints the average score for each subject by using np.argmax() to find the student with the highest score
3. Identifies the student (row index) with the highest total score and displays their total and individual subject scores by using np.argmax() to find the student with the highest score
4. Adds 5 bonus points to the third subject (for all students) and displays the updated score array by using `scores[:, 2] += 5` means: go to column 2 (the third subject) for all students, and add 5 points to each score.

## extra thoughts
At first, I wasn’t sure how to calculate things like “average by row” or “total by row” without using loops.
<<<<<<< HEAD
But NumPy makes it super easy once I understood how to use axis=0 and axis=1. It was also really cool learning how to update specific subjects without needing to write extra for loops. This exercise made me feel more confident in using NumPy for simple data analysis, and I think it’s a good foundation for bigger data projects in the future.
=======
But NumPy makes it super easy once I understood how to use axis=0 and axis=1. It was also really cool learning how to update specific subjects without needing to write extra for loops. This exercise made me feel more confident in using NumPy for simple data analysis, and I think it’s a good foundation for bigger data projects in the future.
>>>>>>> 5da9e6b (update activity 1.2)
