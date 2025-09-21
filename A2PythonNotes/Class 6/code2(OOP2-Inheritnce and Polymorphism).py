import datetime

class LibraryItem:
    def __init__(self, t, a, i):
        self.__Title = t
        self.__Author__Artist = a
        self.__ItemID = i
        self.__OnLoan = False
        self.__DueDate = datetime.date.today()

    def GetTitle(self):
        return self.__Title
    
    def GetAuthorArtist(self):
        return self.__Author__Artist
    
    def GetItemID(self):
        return self.__ItemID
    
    def GetOnLoan(self):
        return self.__OnLoan
    
    def GetDueDate(self):
        return self.__DueDate
    
    def Borrowing(self):
        self.__OnLoan = True
        self.__DueDate = self.__DueDate + datetime.timedelta(weeks=3)

    def Returning(self):
        self.__OnLoan = False

    def PrintDetails(self):
        print("Title:", self.__Title)
        print("Author/Artist:", self.__Author__Artist)
        print("ID:", self.__ItemID)
        print("On Loan:", self.__OnLoan)
        print("Due Date:", self.__DueDate)

class Book(LibraryItem):
    def __init__(self, t, a, i):
        LibraryItem.__init__(self, t, a, i)
        self.__IsRequested = False
        self.__RequestedBy = ""

    def SetRequestedBy(self, r):
        self.__RequestedBy = r

    def SetIsRequested(self, s):
        self.__IsRequested = True

    def PrintDetails(self):
        LibraryItem.PrintDetails(self)
        print("Requested By:", self.__RequestedBy)

class CD(LibraryItem):
    def __init__(self, t, a, i):
        LibraryItem.__init__(self, t, a, i)
        self.__Genre = ""

    def SetGenre(self, g):
        self.__Genre = g

    def GetGenre(self):
        return self.__Genre
    
ThisBook = Book("Harry Potter", "JK Rowling", 23)
ThisBook.SetRequestedBy("xyz")
ThisBook.PrintDetails()

print()

ThisCD = CD("ABC", "DEF", 153)
ThisCD.SetGenre("Music")
print(ThisCD.GetGenre())
ThisCD.PrintDetails()
