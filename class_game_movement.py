#based on the choice of the player to behave
class GameMovement():
    def __init__(self,action):
        self.action = action

    def new_hint(self,points,hint_list,current_hint_no):
        print(hint_list[current_hint_no +1])

    def guess(self):
        guess_input = input("What is your guess?")
        return guess_input

    def quit(self):
        game_over = "Yes"
        return game_over


