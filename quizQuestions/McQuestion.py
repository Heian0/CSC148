from Question import Question


class McQuestion(Question):

    def compareAnswer(self, givenAnswer):

        if ord(givenAnswer) not in range (61, 66):
            print('''please enter "a", "b", "c", "d", or "e".''')
            return

        super(Question, self).compareAnswer