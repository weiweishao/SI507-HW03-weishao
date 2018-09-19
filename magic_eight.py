# SI 507 Hw3
# Group Member:
# Person A: Wei Shao    
# Person B: Zhen Wang
# Section 003: Wednesday 10:00 - 11:30 AM

import random

# create a function that ask users "What is your question?" and saves the response
def get_question():
    print ("What is your question?")
    question = str(input("Type your question here: "))
    return question

# check if user input is a question: if yes, return the question;
# if no, ask for a question and return the question, or,
# ask until the user type in "quit" (or other forms of quit)

def check_question(q):
    lst_q = list(q)
    ends = lst_q[-1]
    while ends != "?":
        print ("I'm sorry, I can only answer questions.")
        print ("What is your question?")
        q = str(input("Your question: "))
        q_lst = list(q)
        ends = q_lst[-1]
        if q in ["quit.","quit","Quit","Quit.","QUIT.","QUIT"]:
            break
    return q



# create a function of the magic 8-ball game
def magic_8_ball():
    question = get_question()
    q = check_question(question)
    if q in ["quit.","quit","Quit","Quit.","QUIT.","QUIT"]:
        print ("You choose to quit the game.")
    else:
        output = get_answer()
        print ("The answer is: " + output)


magic_8_ball()          

