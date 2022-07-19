print("Player one's turn.")
inp = input("Enter Rock, Paper or Scissors: ")
print("Player two's turn.")
inp2 = input("Enter Rock, Paper or Scissors: ")
linp = inp.lower()
linp2 = inp2.lower()
if str(linp) == str(linp2):
    print("Draw!")
#rock
if str(linp) == "rock":
    if str(linp2) == "paper":
        print("Player 2 wins!")
    elif str(linp2) == "scissors":
        print("Player 1 wins!")
#paper
if str(linp) == "paper":
    if str(linp2) == "rock":
        print("Player 1 wins!")
    elif str(linp2) == "scissors":
        print("Player 2 wins!")
#scissors
if str(linp) == "scissors":
    if str(linp2) == "rock":
        print("Player 2 wins!")
    elif str(linp2) == "paper":
        print("Player 1 wins!")

#if inp.lower == "rock" and inp2.lower == "rock":
#    print("Player 1: Rock. Player 2: Rock. Draw!")
#if inp.lower == "rock" and inp2.lower == "paper":
#    print("Player 1: Rock. Player 2: Paper. Player 2 wins!")
#if inp.lower == "rock" and inp2.lower == "scissors":
#    print("Player 1: Rock. Player 2: Scissors. Player 1!")
#if inp.lower == "paper" and inp2.lower == "rock":
#    print("Player 1: Paper. Player 2: Rock. Player 1 wins!")
#if inp.lower == "paper" and inp2.lower == "paper":
#    print("Player 1: Paper. Player 2: Paper. Draw!")
#if inp.lower == "paper" and inp2.lower == "scissors":
#    print("Player 1: Paper. Player 2: Scissors. Player 2 wins!")
#if inp.lower == "scissors" and inp2.lower == "rock":
#    print("Player 1: Scissors. Player 2: Rock. Player 2 wins!")
#if inp.lower == "scissors" and inp2.lower == "paper":
#    print("Player 1: Scissors. Player 2: Paper. Player 1 wins!")
#if inp.lower == "scissors" and inp2.lower == "scissors":
#    print("Player 1: Scissors. Player 2: Scissors. Draw!")
