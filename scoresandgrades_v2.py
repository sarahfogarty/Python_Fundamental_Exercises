#!/usr/bin/env python

# score = int(raw_input("Please enter a score"))
score1 = int(raw_input("Please enter the first score"))
score2 = int(raw_input("Please enter the second score"))
score3 = int(raw_input("Please enter the third score"))
score4 = int(raw_input("Please enter the fourth score"))
score5 = int(raw_input("Please enter the fifth score"))
score6 = int(raw_input("Please enter the sixth score"))
score7 = int(raw_input("Please enter the seventh score"))
score8 = int(raw_input("Please enter the eighth score"))
score9 = int(raw_input("Please enter the ninth score"))
score10 = int(raw_input("Please enter the tenth score"))

scores = [score1, score2, score3, score4, score5, score6, score7, score8, score9, score10]

print "Scores and Grades"

for score in scores:
    if score >= 90:
        print "Score:", score, "; Your grade is A"
        # grade = "A"
    elif score >= 80:
        print "Score:", score, "; Your grade is B"
        # grade = "B"
    elif score >= 70:
        print "Score:", score, "; Your grade is C"
        # grade = "C"
    elif score >= 60:
        print "Score:", score, "; Your grade is D"
        # grade = "D"
    else:
        print "Invalid input. Score must be between 60 and 100"

print "End of program. Bye!"