def hangman(word):
        wrong = 0
            stages = ["",
                                  "_______      ",
                                                "|            ",
                                                              "|      |     ",
                                                                            "|  　　０     ",
                                                                                          "|     /|\    ",
                                                                                                        "|     / \    ",
                                                                                                                      "|            ",
                                                                                                                                     ]
                rletters = list(word)
                    board = ["_"] * len(word)
                        win = False
                            print("Welcome to the hangman!")
                                
                                    while wrong < len(stages) - 1:
                                                print("\n")
                                                        msg = "guess a word"
                                                                char = input(msg)
                                                                        if char in rletters:
                                                                                        cind = rletters.index(char)
                                                                                                    board[cind] = char
                                                                                                                rletters[cind] = '$'
                                                                                                                        else :
                                                                                                                                        wrong += 1
                                                                                                                                                print(" ".join(board))
                                                                                                                                                        e = wrong + 1
                                                                                                                                                                print("\n".join(stages[0:e]))
                                                                                                                                                                        if "_" not in board:
                                                                                                                                                                                        print("You won!")
                                                                                                                                                                                                    print(" ".join(board))
                                                                                                                                                                                                                win = True
                                                                                                                                                                                                                            break
                                                                                                                                                                                                                            if not win:
                                                                                                                                                                                                                                        print("\n".join(stages[0:wrong+1]))
                                                                                                                                                                                                                                                print("You lost! The answer is {}".format(word))
                                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                                        animals = ['dog','cat','rat','pig']
                                                                                                                                                                                                                                                        from random import randint

                                                                                                                                                                                                                                                        hangman(animals[randint(0,len(animals))])
                                                                                                                                                                                                                                                            
