print "Scores and Grades"
def scores():
    for i in range(0,10):
        import random
        score = random.randint(60, 100)
        if score >= 60 and score <=69:
            print "Score:", score, "; Your grade is D"
        elif score >=70 and score <=79:
            print "Score:", score, "; Your grade is C"
        elif score >=80 and score <=89:
            print "Score:", score, "; Your grade is B"
        elif score >=90 and score <=100:
            print "Score:", score, "; Your grade is A"
    print "End of the program. Bye!"
scores()
