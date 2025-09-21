class Card:
    def __init__(self,num,col):
        self.__Number = num
        self.__Colour = col

    def GetNumber():
        return self.__Number

    def GetColour():
        return self.__Colour

oneRed = Card(1,"red")
twoRed = Card(2,"red")
threeRed = Card(3,"red")
fourRed = Card(4,"red")
fiveRed = Card(5,"red")
oneBlue = Card(1,"blue")
twoBlue = Card(2,"blue")
threeBlue = Card(3,"blue")
fourBlue = Card(4,"blue")
fiveBlue = Card(5,"blue")
oneYellow = Card(1, "yellow")
twoYellow = Card(2, "yellow")
threeYellow = Card(3, "yellow")
fourYellow = Card(4, "yellow")
fiveYellow = Card(5, "yellow")

class Hand:
    def __init__(self, card1, card2, card3, card4, card5):
        self.__Cards = []
        self.__Cards.append(card1)
        self.__Cards.append(card2)
        self.__Cards.append(card3)
        self.__Cards.append(card4)
        self.__Cards.append(card5)
        self.__FirstCard = 0
        self.__NumberCards = 5

    def GetCard(self, index):
        return self.__Cards[index]

player1 = Hand(oneRed, twoRed, threeRed, fourRed, oneYellow)
player2 = Hand(twoYellow, threeYellow, fourYellow, fiveYellow, oneBlue)

#c
def CalculateValue(pHand):
    score = 0
    for i in range(5):
        thisCard = pHand.GetCard(i)
        cardColour = pHand.GetColour(i)
        if cardColour == "blue":
            score += 10
        elif cardColour == "red":
            score += 5
        else:
            score += 15
        score = score +thisCard.GetNumber()
    return score
p1score = CalculateValue(player1)
p2score = CalculateValue(player2)
if p1score > p2score:
    print("player 1 wins")
elif p2score > p1score:
    print("player 2 wins")
else:
    print("its a tie")