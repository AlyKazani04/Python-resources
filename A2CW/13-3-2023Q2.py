#a
class Card:
    #__Number as INTEGER
    #__Colour as STRING
    def __init__(self,num,col):
        self.__Number = num
        self.__Colour = col

    def GetNumber(self):
        return self.__Number
    def GetColour(self):
        return self.__Colour
