import random

class Kitten:
    def __init__(self, name):
        self.name = ("Daiquiri")
        self.money = 100
        self.happiness = 20
        self.satiety = 50
        self.food = 0

        print(f"The kitten is named {self.name}")
        print(f"The balance right now is {self.money}")
        print(f"The happiness count i believe is on {self.happiness}")
        print(f"I wonder if the Kittens hungry... his satiety equals to {self.satiety}")
        print(f"The kitten got {self.food} amount of food in his fridge.")


    def get_money(self):
        if self.money <= 50:
            print("Looking for money...")
            self.money += 80
            self.happiness += 20

    def eat(self):
        if self.food <= 0:
            self.shopping("food")
            print("Got to buy food!")
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.food -=5
            print("time to eat!")



    def shopping(self, manage):
        if manage == 'food':
            print("I bought food")
            self.money -= 50
            self.food += 50
        elif manage == "delicacies":
            print("Hooray! Delicious!")
            self.happiness += 10
            self.satiety += 2
            self.money -= 15

    def sleep(self):
        self.happiness += 10
        print("I am full of energy now!")


    def days_indexes(self, day):
        day = f" Today the {day} of{self.name}'s life "
        print(f"{day:=^50}", "\n")
        kitten_indexes = self.name + "'s indexes"
        print(f"{kitten_indexes:^50}", "\n")
        print(f"Money – {self.money}")
        print(f"Satiety – {self.satiety}")
        print(f"Happiness – {self.happiness}")
        print(f"Food - {self.food}")

    def is_alive(self):
        if self.happiness < 0:
            print("Depression…")
            return False
        if self.satiety < 0:
            print("Dead…")
            return False
        if self.money < -500:
            print("bankrupt...")
            return False

    def live(self, day):
        if self.is_alive() == False:
            return False
        self.days_indexes(day)
        dice = random.randint(1, 4)
        if self.satiety < 20:
            print("I'll go eat")
            self.eat()
        elif self.happiness < 20:
            print("Let`s chill!")
            self.sleep()
        elif dice == 1:
            print("Let`s sleep!")
            self.sleep()
        elif dice == 2:
            print("Time for treats!")
            self.shopping(manage="delicacies")

