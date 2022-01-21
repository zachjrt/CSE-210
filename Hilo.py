import random



#TODO: Create a Card Class
class Card:
    def __init__(self):
        self.value = random.randint(1, 13)

    def display(self):
        return self.value

    def firstDisplay(self):
        """
        Display function
        """
        print(f"The card is: {self.value}")

    def secondDisplay(self):
        print(f"Next card was: {self.value}")

#TODO: Create a Score Class
class Score:
    def __init__(self):
        self.points = 300

    def display(self):
        return self.points
    def subtract(self, int):
        self.points -= int
        
    def add(self, int):
        self.points += int


#TODO: Create a Main driver function
def main():
    gamePlay = True
    playerScore = Score()

    while (gamePlay):
        cardA = Card()
        cardB = Card()
        print("")
        cardA.firstDisplay()
        guess = input("Higher or lower? [h/l] ")
        cardB.secondDisplay()

        
        if (guess == "h"):
            if(cardA.value > cardB.value):
                playerScore.subtract(75)
            elif(cardA.value < cardB.value):
               playerScore.add(100)
            else:
                playerScore.add(0)
        
        elif (guess == "l"):
            if(cardA.value < cardB.value):
                playerScore.subtract(75)
            elif(cardA.value > cardB.value):
               playerScore.add(100)
            else:
                playerScore.add(0)
        else:
            print("Error enter correct value")

        print(f"your score is: {playerScore.display()}")

        again = input("Play again? [y/n] ")

        if (again == "n"):
            gamePlay = False
  
          
        




if __name__ == "__main__":
    main()