#!/usr/bin/env python3


def main():
    
    round = 0

    while round < 3:
        print('Finish the movie title, "Monty Python\'s The Life of ______"')

        movie_answer = input()

        if movie_answer == "Brian":
            print("Correct")
            break
        elif round <2:
            print("Incorrect.  Try Again")

        round = round + 1
        
    if round == 3:
        print("Sorry, the answer was Brian.")

main()
