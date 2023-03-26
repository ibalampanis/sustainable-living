import datetime

# Get the current day of the week as an integer (0=Monday, 1=Tuesday, etc.)
day_of_week = datetime.datetime.today().weekday()

# Define a list of poems, one for each day of the week
poems = [
    "In the morning light I rise,\nTo greet the day with open eyes.\nA new week, a fresh start,\nTo live sustainably, from my heart.",  # Monday
    "Today I choose to make a change,\nTo reduce my waste and carbon range.\nI'll bring my own bag and use less power,\nAnd strive for a greener, cleaner hour.",  # Tuesday
    "Midweek comes, and with it hope,\nThat our planet can find a way to cope.\nI'll bike to work and compost my scraps,\nAnd lessen my reliance on harmful traps.",  # Wednesday
    "As the end of the week draws near,\nI'll choose to buy local, and not from afar.\nFor supporting my community and reducing my miles,\nIs a small way to live sustainably with style.",  # Thursday
    "Friday night, a time to unwind,\nBut I won't forget to keep sustainability in mind.\nI'll choose meatless meals and turn off my lights,\nAnd enjoy a peaceful evening with natural delights.",  # Friday
    "Weekend time, a chance to explore,\nThe beauty of nature, I'll adore.\nI'll hike and swim and breathe in fresh air,\nAnd be thankful for this earth that we share.",  # Saturday
    "On this day of rest and reflection,\nI'll think about my sustainable direction.\nI'll plan for the week ahead and set my goals,\nTo live mindfully, and let my sustainability show."  # Sunday
]

# Get the poem for the current day of the week
poem = poems[day_of_week]

# Print the poem
print(poem)