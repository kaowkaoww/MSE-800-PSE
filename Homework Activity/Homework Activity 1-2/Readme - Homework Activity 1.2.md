# Activity : You are given the test scores of 5 students across 3 subjects in a 2D NumPy array 
Each row represents a student, and each column represents a subject.

## Description
This activity demonstrates how to analyze student test scores using NumPy with a 2D array.  
Each row in the array represents a student, and each column represents a subject.

The program performs the following tasks:

1. Calculates and prints the average score for each student.
2. Calculates and prints the average score for each subject.
3. Identifies the student (row index) with the highest total score and displays their total and individual subject scores.
4. Adds 5 bonus points to the third subject (for all students) and displays the updated score array.

## What I Learned

- How to calculate the average using `np.mean()` across rows and columns.
- How to calculate total scores with `np.sum()`.
- How to find the index of the highest scoring student with `np.argmax()`.
- How to use array slicing and broadcasting to modify specific parts of the array.  
  For example, `scores[:, 2] += 5` means: go to column 2 (the third subject) for all students, and add 5 points to each score.
