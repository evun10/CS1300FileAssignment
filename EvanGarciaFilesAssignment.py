def main():
    print("Evan Garcia Files Assignment")
    analyzeGrades()

    # PART 1: countGrades will the parameter gradeList which will act as the grade list. It will iterate through the list going through A's, B's, C's, D's, and F's. This will add to the number in the list showcasing how many of each grade there are.
def countGrades(gradeList):
    grades = [0, 0, 0, 0 ,0]

    for grade in gradeList:
        if (grade >= 90):
            grades[0] +=1

        elif(grade >= 80):
            grades[1] +=1

        elif(grade >= 70):
            grades[2] +=1

        elif(grade >= 60):
            grades[3] +=1

        else:
            grades[4] +=1
        
    return grades

    # PART 2: function openAndReadGrades will open the .txt file "grades" and for each line go through the file and split each string. Then will close and return the grades.
def openAndReadGrades():
    file = open("grades.txt", "r")
    grades = []

    for currentLine in file:
        myString = currentLine.strip()
        temp = myString.split(",")
        temp = temp[3].split("\n")
        grades.append(int(temp[0]))

    file.close()
    return grades

def analyzeGrades():
    grades = openAndReadGrades()
    print("The highest grade:", max(grades))
    print("The lowest grade:", min(grades))
    print("The average grade:", sum(grades) / len(grades))
    
main()