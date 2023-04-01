import random
import sys

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
    },
    "What is the difference between energy conservation and energy efficiency?": {
        "a": "Energy conservation is using less energy, while energy efficiency is using energy more efficiently",
        "b": "Energy conservation is using renewable energy, while energy efficiency is using non-renewable energy",
        "c": "Energy conservation and energy efficiency are the same thing",
        "d": "Energy conservation is using energy more efficiently, while energy efficiency is using less energy",
        "answer": "d"
    },
    "What is the concept of 'reduce, reuse, recycle'?": {
        "a": "A marketing slogan for eco-friendly products",
        "b": "A set of guidelines for waste management",
        "c": "A type of composting technique",
        "d": "A method for reducing greenhouse gas emissions",
        "answer": "b"
    },
    "What is the purpose of sustainable agriculture?": {
        "a": "To maximize profits for farmers",
        "b": "To minimize the environmental impact of agriculture",
        "c": "To increase crop yields at all costs",
        "d": "To use only organic farming methods",
        "answer": "b"
    },
    "What is the difference between biodegradable and compostable?": {
        "a": "There is no difference, they are the same thing",
        "b": "Biodegradable materials break down faster than compostable materials",
        "c": "Compostable materials can only break down in commercial composting facilities",
        "d": "Compostable materials are made from organic materials, while biodegradable materials can be made from any material",
        "answer": "c"
    },
    "What is the purpose of the Paris Agreement on climate change?": {
        "a": "To reduce greenhouse gas emissions and limit global warming",
        "b": "To promote the use of fossil fuels",
        "c": "To increase global economic growth",
        "d": "To reduce the use of renewable energy sources",
        "answer": "a"
    }
}

# Set up the game
lives = 3
score = 0
rounds = 5

# Define the list which store the already used Question
usedQuestion = []

# Define the game loop
for i in range(rounds):

    # Get a random question and answer, different every time
    while True:
        question, choices = random.choice(list(questions.items()))
        if question not in usedQuestion:
            usedQuestion.append(question)
            break

    # Print the question and choices
    print(f"Round {i + 1}: {question}")
    for choice, answer in choices.items():
        if choice != "answer":
            print(f"{choice}: {answer}")

    # Prompt the user for an answer
    while True:
        user_answer = input("Your answer: ")
        if user_answer.lower() in ['a', 'b', 'c', 'd', 'exit']:
            break
        else:
            print("Answer must be one of a,b,c,d or exit to terminate.\nTry again!")

    # Check the user's answer
    if user_answer.lower() == 'exit':
        sys.exit()
    elif user_answer.lower() == choices["answer"]:
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect.\n")
        lives -= 1

    # Check if the game is over
    if lives == 0:
        print("Game over!")
        break

    # Print the current score and lives
    print(f"Score: {score} | Lives: {lives}")

# Print the final score
print(f"Final score: {score}")
