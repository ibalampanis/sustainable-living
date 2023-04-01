import random
import sys

# Define the questions, choices, and answers
questions = {
    "What is a reusable alternative to plastic bags?": {
        "a": "paper bags",
        "b": "reusable tote bags",
        "c": "plastic bags",
        "d": "compostable bags",
        "answer": "b",
        "explanation": "Reusable tote bags are a sustainable alternative to plastic bags, as they can be used multiple times instead of being disposed of after a single use."
    },
    "Which of the following is a way to reduce food waste?": {
        "a": "buying more food than you need",
        "b": "throwing away leftovers",
        "c": "meal planning",
        "d": "ordering takeout",
        "answer": "c",
        "explanation": "Meal planning is an effective way to reduce food waste, as it allows you to buy only the ingredients you need and plan to use leftovers in future meals."
    },
    "What is a sustainable mode of transportation?": {
        "a": "driving alone in a gas-guzzling car",
        "b": "taking a taxi",
        "c": "biking",
        "d": "flying",
        "answer": "c",
        "explanation": "Biking is a sustainable mode of transportation, as it doesn't rely on fossil fuels and doesn't produce greenhouse gas emissions."
    },
    "Which of the following is a way to conserve water in your home?": {
        "a": "letting the faucet run while brushing your teeth",
        "b": "taking long showers",
        "c": "fixing leaks promptly",
        "d": "watering your lawn every day",
        "answer": "c",
        "explanation": "Fixing leaks promptly is a way to conserve water in your home, as even small leaks can waste a significant amount of water over time."
    },
    "Which of the following is a way to reduce energy consumption?": {
        "a": "leaving lights on when you leave a room",
        "b": "using a clothes dryer instead of hanging clothes to dry",
        "c": "using a dishwasher instead of washing dishes by hand",
        "d": "turning off electronics when not in use",
        "answer": "d",
        "explanation": "Turning off electronics when not in use is a way to reduce energy consumption, as even when not in use, many electronics continue to consume energy if they're plugged in."
    },
    "What is the difference between energy conservation and energy efficiency?": {
        "a": "Energy conservation is using less energy, while energy efficiency is using energy more efficiently",
        "b": "Energy conservation is using renewable energy, while energy efficiency is using non-renewable energy",
        "c": "Energy conservation and energy efficiency are the same thing",
        "d": "Energy conservation is using energy more efficiently, while energy efficiency is using less energy",
        "answer": "d",
        "explanation": "Energy conservation involves using less energy overall, while energy efficiency involves using less energy to achieve the same level of output."
    },
    "What is the concept of 'reduce, reuse, recycle'?": {
        "a": "A marketing slogan for eco-friendly products",
        "b": "A set of guidelines for waste management",
        "c": "A type of composting technique",
        "d": "A method for reducing greenhouse gas emissions",
        "answer": "b",
        "explanation": "\"Reduce, reuse, recycle\" is a set of guidelines for waste management. The concept encourages individuals and businesses to reduce their waste generation, reuse items whenever possible, and recycle materials that cannot be reused."
    },
    "What is the purpose of sustainable agriculture?": {
        "a": "To maximize profits for farmers",
        "b": "To minimize the environmental impact of agriculture",
        "c": "To increase crop yields at all costs",
        "d": "To use only organic farming methods",
        "answer": "b",
        "explanation": "The purpose of sustainable agriculture is to minimize the environmental impact of agriculture. This includes reducing the use of pesticides and fertilizers, conserving water resources, and promoting biodiversity."
    },
    "What is the difference between biodegradable and compostable?": {
        "a": "There is no difference, they are the same thing",
        "b": "Biodegradable materials break down faster than compostable materials",
        "c": "Compostable materials can only break down in commercial composting facilities",
        "d": "Compostable materials are made from organic materials, while biodegradable materials can be made from any material",
        "answer": "c",
        "explanation": "The main difference between biodegradable and compostable is that compostable materials can only break down in commercial composting facilities, while biodegradable materials can break down in a variety of environments."
    },
    "What is the purpose of the Paris Agreement on climate change?": {
        "a": "To reduce greenhouse gas emissions and limit global warming",
        "b": "To promote the use of fossil fuels",
        "c": "To increase global economic growth",
        "d": "To reduce the use of renewable energy sources",
        "answer": "a",
        "explanation": "The purpose of the Paris Agreement on climate change is to reduce greenhouse gas emissions and limit global warming. The agreement aims to keep global temperature rise below 2 degrees Celsius above pre-industrial levels, and to pursue efforts to limit the temperature increase even further to 1.5 degrees Celsius."
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
    print('\033[1m' + f'Round {i + 1}: {question}' + '\033[0m')
    for choice, answer in choices.items():
        if choice != "answer" and choice != "explanation":
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
        print('\033[1;32m' + 'Correct!' + '\033[0m' + '\n')
        score += 1
    else:
        print('\033[1;31m' + 'Incorrect.' + '\033[0m' + '\n')
        lives -= 1
        print('\033[1m' + 'Here is an explanation of this:\n' + '\033[0m' + choices["explanation"] + "\n")

    # Check if the game is over
    if lives == 0:
        print('\033[1m' + 'Game over!' + '\033[0m')
        break

    # Print the current score and lives
    print(f"Score: {score} | Lives: {lives}")

# Print the final score
print(f"Final score: {score}")
