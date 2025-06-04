from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

questionBank = []
for questions in question_data:
    questionText= questions["text"]
    questionAnswer = questions["answer"]
    newQuestion = Question(questionText, questionAnswer)
    questionBank.append(newQuestion)
print(questionBank[0].answer)

quiz = QuizBrain(questionBank)
while(1):
    quiz.next_question()