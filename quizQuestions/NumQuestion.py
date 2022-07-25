from Question import Question


class NumQuestion(Question):

        def __init__(self, text, answerRange):
            self.text = text
            self.answerRange = answerRange

        def compareAnswer(self, givenAnswer):
            if givenAnswer != float: 
                print("please enter an answer of type float.")
                return

            return givenAnswer in range(self.answerRange[0], self.answerRange[1])