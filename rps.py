import random
import sys


class RPS:
    def __init__(self):
        self.user_wins = 0
        self.AI_wins = 0
        self.first_round = True
        self.won = False

    def play(self):
        while self.won == False:
            self.input_user()
            self.ai()
            self.check()
            self.wins()

    def input_user(self):
        if self.first_round == True:
            print("Hallo welcome to a game of rock paper scissors")
            print("Choose between rock paper or scissors")
            self.first_round = False
        else:
            pass
        self.user_chose = input()

    def ai(self):
        rps = list(["rock", "paper", "scissors"])
        self.AI_answer = random.choice(rps)
        print("AI", self.AI_answer)

    def check(self):
        if self.user_chose == self.AI_answer:
            print("same")
        elif self.user_chose == "rock":
            if self.AI_answer == "paper":
                # AI wins
                self.AI_wins = self.AI_wins + 1
            elif self.AI_answer == "scissors":
                # user wins
                self.user_wins = self.user_wins + 1
        elif self.user_chose == "paper":
            if self.AI_answer == "rock":
                # user wins
                self.user_wins = self.user_wins + 1
            elif self.AI_answer == "scissors":
                # AI wins
                self.AI_wins = self.AI_wins + 1
        elif self.user_chose == "scissors":
            if self.AI_answer == "paper":
                # user wins
                self.user_wins = self.user_wins + 1
            if self.AI_answer == "rock":
                # AI wins
                self.AI_wins = self.AI_wins + 1
        else:
            print("I said rock paper or scissors not that shit")
        print("user wins =", self.user_wins, "AI wins", self.AI_wins)

    def wins(self):
        if self.user_wins == 3:
            print("the humans win")
            self.won = True
        elif self.AI_wins == 3:
            print("computers wins and will always be the superior")
            self.won = True
        else:
            pass


if __name__ == '__main__':
    a = RPS()
    a.play()
