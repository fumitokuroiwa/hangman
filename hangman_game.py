#python learning
#hangman game

def hangman(word):
    wrong =0
    stages = ["",
    "_______            ",
    "|      |           ",
    "|      0           ",
    "|     /|\          ",
    "|     / \          ",
    "|                  "
    ]
    rletters= list(word)
    board = ["_"]*len(word)
    win=False
    print("welcome to Hangman!!")
#    print(word)

    while wrong < len(stages) -1 :
        print("\n")
        if word == "cat":
            print("Question: Animal & Cute & Not dog.")
        else:
            print("Question: Animal & cool & Not cat.")
            
        msg = "Please assume one characture.: "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong +=1
        print("".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("You win!!")
            print("Answer is:"," ".join(board))
            win = True
            break

    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("You are lose..Answer is {}.".format(word))

#hangman("cat")
hangman("dog")