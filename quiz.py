class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def check_answer(self, user_answer):
        return user_answer == self.answer


class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.question_index = 0

    def get_question(self):
        if self.question_index < len(self.questions):
            return self.questions[self.question_index]
        else:
            return None

    def display_question(self, question):
        print(question.text)
        for i, choice in enumerate(question.choices):
            print(f"{i + 1}. {choice}")
        user_answer = input("Enter the number of your answer: ")
        if user_answer.isdigit():
            return int(user_answer)
        else:
            return -1

    def play(self):
        question = self.get_question()
        while question:
            self.display_question(question)
            user_answer = self.display_question(question) - 1
            if question.check_answer(user_answer):
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Wrong. The correct answer was: {question.choices[question.answer]}\n")
            self.question_index += 1
            question = self.get_question()
        print(f"Quiz completed! Your score is: {self.score}/{len(self.questions)}")


# Sample quiz questions
questions = [
    Question("What is the capital of France?", ["London", "Berlin", "Paris", "Madrid"], 2),
    Question("Which planet is known as the Red Planet?", ["Earth", "Mars", "Jupiter", "Venus"], 1),
    Question("What is the largest mammal in the world?", ["Elephant", "Giraffe", "Whale", "Kangaroo"], 2),
]

# Create and play the quiz
quiz = Quiz(questions)
quiz.play()
