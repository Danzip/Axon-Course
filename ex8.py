keep_game=True
while keep_game:
    player1 = raw_input("enter your move r/p/s")
    player2 = raw_input("enter your move r/p/s")
    if player1==player2:
            print("draw")
    elif player1=="r":
        if player2=="s":
            print "player1 wins"
        else:
            print "player2 wins"
    else:
        if player2=="r":
            print "player2 wins"
        else:
            print "player1 wins"
    kg=raw_input("keep playing y/n")
    if kg=="y":
        keep_game=True
    elif kg=="n":
        keep_game=False


