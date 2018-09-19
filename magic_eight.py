# SI 507 Hw3
# Group Member:
# Person A:
# Person B:
# Section 003: Wednesday 10:00 - 11:30 AM

import random

# create a function that ask users "What is your question?" and saves the response
def get_question():
    print ("What is your question?")
    question = str(input("Type your question here: "))
    return question

# give a random response as return value
def response():
    magic-8-balls = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes - definitely.",
        "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.",
        "Yes.", "Signs point to yes.", "Reply hazy, try again", "Ask again later.",
        "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.",
        "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."]
    return magic-8-balls[randint(0, 19)]
