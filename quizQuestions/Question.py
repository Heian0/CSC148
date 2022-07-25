class Question:

    def __init__(self, text, answer):

        self.text = text
        self.answer = answer

    def displayQuestion(self):

        print(self.text)
        givenAnswer = input()
        self.compareAnswer(givenAnswer)

    def compareAnswer(self, givenAnswer): return givenAnswer == self.answer