import random

# Set up the game
lives = 3
score = 0
rounds = 5

# Define the questions, choices, and answers
questions = {
    "What is a reusable alternative to plastic bags?": {
        "a": "paper bags",
        "b": "reusable tote bags",
        "c": "plastic bags",
        "d": "compostable bags",
        "answer": "b"
    },
    "Which of the following is a way to reduce food waste?": {
        "a": "buying more food than you need",
        "b": "throwing away leftovers",
        "c": "meal planning",
        "d": "ordering takeout",
        "answer": "c"
    },
    "What is a sustainable mode of transportation?": {
        "a": "driving alone in a gas-guzzling car",
        "b": "taking a taxi",
        "c": "biking",
        "d": "flying",
        "answer": "c"
    },
    "Which of the following is a way to conserve water in your home?": {
        "a": "letting the faucet run while brushing your teeth",
        "b": "taking long showers",
        "c": "fixing leaks promptly",
        "d": "watering your lawn every day",
        "answer": "c"
    },
    "Which of the following is a way to reduce energy consumption?": {
        "a": "leaving lights on when you leave a room",
        "b": "using a clothes dryer instead of hanging clothes to dry",
        "c": "using a dishwasher instead of washing dishes by hand",
        "d": "turning off electronics when not in use",
        "answer": "d"
    }
}

# Define the game loop
for i in range(rounds):
    # Get a random question and answer
    question, choices = random.choice(list(questions.items()))

    # Print the question and choices
    print(f"Round {i + 1}: {question}")
    for choice, answer in choices.items():
        if choice != "answer":
            print(f"{choice}: {answer}")

    # Prompt the user for an answer
    user_answer = input("Your answer: ")

    # Check the user's answer
    if user_answer.lower() == choices["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect.")
        lives -= 1

    # Check if the game is over
    if lives == 0:
        print("Game over!")
        break

    # Print the current score and lives
    print(f"Score: {score} | Lives: {lives}")

# Print the final score
print(f"Final score: {score}")
