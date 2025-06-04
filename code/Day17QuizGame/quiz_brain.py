class QuizBrain:
    def __init__(self, qusetionsList):
        self.questionsList = qusetionsList
        self.questionNumber = 0
        self.score = 0
        self.total = 0
    def next_question(self):
        nextQuestion = self.questionsList[self.questionNumber]
        self.questionNumber += 1 
        answer = input(f"Q.{self.questionNumber}: {nextQuestion.text} (True/False)?: ")
        if(answer.lower() == nextQuestion.answer.lower()):
            print("You got it right!")
            self.score += 1
        else:
            print("You got it wrong...")
        self.total += 1
        print(f"The correct answer is: {nextQuestion.answer}")
        print(f"Your current score is: {self.score}/{self.total}.")
        return answer
    
        