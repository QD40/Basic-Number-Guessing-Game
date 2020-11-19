import random


class Game(object):
    true = 0
    wrong = 0
    count = true + wrong
    point = (true * 10) - wrong

    def stats(self):
        print("Total Times Played: ", self.count)
        print("Total True Answer: ", self.true)
        print("Total Wrong Answer: ", self.wrong)
        print("Your Point: ", self.point)

    def intruduce(self):
        print("Your mission is just guess to correct numbers")
        print("Keep your point bigger than -12 or you will lose")
        print("Level 1: 1-10")
        print("Level 2: 1-20")
        print("Level 3: 1-30")
        print("Level 4: 1-40")
        print("Level 5: 1-50")
        print("Keeps Like This...")

    def gamearea(self):
        q = 1
        lvl = 1
        x = 10
        while q == 1 and self.point > -12 :
            print("Level: ", lvl)
            correct_number = random.randint(1,x)
            guessed_number = int(input("Your Guess: "))
            if correct_number != guessed_number:
                while correct_number != guessed_number and self.point > -12:
                    if correct_number > guessed_number:
                        print("Try Higher!")
                        self.wrong += 1
                        self.count += 1
                    elif correct_number < guessed_number:
                        print("Try Lower!")
                        self.wrong += 1
                        self.count += 1
                    guessed_number = int(input("Your Guess: "))
            if correct_number == guessed_number:
                self.true += 1
                print("Correct Answer")
                q = int(input("1) Keep Playing / 2) Exit  // (1/2): "))
                if q == 1:
                    x += 10
                    lvl += 1
                else:
                    q = 2
        self.point = (self.true * 10) - self.wrong
        self.count = self.true + self.wrong







game = Game()
game.intruduce()
game.gamearea()
game.stats()
