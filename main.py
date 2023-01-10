######################### ROCK, PAPER, SCISSORS - COMPUTER VS COMPUTER  ################################################
import random
import time  # time library will help to delay the print statement

def game(name1, name2, user_bet, game_rounds):
    word_list = ['rock', 'paper', 'scissors']   # list used by the system to choose a random word
    count = 0
    c1_points = 0
    c2_points = 0
    print("\n")  # inserting an empty string from the data entry
    while count < game_rounds:   # if count is less than number of rounds specified by the user then execute the code
        c1_choice = random.choice(word_list)  # choose random word for first computer
        c2_choice = random.choice(word_list)  # choose random word for second computer
        print(f"{name1} chose {c1_choice} and {name2} chose {c2_choice}")  # print the chosen word
        time.sleep(0.5)  # delay of 0.5 seconds
        # this if condition will be used to check all the possible cases:
        # E.G. C1 = Paper C2 = Rock the point will be given to the second computer/player
        if ((c1_choice == 'rock' and c2_choice == "paper") or
                (c1_choice == "paper" and c2_choice == 'scissors') or
                (c1_choice == "scissors" and c2_choice == 'rock')):
            c2_points += 1
            # print the round number and the current score
            print(f'The score after round {count + 1} is : {name1} : {c1_points}   {name2}: {c2_points}')
            time.sleep(0.5)
            print("")

        elif ((c1_choice == 'rock' and c2_choice == "rock") or
              (c1_choice == "paper" and c2_choice == 'paper') or
              (c1_choice == "scissors" and c2_choice == 'scissors')):
            print(f"You both chose same elements! No score given!")
            print(f'The score after round {count + 1} is : {name1} : {c1_points}   {name2}: {c2_points}')
            time.sleep(0.5)
            print("")
        elif ((c1_choice == 'paper' and c2_choice == "rock") or
              (c1_choice == "scissors" and c2_choice == 'paper') or
              (c1_choice == "rock" and c2_choice == 'scissors')):
            c1_points += 1
            print(f'The score after round {count + 1} is: {name1} : {c1_points}    {name2}: {c2_points}')
            time.sleep(0.5)
            print("")
        # increasing the counter
        count += 1

    # if the score of the first player/computer is greater than the second one then print you won including the name
    if c1_points > c2_points:
        print(f"{name1} won!")
        # if the user did bet on the first player, it will display that he guesses it right
        if user_bet == "a":
            print("You guessed it right")
        # if he did not bet on him, it will print that he is wrong.
        else:
            print("Your guess was wrong! Better luck next time :(")
    elif c2_points > c1_points:
        print(f"{name2} won!")
        if user_bet == "b":
            print("You guessed it right")
        else:
            print("Your guess was wrong! Better luck next time :(")
    # if the scores of both players are same it will print that it is a tie
    else:
        print("It is a tie!")


comp1_name = input("Give a name to the first computer: ").upper()  # stores the name of the first player/computer
comp2_name = input("Give a name to the second computer: ").upper()  # stores the name of the second player/computer
user_guess = input(f"Who do you think will win? {comp1_name} (A) or {comp2_name} (B)? ").lower()  # stores user bet

# Try Except will be used to raise an exception if in case the number of rounds that have been given is not an integer
try:
    rounds = int(input("How many rounds do you want them to play? "))  # stores the number of rounds
    game(comp1_name, comp2_name, user_guess, rounds)  # recalling the function and passing the variables
except ValueError:  # raising exception for value error
    print("You chose wrong value type for the rounds!")
