import random
import sys


class rsp:
    def __init__(self):
        pass

    def play(self):
        self.input_user()
        self.ai()
        self.check()

    def input_user(self):
        print("Hallo welkom a game of rock paper scissors")
        print("Choose between rock paper or scissors")
        self.user_chose = input()

    def ai(self):
        rps = list(["rock", "paper", "scissors"])
        self.AI_answer = random.choice(rps)
        print(self.AI_answer)

    def check(self):
        if self.user_chose == self.AI_answer:
            print("same")
            sys.exit(0)
        elif self.user_chose == "rock":
            if self.AI_answer == "paper":
                print("you loss")
            elif self.AI_answer == "scissors":
                print("you win")
        elif self.user_chose == "paper":
            if self.AI_answer == "rock":
                print("you win")
            elif self.AI_answer == "scissors":
                print("you loss")
        elif self.user_chose == "scissors":
            if self.AI_answer == "paper":
                print("you win")
            if self.AI_answer == "rock":
                print("you loss")
        else:
            print("I said rock paper or scissors not that shit")


if __name__ == '__main__':
    a = rsp()
    a.play()
