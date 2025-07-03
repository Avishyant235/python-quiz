questions = [
    {"question": "What is the capital of Nepal?", "options": [
        "A. Pokhara", "B. Kathmandu", "C. Biratnagar", "D. Lalitpur"], "answer": "B"},
    {"question": "Which planet is known as the Red Planet?", "options": [
        "A. Earth", "B. Mars", "C. Venus", "D. Saturn"], "answer": "B"},
    {"question": "What is the result of 5 + 7?",
        "options": ["A. 10", "B. 11", "C. 12", "D. 13"], "answer": "C"},
]


def run_quiz():
    score = 0

    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)

        user_answer = input(
            "Enter your answer (A, B, C, or D): ").strip().upper()

        if user_answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.")

    print(f"\nYour final score is {score}/{len(questions)}.")


run_quiz()
