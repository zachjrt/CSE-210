import random



#TODO: Create a Card Class
class Card:
    def __init__(self):
        self.value = random.randint(1, 13)

    def display(self):
        """
        basic display function

        returns vale of card
        """
        return self.value

    def firstDisplay(self):
        """
        Display function

        Returns first card value in format
        """
        print(f"The card is: {self.value}")

    def secondDisplay(self):
        """
        Second Display

        Returns second card value in format
        """
        print(f"Next card was: {self.value}")


class Score:
    def __init__(self):
        #Total Points
        self.points = 300

    def display(self):
        """
        Display

        Shows score
        """
        print(f"your score is: {self.points}")


    def subtract(self, int):
        """
        subtract

        subtracts int arg from total points
        """
        self.points -= int
        
    def add(self, int):
        """
        add

        adds int arg from total points
        """
        self.points += int


#TODO: Create a Main driver function
def main():
    """
     Main driver of the game
    sets playing to true
    creates score object
    """
    gamePlay = True
    playerScore = Score()

    """
    This while loop is the main loop
    Creates two card objects
    Displays one
    prompts user to guess h or l
    Displays the second card
    Assigns points depending on guess
    Shows points
    Asks if they want to play again
    Repeats if yes
    """
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


        playerScore.display()

        again = input("Play again? [y/n] ")

        if (again == "n"):
            gamePlay = False
  
          
        




if __name__ == "__main__":
    main()