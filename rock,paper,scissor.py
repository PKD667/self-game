import random

play = []

def player(number) :
   global play
   words = ("Rock", "Paper", "scissor")
   word = random.choice(words)
   correct = word
   play.append(word)

def verifier(play) :
    win = None
    if play[0]== "Rock" :
        if play[1] == "Rock" : 
            win = None
        if play[1] == "Paper" :
            win = 1
        if play[1] == "scissor" :
            win = 0
    if play[0] == "Paper" :
        if play[1] == "Paper" : 
            win = None
        if play[1] == "scissor" :
            win = 1
        if play[1] == "Rock" :
            win = 0
    if play[0] == "scissor" :
        if play[1] == "scissor" : 
            win = None
        if play[1] == "Rock" :
            win = 1
        if play[1] == "Paper" :
            win = 0
    return win
Win = []
zero = 0
un = 0
for i in range(100000) :
    for p in range(2) :
        player(p)
    print(play)
    Win.append(verifier(play))
    play = []
print(Win)
for w in range(len(Win)) :
    if Win[w] == 0 :
        zero += 1
    elif Win[w] == 1 :
        un += 1
print("\n 0 : ",zero,"\n 1 : ",un)


