from TicTacToeClass import TicTacToe, minmax_decision, alpha_beta_search, GameState

def main():
    play_again = True
    while play_again:
        size_string = input("Input the size of the board in the form x,y")
        sizes = size_string.split(",")
        numgames = 0
        while numgames < 2:
            if numgames == 0:
                print("The Minmax decision algorithm will be used in this game")
            else:
                print("The Alpha Beta search algorithm will be used in this game")
            game = TicTacToe()
            game.__init__(int(sizes[0]), int(sizes[1]), min(int(sizes[0]), int(sizes[1])))
            game_states = []
            current_state = game.initial
            game_states.append(game.initial)
            while not game.terminal_test(current_state):
                game.display(current_state)
                print("--------------------------")
                if current_state.to_move == 'X':
                    print("X to move\n")
                    if numgames == 0:
                        new_move = minmax_decision(current_state, game)
                    else:
                        new_move = alpha_beta_search(current_state, game)
                    current_state = game.result(current_state, new_move)
                    game_states.append(current_state)
                else:
                    print("O to move\n")
                    if numgames == 0:
                        new_move = minmax_decision(current_state, game)
                    else:
                        new_move = alpha_beta_search(current_state, game)
                    current_state = game.result(current_state, new_move)
                    game_states.append(current_state)
            game.display(current_state)
            if game.utility(current_state, 'X') == 1:
                print("X wins game")
            elif game.utility(current_state, 'X') == -1:
                print("O wins game")
            else:
                print("Game tie")
            numgames += 1
        again = input("Would you like to play again? Y/N")
        if again.lower() != "y":
            play_again = False
            print("Thank You for Playing Our Game!")

if __name__ == "__main__":
    main()
