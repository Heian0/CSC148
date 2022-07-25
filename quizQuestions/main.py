from Question import Question
from McQuestion import McQuestion
from NumQuestion import NumQuestion

if __name__ == "__main__":

    q1 = Question("What is 1 + 1?", "2")
    q2 = McQuestion("Example MC question, answer is 'a'.", "a")
    q3 = NumQuestion("Example Numerical question, answer is in range of 0.5 to 0.7.", (0.5, 0.7)) 

    q1.displayQuestion()
    q2.displayQuestion()
    q3.displayQuestion()