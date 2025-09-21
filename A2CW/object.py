import datetime

class LibraryItem: 
    def __init__(self, t , a , i):
        self.__Title = t
        self.__Author__Artist = a
        self.__ItemID = i
        self.__OnLoan = False
        self.__DueDate = datetime.date.today()
    def GetTitle(self):
        return (self.__Title)
    def GetItemID(self):
        return (self.__ItemID)
    def GetAuthor(self):
        return (self.__Author__Artist)
    def Borrowing(self):
        self.__OnLoan = True
        self.__DueDate = self.__DueDate + datetime.timedelta(weeks=1)
    def Returning(self):
        self.__OnLoan = False
    def PrintDetails(self):
        print("Title:" , self.__Title)
        print("Creator:" , self.__Author__Artist)
        print("ItemID:", self.__ItemID)
        print("On loan:", self.__OnLoan)
        print("DueDate:", self.__DueDate)        

class Book(LibraryItem):
    def __init__(self, t , a , i):
        LibraryItem.__init__(self, t, a , i)
        self.__IsRequested = False
    def GetIsRequested(self):
        return (self.__IsRequested)
    def SetIsRequested(self, r):
        self.__IsRequested = r
    def PrintDetails(self):
        LibraryItem.PrintDetails(self)
        print("is requested:" , self.__IsRequested)

class CD(LibraryItem):
    def __init__(self , t , a , i ):
        LibraryItem.__init__(self, t , a , i)
        self.__Genre = ""
    def GetGenre(self):
        return (self.__Genre)
    def SetGenre(self, g):
        self.__Genre = g


myBook = Book("Harry Potter","JK Rowling",123)
myBook.Borrowing()
myBook.PrintDetails()


#polymorphism: the method behaves differently for different classes in the hierarchy

#Containment: a relationship in which one class has a component that is of another class type