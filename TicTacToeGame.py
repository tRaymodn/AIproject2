from TicTacToeClass import TicTacToe, minmax_decision, alpha_beta_search, GameState

def main():
    play_again = True
    while play_again:
        size_string = input("Input the size of the board in the form x,y")
        sizes = size_string.split(",")
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
                new_move = alpha_beta_search(current_state, game)
                current_state = game.result(current_state, new_move)
                game_states.append(current_state)
                """correct_move = False  ## User input for player 'X'
                while not correct_move:
                    move_string = input("Input an ordered pair x,y for the position to place your X")
                    coords = move_string.split(",")
                    new_move = (int(coords[1]), int(coords[0]))
                    if not game.result(current_state, new_move) == current_state:
                        correct_move = True
                    else:
                        print("Incorrect input")
                current_state = game.result(current_state, new_move)
                game_states.append(current_state)"""
            else:
                print("O to move\n")
                new_move = minmax_decision(current_state, game)
                current_state = game.result(current_state, new_move)
                game_states.append(current_state)
        game.display(current_state)
        print("Game End")
        again = input("Would you like to play again? Y/N")
        if again.lower() != "y":
            play_again = False
        else:
            print("Thank You for Playing Our Game!")

if __name__ == "__main__":
    main()