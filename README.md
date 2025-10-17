CS 1300 
Lab 10 Files 

Objectives
•	Demonstrate the ability to create, iterate through, and extract elements from a list.
•	Open and read from a text file.
•	Read the data from a text file into a list and process the data.

Specifications

Getting started

1.	Download the file grades.txt which will be the file that this assignment will read data from. Make sure to store this file in the same folder where your Python file is located.

2.	Create a new Python program file named: FirstnameLastnameFiles.py, e.g., SallyWhiteFiles.py.

3.	Define a main function that will be the entry point and control the program. 

4.	Within the main function body, add a print statement that will print out Lab 10 by your name, e.g., Lab 10 by Sally White.

5.	Add a line at the end of the file that will call the main function.

Part 1 – Count grades in a list (3 pts.)

1.	Write a function called count_grades that will take a list of grades and return a list of the number of A’s, B’s, C’s, D’s and F’s based on the 90, 80, 70, 60 scale. For example, if you called this function and passed it the list [80, 75, 92, 88, 54, 98] it would return the list [2, 2, 1, 0, 1], where this means there are 2 As, 2 Bs, 1 C, 0 Ds, and 1 F.

a.	Note: You wrote this function is Assignment 7 you may copy it from your Assignment 7 code.

Part 2 – Reading grades stored in a file (5 pts.)

1.	Write a function called open_and_read_grades. This function will open a text file called grades.txt and read all the students enrolled in a class and the grades they earned. All the grades will be stored in a list and that list of grades only will be returned from the function.

Note: the data stored on each line of the text file is the student’s last name, then first name, 917 number, and grade as a numerical score between 0 and 100. Each field is separated by a comma. 

Part 3 – Analyze the grades (12 pts.)

1.	Write a function called analyze_grades. Within this function do the following:

a.	Make a call to the open_and_read_grades function and assign that function to a variable that will store the list of grades read in and returned from the function.

b.	Take the list of grades returned and print out the following:

i.	The highest grade.
ii.	The lowest grade.
iii.	The average grade.
iv.	The median grade. Remember if there are even number of grades in the list the median is the average of the middle two elements.
v.	The grading breakdown. The number of A’s, B’s, etc.
vi.	Prompt the user for a threshold value between 0 and 100 and then print out the number of grades that are greater than or equal to the threshold value.

Note: You may want to write some helper functions to calculate some of the output values.

Example output (This is just example output and will not be the data output from the grades in the provided grades.txt file. I just made up the values below.)

Enter a grade threshold that you want to count all the grades greater than or equal to that value: 74

The highest grade: 98
The lowest grade: 45
The average grade: 83.45
The median grade: 82.5
The number of grades greater than or equal to 74: 11
Grading breakdown:
A’s: 4
B’s: 3
C’s: 5
D’s: 6
F’s: 3 

2.	In the main function, add a function call to analyze_grades. 

End of assignment


